# ===============================
# Singleton using a metaclass.
# ===============================

class SingletonMeta(type):
    """
    Singleton metaclass obj.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonMetaclass(metaclass=SingletonMeta):
    def __init__(self):
        self.log_file = "metaclass.log"

    def log(self, message: str) -> None:
        print(f"[LOG] - {self.log_file}:: {message}\n")