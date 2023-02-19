import api.util


@api.util.singleton
class MixinManger(object):

    def __init__(self):
        self.mixins = {}

    def __call__(self, method):
        if method in self.mixins:
            return self.mixins[method]
        else:
            raise AttributeError(
                'Mixin Manger can\'t found the target class\'s mixin.')

    __getattr__ = __call__


def mixable(target):
    """
    被这个类注释的方法可以被 java 层 Mixin。
    目前没有用处，用于以后实现 Forge/Fabric 兼容。
    用例：
    @mixable("net.minecraft.math.random.Random")
    def random():
        random.randint(1,100)
    这个方法默认情况下返回1到100的随机数，通过java层的mixin可以支持进行其他操作来替换这个操作 
    """

    def wrapper(func):

        def iwrapper(*arg, **kwarg):
            try:
                return MixinManger()(target)(*arg, **kwarg)
            except AttributeError:
                return func(*arg, **kwarg)

        return iwrapper

    return wrapper
