"""player_api.mcdr.config

Config module for MCDR plugin workaround.
"""
from mcdreforged.api.utils import Serializable
from mcdreforged.api.types import PluginServerInterface


class OnlineModules(Serializable):
    """Plugin config options for online modules.

    Args:
        matcher (bool): Matching various player information feature.
            Default to False (to disable).
        counter (bool): Online player count feature.
            Default to False (to disable).
        timer (bool): Online time statistics feature.
            Default to False (to disable).
    """
    matcher: bool = False  # 匹配各种玩家信息
    counter: bool = False  # 在线人数获取
    timer: bool = False  # 在线时间统计


class PluginModules(Serializable):
    """Plugin config options for modules.

    Args:
        online (OnlineModules): Whether to enable online modules.
        binder (bool): Custom player ID feature.
            Default to False (to disable).
        ip_logger (bool): Player IP logging feature.
            Default to False (to disable).
    """
    online: OnlineModules = OnlineModules()
    binder: bool = False
    ip_logger: bool = False


class PluginConfig(Serializable):
    """Plugin configuration main class.

    Root nodes of the config options.

    Args:
        enable (bool): Whether the plugin is enabled.
        modules (PluginModules): Whether the modules to be loaded.
    """
    enable: bool = False  # * Disable the plugin by default.
    modules: PluginModules = PluginModules()


def config_loader(server: PluginServerInterface) -> PluginConfig:
    """Load the plugin's configuration.
    """
    # ? idk how to solve the error IDE raises, so just ignore it.
    config: PluginConfig = server.load_config_simple(
        target_class=PluginConfig())  # type: ignore
    return config
