from mcdreforged.api.utils import Serializable
from mcdreforged.api.types import PluginServerInterface


class OnlineModules(Serializable):
    matcher: bool = False # 匹配各种玩家信息
    counter: bool = False # 在线人数获取
    timer: bool = False # 在线时间统计

class PluginModules(Serializable):
    online: OnlineModules = OnlineModules() # 在线相关功能模块
    binder: bool = False # 自定义玩家身份ID功能
    ip_logger: bool = False # 玩家IP记录功能

class PluginConfig(Serializable):
    enable: bool = False # 默认禁用全部模块
    modules: PluginModules = PluginModules()

def config_loader(server: PluginServerInterface) -> PluginConfig:
    config: PluginConfig = server.load_config_simple(target_class=PluginConfig())
    return config