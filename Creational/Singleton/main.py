from singleton_base import SingletonBaseclass
from singleton_decorator import SingletonDecorator
from singleton_metaclass import SingletonMetaclass

SUCCESS_MSG = "Singleton works, both variables contain the same instance."
FAILED_MSG = "Singleton failed, variables contain different instances."

if __name__ == "__main__":
    # Singleton Base
    s1_base = SingletonBaseclass()
    s2_base = SingletonBaseclass()

    if s1_base is s2_base:
        s1_base.log(SUCCESS_MSG)
        s2_base.log(SUCCESS_MSG)
    else:
        print(FAILED_MSG)

    # Singleton Decorator
    s1_decorator = SingletonDecorator()
    s2_decorator = SingletonDecorator()

    if s1_decorator is s2_decorator:
        s1_decorator.log(SUCCESS_MSG)
        s2_decorator.log(SUCCESS_MSG)
    else:
        print(FAILED_MSG)

    # Singleton Metaclass
    s1_metaclass = SingletonMetaclass()
    s2_metaclass= SingletonMetaclass()

    if s1_metaclass is s2_metaclass:
        s1_metaclass.log(SUCCESS_MSG)
        s2_metaclass.log(SUCCESS_MSG)
    else:
        print(FAILED_MSG)