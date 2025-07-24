import asyncio
from functools import wraps

def simple_logger(func):
        if asyncio.iscoroutinefunction(func):
            @wraps(func)
            async def async_wrapper(self, *args, **kwargs):
                self.logger.debug(f'Запускаем функцию {func.__name__}()')
                try:
                    return await func(self, *args, **kwargs)
                except Exception as e:
                    self.logger.exception(f"Ошибка в {func.__name__}():\n {e}")
                    raise
            return async_wrapper
        else:
            @wraps(func)
            def sync_wrapper(self, *args, **kwargs):
                self.logger.debug(f'Запускаем функцию {func.__name__}()')
                try:
                    return func(self, *args, **kwargs)
                except Exception as e:
                    self.logger.exception(f"Ошибка в {func.__name__}():\n {e}")
                    raise
            return sync_wrapper