import locale

from typing import Any, Callable, Optional
from datetime import datetime, timezone


# Usage: @execute_if(bool | Callable -> bool)
def execute_if(condition: bool | Callable[[], bool]):
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
    if not return_str:
        return datetime.now(timezone.utc)
    else:
        return datetime.now(timezone.utc).isoformat()


def get_time_styled(locale: Optional[str]) -> str:
    format = r"%Y-%m-%d %H:%M:%S %A"
    if locale == "zh_cn":
        locale.setlocale(locale.LC_TIME, 'zh_CN.UTF-8')
        format = r"%Y年%m月%d日 %H:%M:%S %A"
    return datetime.now().astimezone().strftime(format)


def format_time(time: datetime | str, locale: Optional[str]) -> str:
    format = r"%Y-%m-%d %H:%M:%S %A"
    if locale == "zh_cn":
        locale.setlocale(locale.LC_TIME, 'zh_CN.UTF-8')
        format = r"%Y年%m月%d日 %H:%M:%S %A"
    if not isinstance(time, datetime):
        time = datetime.fromisoformat(time)
    return time.astimezone().strftime(format)
