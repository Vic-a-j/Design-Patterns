# ===============================
# Singleton using a base class.
# ===============================

class SingletonBase:
    """
    Singleton base obj.
    """

    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = object.__new__(cls)
        return cls._instances[cls]


class SingletonBaseclass(SingletonBase):
    def __init__(self):
        self.log_file = "base_class.log"

    def log(self, message: str) -> None:
        print(f"[LOG] - {self.log_file}:: {message}\n")