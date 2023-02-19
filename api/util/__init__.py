import dataclasses

import api.util.log as log


def singleton(cls):
    _instance = None

    def wrapper():
        nonlocal _instance
        if _instance is None:
            _instance = cls()
        return _instance

    return wrapper


def get_subclass(cls):
    return cls.__subclasses__()


def check_engine(func):

    def wrapper(self, *arg, **kwarg):
        if self._engine is None:
            raise api.error.RenderEngineNotInited
        return func(self, *arg, **kwarg)

    return wrapper


def stage(name):

    def deco(func):

        def wrapper(*arg, **kwarg):
            log.info("Entered stage " + name)
            func(*arg, **kwarg)
            log.info("Stage " + name + " Finash")

        return wrapper

    return deco


@dataclasses.dataclass
class Pos(object):
    x: float
    b: float
    z: float
