from mcdreforged.api.all import *
from ..utils import execute_if
from .config import PluginConfig, config_loader

psi: PluginServerInterface = None
cfg: PluginConfig = None


# MCDR Plugin Entry
def on_load(server: PluginServerInterface, prev_module):
    global psi, cfg
    psi = server if not psi else psi
    server.logger.info("PlayerAPI is loading with MCDR API.")
    cfg = config_loader()


# MCDR Default Listener
@execute_if(lambda: cfg.modules.online.counter is True)
def on_server_startup(server: PluginServerInterface):
    server.logger.info("[Counter] 在线玩家计数器开始初始化...")
    server.logger.warning("警告：开发未完成！")
