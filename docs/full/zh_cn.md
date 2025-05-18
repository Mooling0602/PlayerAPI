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

**返回**:

- `bool` - True 如果这个 UUID 来自 Floodgate，否则为False。

<a id="player_api.Player"></a>

## Player 对象

```python
@dataclass
class Player()
```

基础的玩家类。

任何继承自这个类的子类都应该有以下的属性（参数）。

**属性**:

- `name` _Optional[str]_ - 玩家名称，用于原版聊天格式和日志、命令等。

- `uuid` _Optional[UUID]_ - 玩家的 UUID。

- `online_mode` _Optional[bool]_ - 这个玩家是否处于在线模式。

- `official_account` _Optional[bool]_ - 这个玩家的账户是否由 Mojang 或 Microsoft 验证。

- `api` _Optional[HttpUrl|str]_ - 登录服务 API 地址。

- `service_name` _Optional[str]_ - 登录服务名称。

**抛出（报错）**:

- `TypeError` - 如果必要参数没有提供。

<a id="player_api.OfflinePlayer"></a>

## OfflinePlayer 对象

```python
@dataclass
class OfflinePlayer(Player)
```

离线玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**属性**:

- `online_mode` _Optional[bool]_ - 强制玩家为离线模式。

  默认为 `False`。

- `official_account` _Optional[bool]_ - 强制（认定）玩家的账户没有被 Mojang 或 Microsoft 验证。

  默认为 `False`。

- `api` _Optional[HttpUrl]_ - 强制登录服务的 API 地址为空。

  默认为 `None`。

- `service_name` _Optional[str]_ - 强制登录服务的名称为 "offline"。

  默认为 "offline"。

<a id="player_api.OnlinePlayer"></a>

## OnlinePlayer 对象

```python
@dataclass
class OnlinePlayer(Player)
```

在线玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**属性**:

- `online_mode` _Optional[bool]_ - 强制玩家为在线模式。

  默认为 `True`。

<a id="player_api.OfficialPlayer"></a>

## OfficialPlayer 对象

```python
@dataclass
class OfficialPlayer(OnlinePlayer)
```

正版（Java 版）玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**属性**:

- `official_account` _Optional[bool]_ - 强制（认定）玩家的账户已经被 Mojang 或 Microsoft 验证。

  默认为 `True`。

- `api` _Optional[HttpUrl|str]_ - 强制使用官方的 API URL。

  默认为 `HttpUrl("https://api.mojang.com/users/profiles/minecraft/")`。

- `service_name` _Optional[str]_ - 强制为 "mojang"。

  默认为 "mojang"。

**抛出（报错）**:

- `TypeError` - 如果检测到一个 Floodgate 玩家的 UUID。

<a id="player_api.YggdrasilPlayer"></a>

## YggdrasilPlayer 对象

```python
@dataclass
class YggdrasilPlayer(OnlinePlayer)
```

Yggdrasil（外置登录）玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**属性**:

- `official_account` _Optional[bool]_ - 强制（认定）玩家的账户没有被 Mojang 或 Microsoft 验证。

  默认为 `False`。

- `service_name` _Optional[str]_ - 强制为 "yggdrasil"。

  默认为 "yggdrasil"。

**抛出（报错）**:

- `TypeError` - 如果没有提供 Yggdrasil API 地址。

<a id="player_api.FloodgatePlayer"></a>

## FloodgatePlayer 对象

```python
@dataclass
class FloodgatePlayer(OnlinePlayer)
```

Floodgate（基岩版Xbox）玩家类。

缺少的属性请查看 [`Player`](#player_api.Player)。

**属性**:

- `official_account` _Optional[bool]_ - 因为无法确认基岩版玩家是否购买了游戏，所以强制（认定）玩家的账户没有被 Mojang 或 Microsoft 验证。
  

**抛出（报错）**:

- `TypeError` - 如果UUID格式不匹配。

<a id="player_api.test"></a>

#### test

```python
def test()
```

测试用模块。

<a id="player_api.mcdr.runtime"></a>

# player\_api.mcdr.runtime

MCDR 插件运行时模块。

<a id="player_api.mcdr.runtime.cfg"></a>

#### cfg

[`PluginConfig`](#player_api.mcdr.config.PluginConfig) 实例

用于存储并提供访问插件配置。

<a id="player_api.mcdr.runtime.psi"></a>

#### psi

[`PluginServerInterface`](https://docs.mcdreforged.com/en/latest/code_references/PluginServerInterface.html) 实例，适用于 MCDR 插件。

用于访问 MCDR 插件服务器接口及其方法。

<a id="player_api.mcdr.config"></a>

# player\_api.mcdr.config

MCDR 插件的配置文件处理模块。

<a id="player_api.mcdr.config.OnlineModules"></a>

## OnlineModules 对象

```python
class OnlineModules(Serializable)
```

插件配置选项：在线模块

**属性**:

- `matcher` _bool_ - 匹配各种玩家信息的功能。

  默认为 `False`（以禁用）。

- `counter` _bool_ - 在线玩家计数器功能。

  默认为 `False`（以禁用）。

- `timer` _bool_ - 在线时长统计功能。

  默认为 `False`（以禁用）。

<a id="player_api.mcdr.config.PluginModules"></a>

## PluginModules 对象

```python
class PluginModules(Serializable)
```

Plugin config options for modules.

**属性**:

- `online` _OnlineModules_ - 是否启用在线相关模块。

- `binder` _bool_ - 自定义玩家 ID 功能。

  默认为 `False`（以禁用）。

- `ip_logger` _bool_ - 记录玩家 IP 功能。

  默认为 `False`（以禁用）。

<a id="player_api.mcdr.config.PluginConfig"></a>

## PluginConfig 对象

```python
class PluginConfig(Serializable)
```

插件配置主类。

配置选项的根节点。

**属性**:

- `enable` _bool_ - 是否启用插件。

  默认为 `False`（以禁用）。

- `modules` _PluginModules_ - 是否启用插件的各个模块。

<a id="player_api.mcdr.config.config_loader"></a>

#### config\_loader

```python
def config_loader(server: PluginServerInterface) -> PluginConfig
```

加载插件的所有配置。

<a id="player_api.mcdr"></a>

# player\_api.mcdr

MCDR 插件入口点。

<a id="player_api.mcdr.on_load"></a>

#### on\_load

```python
def on_load(server: PluginServerInterface, prev_module) -> None
```

在插件被加载时调用。

<a id="player_api.mcdr.on_server_startup"></a>

#### on\_server\_startup

```python
@execute_if(lambda: (rt.cfg.modules.online.counter and rt.cfg.enable) is True)
def on_server_startup(server: PluginServerInterface)
```

在服务器启动完成时调用。

<a id="player_api.mcdr.utils"></a>

# player\_api.mcdr.utils

<a id="player_api.mcdr.utils.tr"></a>

#### tr

```python
def tr(server: PluginServerInterface,
       key: str,
       to_str: Optional[bool] = None,
       **kwargs) -> RTextMCDRTranslation | str
```

根据翻译键翻译出符合服务器语言的文本。

**Arguments**:

- `server` _PluginServerInterface_ - 插件服务器接口实例。
  
- `key` _str_ - 翻译键。
  
- `to_str` _bool, optional_ - 是否将结果转换为字符串。

  默认为 `None`（以不转换）。
  
- `**kwargs` - 用于翻译的额外参数。
  

**返回**:

  RTextMCDRTranslation | str: 翻译后的文本。

<a id="player_api.mcdr.modules.binder"></a>

# player\_api.mcdr.modules.binder

<a id="player_api.mcdr.modules.online"></a>

# player\_api.mcdr.modules.online

<a id="player_api.utils"></a>

# player\_api.utils

PlayerAPI 的工具函数。

<a id="player_api.utils.execute_if"></a>

#### execute\_if

```python
def execute_if(condition: bool | Callable[[], bool])
```

添加一个装饰器，如果条件满足，则执行函数。

**用法**:

在函数前添加 `@execute_if(bool | Callable -> bool)` 行。

**参数**:

- `condition` _bool | Callable[[], bool]_ - 要检查的条件。

<a id="player_api.utils.get_time"></a>

#### get\_time

```python
def get_time(return_str: Optional[bool]) -> datetime | str
```

获取一个 `datetime` 对象或字符串表示时间。

**参数**:

- `return_str` _Optional[bool]_ - 是否返回字符串结果以代替 `datetime` 对象。
  

**返回**:

  datetime | str: 获取到的时间结果。

<a id="player_api.utils.get_time_styled"></a>

#### get\_time\_styled

```python
def get_time_styled(locale_code: Optional[str]) -> str
```

获取一个可读的文本时间结果。

**Arguments**:

- `locale_code` _Optional[str]_ - 设置语言区域代码如果你想获取在特定语言区域下的结果。
  
  支持的语言区域代码:
  - zh_cn (简体中文)
  
  不支持的语言区域代码将回退到英文结果。
  
**返回**:

- `str` - 可读的文本时间结果。

<a id="player_api.utils.format_time"></a>

#### format\_time

```python
def format_time(time: datetime | str, locale_code: Optional[str]) -> str
```

Format string time or datetime instance to readable text.

**参数**:

- `time` _datetime | str_ - 文本时间或 `datetime` 实例。

- `locale_code` _Optional[str]_ - 请查看 [`get_time_styled()`](#player_api.utils.get_time_styled)。
  

**Returns**:

- `str` - 可读的文本时间结果。
