"""player_api.mcdr.runtime

Runtime module for MCDR plugin workaround.
"""
from mcdreforged.api.types import PluginServerInterface
from .config import PluginConfig


cfg: PluginConfig = None  # type: ignore
"""PluginConfig instance.

This is used to access the plugin configuration.
"""
psi: PluginServerInterface = None  # type: ignore
"""PluginServerInterface instance for MCDR plugin.

This is used to access the psi instance and its methods.
"""
