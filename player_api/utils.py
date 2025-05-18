"""Utility functions for PlayerAPI.
"""
import locale

from typing import Any, Callable, Optional
from datetime import datetime, timezone


def execute_if(condition: bool | Callable[[], bool]):
    """Add a decorator to execute a function only if a condition is met.

    Usage:
        add `@execute_if(bool | Callable -> bool)` line before the function.

    Args:
        condition (bool | Callable[[], bool]): Condition to check.
    """
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            actual_condition = None
            if callable(condition):
                actual_condition = condition()
            else:
                actual_condition = condition
            if actual_condition:
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator


def get_time(return_str: Optional[bool]) -> datetime | str:
    """Get a datetime object or string.

    Args:
        return_str (Optional[bool]): \
Return a string result instead of a datetime instance or not.

    Returns:
        datetime | str: Result of the time.
    """
    if not return_str:
        return datetime.now(timezone.utc)
    else:
        return datetime.now(timezone.utc).isoformat()


def get_time_styled(locale_code: Optional[str]) -> str:
    """Get a readable time result

    Args:
        locale_code (Optional[str]): Set the locale code \
if you want to get the result in the specified locale.

            Supported locale codes:
                - zh_cn (Chinese)

            Unsupported locale codes will fallback to English result.

    Returns:
        str: Text time result that is readable.
    """
    style = r"%Y-%m-%d %H:%M:%S %A"
    if locale_code == "zh_cn":
        locale.setlocale(locale.LC_TIME, 'zh_CN.UTF-8')
        style = r"%Y年%m月%d日 %H:%M:%S %A"
    return datetime.now().astimezone().strftime(style)


def format_time(time: datetime | str, locale_code: Optional[str]) -> str:
    """Format string time or datetime instance to readable text.

    Args:
        time (datetime | str): String time or datetime instance.

        locale_code (Optional[str]): See [`get_time_styled()`]\
(#player_api.utils.get_time_styled).

    Returns:
        str: Text time result that is readable.
    """
    style = r"%Y-%m-%d %H:%M:%S %A"
    if locale_code == "zh_cn":
        locale.setlocale(locale.LC_TIME, 'zh_CN.UTF-8')
        style = r"%Y年%m月%d日 %H:%M:%S %A"
    if not isinstance(time, datetime):
        time = datetime.fromisoformat(time)
    return time.astimezone().strftime(style)
