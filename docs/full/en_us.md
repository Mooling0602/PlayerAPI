# Table of Contents

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
  * [config\_loader](#player_api.mcdr.config.config_loader)
* [player\_api.mcdr](#player_api.mcdr)
  * [on\_load](#player_api.mcdr.on_load)
  * [on\_server\_startup](#player_api.mcdr.on_server_startup)
* [player\_api.mcdr.utils](#player_api.mcdr.utils)
  * [tr](#player_api.mcdr.utils.tr)
* [player\_api.mcdr.modules.binder](#player_api.mcdr.modules.binder)
* [player\_api.mcdr.modules.online](#player_api.mcdr.modules.online)
* [player\_api.utils](#player_api.utils)
  * [execute\_if](#player_api.utils.execute_if)
  * [get\_time](#player_api.utils.get_time)
  * [get\_time\_styled](#player_api.utils.get_time_styled)
  * [format\_time](#player_api.utils.format_time)

<a id="player_api"></a>

# player\_api

PlayerAPI - A Python lib and a MCDReforged plugin for querying and managing Minecraft player information.

<a id="player_api.ServiceType"></a>

## ServiceType Objects

```python
class ServiceType(StrEnum)
```

The type of service.

<a id="player_api.is_from_floodgate"></a>

#### is\_from\_floodgate

```python
def is_from_floodgate(uuid: Optional[UUID]) -> bool
```

Check if the UUID is from Floodgate.

Floodgate player's UUID is prefixed with "00000000", so we can check if it is.

**Arguments**:

  
- `uuid` _Optional[UUID]_ - The UUID to check.
  

**Returns**:

  
- `bool` - `True` if the UUID is from Floodgate, `False` otherwise.

<a id="player_api.Player"></a>

## Player Objects

```python
@dataclass
class Player()
```

Basic player class.

Any subclass based on this class should have the following attributes.

**Arguments**:

- `name` _Optional[str]_ - Player name, used in vanilla chat format and logs, commands, etc.
  
- `uuid` _Optional[UUID]_ - UUID of the player.
  
- `online_mode` _Optional[bool]_ - Whether the player is in online mode or not.
  
- `official_account` _Optional[bool]_ - Whether the player's account has been verified by Mojang/Microsoft.
  
- `api` _Optional[HttpUrl|str]_ - Login service API address.
  
- `service_name` _Optional[str]_ - Login service name.
  

**Raises**:

- `TypeError` - If no necessary arguments are provided.

<a id="player_api.OfflinePlayer"></a>

## OfflinePlayer Objects

```python
@dataclass
class OfflinePlayer(Player)
```

Offline player class.

Missing attributes see class [`Player`](#player_api.Player).

**Arguments**:

- `online_mode` _Optional[bool]_ - Force the player to be offline mode.
  
  Defaults to `False`.
  
- `official_account` _Optional[bool]_ - Force the player's account hasn't been verified by Mojang/Microsoft.
  
  Defaults to `False`.
  
- `api` _Optional[HttpUrl]_ - Force the login service's api address to be empty.
  
  Defaults to `None`.
  
- `service_name` _Optional[str]_ - Force the login service's name to be "offline".
  
  Defaults to "offline".

<a id="player_api.OnlinePlayer"></a>

## OnlinePlayer Objects

```python
@dataclass
class OnlinePlayer(Player)
```

Online player class.

Missing attributes see class [`Player`](#player_api.Player).

**Arguments**:

- `online_mode` _Optional[bool]_ - Force the player is in online mode.
  
  Defaults to `True`.

<a id="player_api.OfficialPlayer"></a>

## OfficialPlayer Objects

```python
@dataclass
class OfficialPlayer(OnlinePlayer)
```

Official player class.

Missing attributes see class [`Player`](#player_api.Player).

**Arguments**:

- `official_account` _Optional[bool]_ - Force the player's account has been verified by Mojang/Microsoft.
  
  Defaults to `True`.
  
- `api` _Optional[HttpUrl|str]_ - Force to use the official API URL.
  
  Defaults to `HttpUrl("https://api.mojang.com/users/profiles/minecraft/")`.
  
- `service_name` _Optional[str]_ - Force to be "mojang".
  
  Defaults to "mojang".
  

**Raises**:

- `TypeError` - If a floodgate player's UUID detected.

<a id="player_api.YggdrasilPlayer"></a>

## YggdrasilPlayer Objects

```python
@dataclass
class YggdrasilPlayer(OnlinePlayer)
```

Yggdrasil player class.

Missing attributes see class [`Player`](#player_api.Player).

**Arguments**:

- `official_account` _Optional[bool]_ - Force the player's account hasn't been verified by Mojang/Microsoft.
  
  Defaults to `False`.
  
- `service_name` _Optional[str]_ - Force to be "yggdrasil".
  
  Defaults to "yggdrasil".
  

**Raises**:

- `TypeError` - If not provided yggdrasil api address.

<a id="player_api.FloodgatePlayer"></a>

## FloodgatePlayer Objects

```python
@dataclass
class FloodgatePlayer(OnlinePlayer)
```

Floodgate player class.

Missing attributes see class [`Player`](#player_api.Player).

**Arguments**:

- `official_account` _Optional[bool]_ - Because unable to check if a bedrock player has bought the game,             so force the player's account hasn't been verified                 by Mojang/Microsoft.
  
  Defaults to `False`.
  

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

[`PluginConfig`](#player_api.mcdr.config.PluginConfig) global instance.

This is used to store the plugin configuration and provide the access of it.

<a id="player_api.mcdr.runtime.psi"></a>

#### psi

[`PluginServerInterface`](https://docs.mcdreforged.com/en/latest/code_references/PluginServerInterface.html) instance for MCDR plugin.

This is used to access the mcdr plugin server interface and its methods.

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
  
  Default to `False` (to disable).
  
- `counter` _bool_ - Online player count feature.
  
  Default to `False` (to disable).
  
- `timer` _bool_ - Online time statistics feature.
  
  Default to `False` (to disable).

<a id="player_api.mcdr.config.PluginModules"></a>

## PluginModules Objects

```python
class PluginModules(Serializable)
```

Plugin config options for modules.

**Arguments**:

  
- `online` _OnlineModules_ - Whether to enable online modules.
  
- `binder` _bool_ - Custom player ID feature.
  
  Default to `False` (to disable).
  
- `ip_logger` _bool_ - Player IP logging feature.
  
  Default to `False` (to disable).

<a id="player_api.mcdr.config.PluginConfig"></a>

## PluginConfig Objects

```python
class PluginConfig(Serializable)
```

Plugin configuration main class.

Root nodes of the config options.

**Arguments**:

- `enable` _bool_ - Whether the plugin is enabled.
  
  Default to `False` (to disable).
  
- `modules` _PluginModules_ - Whether the modules to be loaded.

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
def on_load(server: PluginServerInterface, prev_module)
```

Called when the plugin is loaded.

<a id="player_api.mcdr.on_server_startup"></a>

#### on\_server\_startup

```python
@execute_if(lambda: (rt.cfg.modules.online.counter and rt.cfg.enable) is True)
def on_server_startup(server: PluginServerInterface)
```

Called when the server is startup.

<a id="player_api.mcdr.utils"></a>

# player\_api.mcdr.utils

Utility functions for MCDR plugin development.

<a id="player_api.mcdr.utils.tr"></a>

#### tr

```python
def tr(server: PluginServerInterface,
       key: str,
       to_str: Optional[bool] = None,
       **kwargs) -> RTextMCDRTranslation | str
```

Translate the key to the language of the server.

**Arguments**:

- `server` _PluginServerInterface_ - The server instance.
  
- `key` _str_ - The key to translate.
  
- `to_str` _bool, optional_ - Whether to convert the result to string.
  
  Default to `None` (to disable).
  
- `**kwargs` - Additional arguments for translation.
  

**Returns**:

  RTextMCDRTranslation | str: The translated text.

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

Usage:
add `@execute_if(bool | Callable -> bool)` line before the function.

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

