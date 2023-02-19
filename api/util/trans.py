# 调用顺序：core/init/mergelang.py/merge_lang(合并各个mod的语言文件并编译)->api/util/trans/load_engine(加载引擎)->translate

import gettext
import builtins

import api.error

engine = None


def translate(key):
    if engine is None:
        raise api.error.I18NEngineNotLoadedError
    return engine.gettext(key)


def load_engine(accept_lang=["zh_cn"]):
    global engine
    engine = gettext.find("xlang", "./cache/resources/",
                          accept_lang + ["en_us"])


builtins.trans = translate
