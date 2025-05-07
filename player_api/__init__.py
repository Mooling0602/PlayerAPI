from dataclasses import dataclass, field
from pydantic import HttpUrl
from typing import Optional
from uuid import UUID


@dataclass
class Player:
    name: str
    uuid: UUID
    online_mode: Optional[bool] = None
    official_account: Optional[bool] = None
    api: Optional[HttpUrl] = None
    service_name: Optional[str] = None


@dataclass
class OfflinePlayer(Player):
    online_mode: bool = field(default=False, init=False)
    official_account: bool = field(default=False, init=False)
    api: Optional[HttpUrl] = field(default=None, init=False)
    service_name: str = "offline"

@dataclass
class OnlinePlayer(Player):
    online_mode: bool = field(default=True, init=False)
    official_account: bool
    api: Optional[HttpUrl] = None
    service_name: Optional[str] = None # not actually works, just as a tag.

@dataclass
class OfficialPlayer(OnlinePlayer):
    official_account: bool = field(default=True, init=False)
    api: Optional[HttpUrl] = "https://api.mojang.com/users/profiles/minecraft"
    service_name: str = "mojang"

class YggdrasilPlayer(OnlinePlayer):
    official_account: bool = field(default=False, init=False)
    service_name: str = "yggdrasil" # can be changed on your like.
    api: HttpUrl

class FloodgatePlayer(OnlinePlayer):
    official_account: bool = field(default=False, init=False)
    service_name: str = "floodgate"

# Testing codes.
player = OfficialPlayer(name="CleMooling", uuid="392cdfd1-0016-4afa-ae13-66488ef79bb9")
print(player)