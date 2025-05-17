"""Runtime module for MCDR plugin workaround.
"""
from mcdreforged.api.types import PluginServerInterface
from .config import PluginConfig


cfg: PluginConfig = None  # type: ignore
"""[`PluginConfig`](#player_api.mcdr.config.PluginConfig) global instance.

This is used to store the plugin configuration and provide the access of it.
"""
psi: PluginServerInterface = None  # type: ignore
"""[`PluginServerInterface`]\
(https://docs.mcdreforged.com/en/latest/code_references/PluginServerInterface.html)\
 instance for MCDR plugin.

This is used to access the mcdr plugin server interface and its methods.
"""
