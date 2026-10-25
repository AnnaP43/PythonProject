from datetime import datetime
from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time_now = datetime.now()

            try:
                result = func(*args, **kwargs)
                lod_message = f"{time_now} - {func.__name__} ok\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(lod_message)
                else:
                    print(lod_message, end="")

                return result

            except Exception as e:
                error_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="")

                raise
        return wrapper
    return decorator