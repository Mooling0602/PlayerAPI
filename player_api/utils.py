from typing import Callable, Any


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
