import requests

from dataclasses import dataclass, field
from enum import StrEnum, auto
from pydantic import HttpUrl
from typing import Optional
from uuid import UUID


class ServiceType(StrEnum):
    OFFLINE = auto()
    MOJANG = auto()
    YGGDRASIL = auto()
    FLOODGATE = auto()

def is_from_floodgate(uuid: UUID) -> bool:
    if uuid:
        if str(uuid).startswith("00000000"):
            return True
    return False

@dataclass
class Player:
    name: Optional[str] = None
    uuid: Optional[UUID] = None
    online_mode: Optional[bool] = None
    official_account: Optional[bool] = None
    api: Optional[HttpUrl] = None
    service_name: Optional[str] = None

    def __post_init__(self):
        if self.uuid is None and self.name is None:
            raise TypeError("no necessary given informations!")
        if isinstance(self.uuid, str):
            self.uuid = UUID(self.uuid)
        
@dataclass
class OfflinePlayer(Player):
    online_mode: bool = field(default=False, init=False)
    official_account: bool = field(default=False, init=False)
    api: Optional[HttpUrl] = field(default=None, init=False)
    service_name: str = ServiceType.OFFLINE

@dataclass
class OnlinePlayer(Player):
    online_mode: bool = field(default=True, init=False)
    official_account: bool
    api: Optional[HttpUrl] = None
    service_name: Optional[str] = None # not actually works, just as a tag.

@dataclass
class OfficialPlayer(OnlinePlayer):
    official_account: bool = field(default=True, init=False)
    api: Optional[HttpUrl] = "https://api.mojang.com/users/profiles/minecraft/" # if you want to modify it, plz keep the same format.
    service_name: str = ServiceType.MOJANG

    def __post_init__(self):
        if is_from_floodgate(self.uuid):
            raise TypeError("Invalid player uuid, seems a floodgate one?")
        if self.name and not self.uuid:
            response = requests.get(self.api + self.name, timeout=5)
            if response.status_code == 200:
                self.uuid = UUID(response.json().get("id", None))
        if self.uuid and not self.name:
            url = "https://sessionserver.mojang.com/session/minecraft/profile/" + str(self.uuid)
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                self.name = response.json().get("name", None)
        super().__post_init__()

@dataclass
class YggdrasilPlayer(OnlinePlayer):
    official_account: bool = field(default=False, init=False)
    service_name: str = ServiceType.YGGDRASIL
    api: HttpUrl
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
    official_account: bool = field(default=False, init=False)
    def __post_init__(self):
        super().__post_init__()
        if not is_from_floodgate(self.uuid):
            raise TypeError("Invalid floodgate player uuid!")
        if not is_from_floodgate(self.uuid):
            raise TypeError("Invalid floodgate player uuid!")

# Test module.
def test():
    player = OfficialPlayer(name="CleMooling")
    print(player)
    ygg_player = YggdrasilPlayer(name="Mooling0602", api="https://littleskin.cn/api/yggdrasil")
    print(ygg_player)

# test()