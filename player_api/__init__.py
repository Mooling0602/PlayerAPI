from dataclasses import dataclass, field
from pydantic import HttpUrl
from typing import Optional
from uuid import UUID


@dataclass
class Player:
    name: str
    uuid: UUID
    online_mode: bool

class OfflinePlayer(Player):
    online_mode: bool = field(default=False, init=False)

class OnlinePlayer(Player):
    online_mode: bool = field(default=True, init=False)
    official_account: bool
    api: Optional[HttpUrl]
    service_name: Optional[str] # not actually works, just as a tag.

class OfficialPlayer(OnlinePlayer):
    official_account: bool = field(default=True, init=False)
    service_name: str = "microsoft"

class YggdrasilPlayer(OnlinePlayer):
    official_account: bool = field(default=False, init=False)
    service_name: str = "yggdrasil" # can be changed on your like.
    api: HttpUrl

class FloodgatePlayer(OnlinePlayer):
    official_account: bool = field(default=False, init=False)
    service_name: str = "floodgate"