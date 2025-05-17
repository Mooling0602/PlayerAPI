"""MCDR plugin entrypoint.
"""
from mcdreforged.api.all import PluginServerInterface
from player_api.utils import execute_if
from player_api.mcdr.config import config_loader

import player_api.mcdr.runtime as rt


def on_load(server: PluginServerInterface, prev_module):
    """Called when the plugin is loaded.
    """
    prev_module = None if not prev_module else prev_module
    rt.psi = server if not rt.psi else rt.psi
    server.logger.info("PlayerAPI is loading with MCDR API.")
    rt.cfg = config_loader(server)


# MCDR Default Listener
@execute_if(lambda: rt.cfg.modules.online.counter is True)
def on_server_startup(server: PluginServerInterface):
    """Called when the server is startup.
    """
    server.logger.info("[Counter] 在线玩家计数器开始初始化...")
    server.logger.warning("警告：开发未完成！")
