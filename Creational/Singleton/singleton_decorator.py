# ===============================
# Singleton using a decorator.
# ===============================


def singleton(cls):
    """
    Singleton decorator.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class SingletonDecorator:
    def __init__(self):
        self.log_file = "decorator.log"

    def log(self, message):
       print(f"[LOG] - {self.log_file}:: {message}\n")