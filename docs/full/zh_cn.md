# 模块索引

* [player\_api](#player_api)
  * [ServiceType](#player_api.ServiceType)
  * [is\_from\_floodgate](#player_api.is_from_floodgate)
  * [Player](#player_api.Player)
  * [OfflinePlayer](#player_api.OfflinePlayer)
  * [OnlinePlayer](#player_api.OnlinePlayer)
  * [OfficialPlayer](#player_api.OfficialPlayer)
  * [YggdrasilPlayer](#player_api.YggdrasilPlayer)
  * [FloodgatePlayer](#player_api.FloodgatePlayer)
  * [test](#player_api.test)
* [player\_api.mcdr.runtime](#player_api.mcdr.runtime)
  * [cfg](#player_api.mcdr.runtime.cfg)
  * [psi](#player_api.mcdr.runtime.psi)
* [player\_api.mcdr.config](#player_api.mcdr.config)
  * [OnlineModules](#player_api.mcdr.config.OnlineModules)
  * [PluginModules](#player_api.mcdr.config.PluginModules)
  * [PluginConfig](#player_api.mcdr.config.PluginConfig)
    * [enable](#player_api.mcdr.config.PluginConfig.enable)
  * [config\_loader](#player_api.mcdr.config.config_loader)
* [player\_api.mcdr](#player_api.mcdr)
  * [on\_load](#player_api.mcdr.on_load)
  * [on\_server\_startup](#player_api.mcdr.on_server_startup)
* [player\_api.mcdr.utils](#player_api.mcdr.utils)
* [player\_api.mcdr.modules.binder](#player_api.mcdr.modules.binder)
* [player\_api.mcdr.modules.online](#player_api.mcdr.modules.online)
* [player\_api.utils](#player_api.utils)
  * [execute\_if](#player_api.utils.execute_if)
  * [get\_time](#player_api.utils.get_time)
  * [get\_time\_styled](#player_api.utils.get_time_styled)
  * [format\_time](#player_api.utils.format_time)

<a id="player_api"></a>

# player\_api

PlayerAPI - 一个 Python 库和 MCDReforged 插件用于查询和管理 Minecraft 玩家信息。

<a id="player_api.ServiceType"></a>

## ServiceType 对象

```python
class ServiceType(StrEnum)
```

服务类型

<a id="player_api.is_from_floodgate"></a>

#### is\_from\_floodgate

```python
def is_from_floodgate(uuid: Optional[UUID]) -> bool
```

检查 UUID 是否来自 Floodgate。

Floodgate 玩家的 UUID 以 "00000000" 作为前缀，据此判断。

**参数**:

- `uuid` _Optional[UUID]_ - 要检查的UUID。
  

**Returns**:

- `bool` - True 如果这个 UUID 来自 Floodgate，否则为False。

<a id="player_api.Player"></a>

## Player 对象

```python
@dataclass
class Player()
```

基础的玩家类。

任何继承自这个类的子类都应该有以下的属性（参数）。

**参数**:

- `name` _Optional[str]_ - 玩家名称，用于原版聊天格式和日志、命令等。
- `uuid` _Optional[UUID]_ - 玩家的 UUID。
- `online_mode` _Optional[bool]_ - 这个玩家是否处于在线模式。
- `official_account` _Optional[bool]_ - 这个玩家的账户是否由 Mojang 或 Microsoft 验证。
- `api` _Optional[HttpUrl|str]_ - 登录服务 API 地址。
- `service_name` _Optional[str]_ - 登录服务名称。
  

**Raises**:

- `TypeError` - 如果必要参数没有提供。

<a id="player_api.OfflinePlayer"></a>

## OfflinePlayer Objects

```python
@dataclass
class OfflinePlayer(Player)
```

离线玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**参数**:

- `online_mode` _Optional[bool]_ - 强制玩家为离线模式。
  默认为 `False`。
- `official_account` _Optional[bool]_ - 强制（认定）玩家的账户没有被 Mojang 或 Microsoft 验证。
  默认为 `False`。
- `api` _Optional[HttpUrl]_ - 强制登录服务的 API 地址为空。
  默认为 `None`。
- `service_name` _Optional[str]_ - 强制登录服务的名称为 "offline"。
  默认为 "offline"。

<a id="player_api.OnlinePlayer"></a>

## OnlinePlayer Objects

```python
@dataclass
class OnlinePlayer(Player)
```

在线玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**参数**:

- `online_mode` _Optional[bool]_ - 强制玩家为在线模式。
  默认为 `True`。

<a id="player_api.OfficialPlayer"></a>

## OfficialPlayer Objects

```python
@dataclass
class OfficialPlayer(OnlinePlayer)
```

正版（Java 版）玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**Arguments**:

- `official_account` _Optional[bool]_ - 强制（认定）玩家的账户已经被 Mojang 或 Microsoft 验证。
  默认为 `True`。
- `api` _Optional[HttpUrl|str]_ - 强制使用官方的 API URL。
  默认为 `HttpUrl("https://api.mojang.com/users/profiles/minecraft/")`。
- `service_name` _Optional[str]_ - 强制为 "mojang"。
  默认为 "mojang"。

**抛出（报错）**:

- `TypeError` - 如果检测到一个 Floodgate 玩家的 UUID。

<a id="player_api.YggdrasilPlayer"></a>

## YggdrasilPlayer Objects

```python
@dataclass
class YggdrasilPlayer(OnlinePlayer)
```

Yggdrasil（外置登录）玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**Arguments**:

- `official_account` _Optional[bool]_ - 强制（认定）玩家的账户没有被 Mojang 或 Microsoft 验证。
  默认为 `False`。
- `service_name` _Optional[str]_ - 强制为 "yggdrasil"。
  默认为 "yggdrasil"。

**Raises**:

- `TypeError` - If not provided yggdrasil api address.

<a id="player_api.FloodgatePlayer"></a>

## FloodgatePlayer Objects

```python
@dataclass
class FloodgatePlayer(OnlinePlayer)
```

Floodgate player class.

Missing attributes see [`class Player`](#player_api.Player).

**Arguments**:

- `official_account` _Optional[bool]_ - Because unable to check if a bedrock player has bought the game,             so force the player's account hasn't been verified                 by Mojang/Microsoft.
  

**Raises**:

- `TypeError` - If the uuid mismatches the player's type.

<a id="player_api.test"></a>

#### test

```python
def test()
```

Test module.

<a id="player_api.mcdr.runtime"></a>

# player\_api.mcdr.runtime

Runtime module for MCDR plugin workaround.

<a id="player_api.mcdr.runtime.cfg"></a>

#### cfg

PluginConfig instance.

This is used to access the plugin configuration.

<a id="player_api.mcdr.runtime.psi"></a>

#### psi

PluginServerInterface instance for MCDR plugin.

This is used to access the psi instance and its methods.

<a id="player_api.mcdr.config"></a>

# player\_api.mcdr.config

Config module for MCDR plugin workaround.

<a id="player_api.mcdr.config.OnlineModules"></a>

## OnlineModules Objects

```python
class OnlineModules(Serializable)
```

Plugin config options for online modules.

**Arguments**:

- `matcher` _bool_ - Matching various player information feature.
  Default to False (to disable).
- `counter` _bool_ - Online player count feature.
  Default to False (to disable).
- `timer` _bool_ - Online time statistics feature.
  Default to False (to disable).

<a id="player_api.mcdr.config.PluginModules"></a>

## PluginModules Objects

```python
class PluginModules(Serializable)
```

Plugin config options for modules.

**Arguments**:

- `online` _OnlineModules_ - Whether to enable online modules.
- `binder` _bool_ - Custom player ID feature.
  Default to False (to disable).
- `ip_logger` _bool_ - Player IP logging feature.
  Default to False (to disable).

<a id="player_api.mcdr.config.PluginConfig"></a>

## PluginConfig Objects

```python
class PluginConfig(Serializable)
```

Plugin configuration main class.

Root nodes of the config options.

**Arguments**:

- `enable` _bool_ - Whether the plugin is enabled.
- `modules` _PluginModules_ - Whether the modules to be loaded.

<a id="player_api.mcdr.config.PluginConfig.enable"></a>

#### enable

* Disable the plugin by default.

<a id="player_api.mcdr.config.config_loader"></a>

#### config\_loader

```python
def config_loader(server: PluginServerInterface) -> PluginConfig
```

Load the plugin's configuration.

<a id="player_api.mcdr"></a>

# player\_api.mcdr

MCDR plugin entrypoint.

<a id="player_api.mcdr.on_load"></a>

#### on\_load

```python
def on_load(server: PluginServerInterface, prev_module) -> None
```

Called when the plugin is loaded.

<a id="player_api.mcdr.on_server_startup"></a>

#### on\_server\_startup

```python
@execute_if(lambda: rt.cfg.modules.online.counter is True)
def on_server_startup(server: PluginServerInterface)
```

Called when the server is startup.

<a id="player_api.mcdr.utils"></a>

# player\_api.mcdr.utils

<a id="player_api.mcdr.modules.binder"></a>

# player\_api.mcdr.modules.binder

<a id="player_api.mcdr.modules.online"></a>

# player\_api.mcdr.modules.online

<a id="player_api.utils"></a>

# player\_api.utils

Utility functions for PlayerAPI.

<a id="player_api.utils.execute_if"></a>

#### execute\_if

```python
def execute_if(condition: bool | Callable[[], bool])
```

Add a decorator to execute a function only if a condition is met.

Usage: add `@execute_if(bool | Callable -> bool)` line before the function.

**Arguments**:

- `condition` _bool | Callable[[], bool]_ - Condition to check.

<a id="player_api.utils.get_time"></a>

#### get\_time

```python
def get_time(return_str: Optional[bool]) -> datetime | str
```

Get a datetime object or string.

**Arguments**:

- `return_str` _Optional[bool]_ - Return a string result instead of a datetime instance or not.
  

**Returns**:

  datetime | str: Result of the time.

<a id="player_api.utils.get_time_styled"></a>

#### get\_time\_styled

```python
def get_time_styled(locale_code: Optional[str]) -> str
```

Get a readable time result

**Arguments**:

- `locale_code` _Optional[str]_ - Set the locale code if you want to get the result in the specified locale.
  
  Supported locale codes:
  - zh_cn (Chinese)
  
  Unsupported locale codes will fallback to English result.
  

**Returns**:

- `str` - Text time result that is readable.

<a id="player_api.utils.format_time"></a>

#### format\_time

```python
def format_time(time: datetime | str, locale_code: Optional[str]) -> str
```

Format string time or datetime instance to readable text.

**Arguments**:

- `time` _datetime | str_ - String time or datetime instance.
- `locale_code` _Optional[str]_ - See [`get_time_styled()`](#player_api.utils.get_time_styled).
  

**Returns**:

- `str` - Text time result that is readable.

