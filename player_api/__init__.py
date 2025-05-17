"""PlayerAPI - A Python lib and a MCDReforged plugin \
    for querying and managing Minecraft player information.
"""
from dataclasses import dataclass, field
from enum import StrEnum, auto
from typing import Optional
from uuid import UUID

import requests

from pydantic import HttpUrl


class ServiceType(StrEnum):
    """
    The type of service.
    """
    OFFLINE = auto()
    MOJANG = auto()
    YGGDRASIL = auto()
    FLOODGATE = auto()


def is_from_floodgate(uuid: Optional[UUID]) -> bool:
    """Check if the UUID is from Floodgate.

    Floodgate player's UUID is prefixed with "00000000", \
        so we can check if it is.

    Args:
        uuid (Optional[UUID]): The UUID to check.

    Returns:
        bool: True if the UUID is from Floodgate, False otherwise.
    """
    if uuid:
        if str(uuid).startswith("00000000"):
            return True
    return False


@dataclass
class Player:
    """Basic player class.

    Any subclass based on this class should have the following attributes.

    Args:
        name (Optional[str]): Player name, used in \
            vanilla chat format and logs, commands, etc.
        uuid (Optional[UUID]): UUID of the player.
        online_mode (Optional[bool]): \
            Whether the player is in online mode or not.
        official_account (Optional[bool]): \
            Whether the player's account has been verified by Mojang/Microsoft.
        api (Optional[HttpUrl|str]): Login service API address.
        service_name (Optional[str]): Login service name.

    Raises:
        TypeError: If no necessary arguments are provided.
    """
    name: Optional[str] = None
    uuid: Optional[UUID] = None
    online_mode: Optional[bool] = None
    official_account: Optional[bool] = None
    api: Optional[HttpUrl | str] = None
    service_name: Optional[str] = None

    def __post_init__(self):
        if self.uuid is None and self.name is None:
            raise TypeError("no necessary given informations!")
        if isinstance(self.uuid, str):
            self.uuid = UUID(self.uuid)
        if isinstance(self.api, str):
            self.api = HttpUrl(self.api)


@dataclass
class OfflinePlayer(Player):
    """Offline player class.

    Missing attributes see class `Player`.

    Args:
        online_mode (Optional[bool]): Force the player to be offline mode.
            Defaults to False.
        official_account (Optional[bool]): \
            Force the player's account hasn't been verified by \
                Mojang/Microsoft.
            Defaults to False.
        api (Optional[HttpUrl]): \
            Force the login service's api address to be empty.
            Defaults to None.
        service_name (Optional[str]): \
            Force the login service's name to be "offline".
            Defaults to "offline".
    """
    online_mode: Optional[bool] = field(default=False, init=False)
    official_account: Optional[bool] = field(default=False, init=False)
    api: Optional[HttpUrl | str] = field(default=None, init=False)
    service_name: Optional[str] = ServiceType.OFFLINE


@dataclass
class OnlinePlayer(Player):
    """Online player class.

    Missing attributes see class `Player`.

    Args:
        online_mode (Optional[bool]): Whether the player is online.
    """
    online_mode: Optional[bool] = field(default=True, init=False)


@dataclass
class OfficialPlayer(OnlinePlayer):
    """Official player class.

    Missing attributes see class `Player`.

    Args:
        official_account (Optional[bool]): \
            Force the player's account has been verified by Mojang/Microsoft.
        api (Optional[HttpUrl|str]): Force to use the official API URL.
        service_name (Optional[str]): Force to be "mojang".

    Raises:
        TypeError: If a floodgate player's UUID detected.
    """
    official_account: Optional[bool] = field(default=True, init=False)
    # if you want to modify it, plz keep the same format.
    api: Optional[HttpUrl | str] = HttpUrl(
        "https://api.mojang.com/users/profiles/minecraft/"
    )
    service_name: Optional[str] = ServiceType.MOJANG

    def __post_init__(self):
        if is_from_floodgate(self.uuid):
            raise TypeError("Invalid player uuid, seems a floodgate one?")
        if self.name and not self.uuid:
            response = requests.get(str(self.api) + self.name, timeout=5)
            if response.status_code == 200:
                self.uuid = UUID(response.json().get("id", None))
        if self.uuid and not self.name:
            url = (
                "https://sessionserver.mojang.com/session/minecraft/profile/"
                + str(self.uuid)
            )
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                self.name = response.json().get("name", None)
        super().__post_init__()


@dataclass
class YggdrasilPlayer(OnlinePlayer):
    """Yggdrasil player class.

    Missing attributes see class `Player`.

    Args:
        official_account (Optional[bool]): \
            Force the player's account hasn't been verified \
                by Mojang/Microsoft.
        service_name (Optional[str]): Force to be "yggdrasil".

    Raises:
        TypeError: If not provided yggdrasil api address.
    """
    official_account: Optional[bool] = field(default=False, init=False)
    service_name: Optional[str] = ServiceType.YGGDRASIL

    def __post_init__(self):
        if not self.api:
            raise TypeError("Missing Yggdrasil api address!")
        if self.name and not self.uuid:
            url = f"{self.api}/api/profiles/minecraft"
            response = requests.post(url, json=[self.name], timeout=5)
            if response.status_code == 200:
                results = response.json()
                if results and isinstance(results, list) and len(results) > 0:
                    self.uuid = UUID(results[0].get("id", None))
        super().__post_init__()


@dataclass
class FloodgatePlayer(OnlinePlayer):
    """Floodgate player class.

    Args:
        official_account (Optional[bool]): \
            Because unable to check if a bedrock player has bought the game, \
            so force the player's account hasn't been verified \
                by Mojang/Microsoft.

    Raises:
        TypeError: If the uuid mismatches the player's type.
    """
    official_account: Optional[bool] = field(default=False, init=False)

    def __post_init__(self):
        super().__post_init__()
        if not is_from_floodgate(self.uuid):
            raise TypeError("Invalid floodgate player uuid!")


# Test module.
def test():
    """Test module.
    """
    player = OfficialPlayer(name="CleMooling")
    print(player)
    ygg_player = YggdrasilPlayer(
        name="Mooling0602",
        api="https://littleskin.cn/api/yggdrasil"
    )
    print(ygg_player)


# test()
# * Uncomment this line to run the test module.
