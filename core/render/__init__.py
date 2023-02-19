import core.render.ursina as _engine

engine = _engine.Engine()  # 目前硬编码为这个引擎,未来有概率（aka 1/inf）实现其他引擎


def set_engine(eng):
    global engine
    engine = eng


def get_engine():
    return engine


class BasicTexture:
    pass
