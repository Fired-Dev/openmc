import core.render


class ItemConfig():
    pass


class ItemBase(object):

    def __init__(self, config: ItemConfig):
        self.config = config

    def onuse(self):
        pass

    def canbreak(self, block):
        pass

    def render(self) -> render.SimpleTexture:
        pass
