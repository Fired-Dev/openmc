# 这个文件会自动让一些数学相关的方法可以被mixin，并提供一些实用方法
import math
import builtins
import secrets

from api.util.mixin import mixable


def _mix_math(target, name, key="math"):
    key = globals()[key]
    setattr(key, name, mixable(target)(getattr(key, name)))


_mix_math("java.lang.Math.abs", "abs", "builtins")
_mix_math("java.lang.Math.max", "max", "builtins")
_mix_math("java.lang.Math.min", "min", "builtins")
_mix_math("java.lang.Math.ceil", "ceil")
_mix_math("java.lang.Math.floor", "floor")
_mix_math("java.lang.Math.sin", "sin")
_mix_math("java.lang.Math.cos", "cos")
_mix_math("java.lang.Math.tan", "tan")
_mix_math("java.lang.Math.exp", "exp")
_mix_math("java.lang.Math.pow", "pow")
_mix_math("java.lang.Math.sqrt", "sqrt")
_mix_math("java.lang.Math.log", "log")
_mix_math("java.lang.Math.toDegrees", "degrees")
_mix_math("java.lang.Math.toRadians", "radians")
_mix_math("java.lang.Math.asin", "asin")
_mix_math("java.lang.Math.acos", "acos")
_mix_math("java.lang.Math.atan", "atan")
_mix_math("java.lang.Math.round", "round", "builtins")


def randint(a, b):
    return a + secrets.randbelow(b - a + 1)


secrets.randint = randint
