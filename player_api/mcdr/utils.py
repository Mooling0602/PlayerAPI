"""Utility functions for MCDR plugin development.
"""
from typing import Optional
from mcdreforged.api.all import PluginServerInterface, RTextMCDRTranslation


def tr(
    server: PluginServerInterface, key: str,
    to_str: Optional[bool] = None, **kwargs
) -> RTextMCDRTranslation | str:  # type: ignore
    """Translate the key to the language of the server.

    Args:
        server (PluginServerInterface): The server instance.

        key (str): The key to translate.

        to_str (bool, optional): Whether to convert the result to string.

            Default to `None` (to disable).

        **kwargs: Additional arguments for translation.

    Returns:
        RTextMCDRTranslation | str: The translated text.
    """
    plugin_id = server.get_self_metadata().id
    if not key.startswith("#"):
        result = server.rtr(plugin_id + "." + key, **kwargs)
    else:
        result = server.rtr(key[1:], **kwargs)
    if to_str:
        if to_str is True:
            result = str(result)
    return result
