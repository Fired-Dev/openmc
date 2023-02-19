import api.commandbasebase
import api.util
import api.error
import api.cache


def find_command(key, root=None):
    if isinstance(key, str):
        key = key.split()
    if key == []:
        if root is None:
            raise api.error.CommandError("unkown error")
        else:
            return root
    try:
        return api.cache.cachedb["command"][key]
    except KeyError:
        pass

    rkey = key.split()
    if root is None:
        for i in api.util.get_subclass(api.commandbase.CommandBase):
            if i.__name__ == key[0]:
                api.cache.cachedb["command"][key] = find_command(key[1:], i)
                return api.cache.cachedb["command"][key]
        raise api.error.CommandNotFoundError(' '.join(key))
    try:
        api.cache.cachedb["command"][key] = find_command(
            key[1:], getattr(root, key[0]))
        return api.cache.cachedb["command"][key]
    except AttributeError:
        raise api.error.CommandNotFoundError(' '.join(key))


class Command(api.commandbase.CommandBase):
    """允许通过指令管理指令引擎"""

    @staticmethod
    def reflush():
        api.cache.cachedb["command"].clear()
        return "成功刷新了引擎缓存"
