# 智能选择可用的Python TOML库，无任何可用实现时报错
import api.util.log as logger


def _apply_engine(eng):
    global load, loads, dump, dumps
    load = eng.load
    loads = eng.loads
    dump = eng.dump
    dumps = eng.dumps


def _auto_select():
    global load, loads, dump, dumps
    try:  # Tomli&Tomliw installed/Python3.11+&Tomli installed.
        try:  # Auto Check Is Python3.11+/Tomli.
            import tomllib
        except ModuleNotFoundErrror:
            try:
                import tomli as tomllib
            except ModuleNotFoundError as exc:
                raise exc
        try:
            import tomli_w
        except ModuleNotFoundError as exc:
            logger.warning("找到了tomli/tomllib但是没有找到tomliw，已临时忽略tomli/tomllib库。")
            raise exc

        load = tomllib.load
        loads = tomllib.loads
        dump = tomli_w.dump
        dumps = tomli_w.dumps
        return
    except ModuleNotFoundError:
        pass
    try:  # RToml Installed.
        import rtoml
        _apply_engine(rtoml)
        return
    except ModuleNotFoundError:
        pass
    try:  # PyTomlPP Installed.
        import pytomlpp
        _apply_engine(pytomlpp)
        return
    except ModuleNotFoundError:
        pass
    try:  # TomlKit Installed.
        import tomlkit
        _apply_engine(tomlkit)
        return
    except ModuleNotFoundError:
        pass
    logger.warning(
        "未检测到符合TOML1.0标准的TOML库(支持tomli+tomliw/rtoml/pytomlpp/tomlkit)，正在查找符合TOML0.5标准的TOML库，这可能导致未知的问题。"
    )
    try:  # QToml
        import qtoml
        _apply_engine(qtoml)
        return
    except ModuleNotFoundError:
        pass
    try:  # Toml
        import toml
        _apply_engine(toml)
    except ModuleNotFoundError:
        pass
    logger.critical(
        "未检测到符合TOML1.0(兼容列表见上)/TOML0.5(toml/qtoml)标准的TOML库，OpenMinecraft不可能在这种情况下继续运行，正在退出"
    )
    raise SystemExit


_auto_select()
