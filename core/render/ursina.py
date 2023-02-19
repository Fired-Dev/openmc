import ursina
from multidispatch import dispatch

import api.error
import api.util


@dispatch
def transform_pos(pos: api.util.Pos):
    return api.util.Pos(pos.x, pos.z, pos.y)


@dispatch
def transform_pos(x: int, y: int, z: int):
    return (x, y, z)


@dispatch
def transform_pos(x: float, y: float, z: float):
    return (x, y, z)


@dispatch
def transform_pos(pos: float):
    return (pos[0], pos[2], pos[1])


class RenderWorld(ursina.Entity):
    pass


class RenderBlock(ursina.Button):

    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        if isinstance(position, api.util.Pos):
            position = (position.x, position.y, position.y)
        super().__init__(parent=ursina.scene,
                         position=position,
                         model="cube",
                         highlight_color=ursina.color.lime,
                         color=cursina.color.white,
                         texture=texture,
                         origin_y=0.5)


class Sky(Entity):

    def __init__(self):
        super().__init__(parent=ursina.scene,
                         model="sphere",
                         scale=1500,
                         texture=api.texture.get_texture('core', "sky"),
                         double_sided=True,
                         position=(0, 0, 0))


class Engine():

    def __init__(self):
        self._engine = None
        self.world = None

    def init(self):
        self._engine = ursina.Ursina()
        self.world = RenderWorld()
        self.run()  # 现在立即启动引擎，未来可能进行修改

    @api.util.check_engine
    def run(self):
        self._engine.run()
