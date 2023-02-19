# api/util/keyboard/_win32.py
import api.util.log
from ctypes import windll,wintypes

try:
   import PyHook3 as hook
except ModuleNotFoundError:
    api.util.log.critical("Can't find pyHook3 library.OMC request it in windows")
    api.util.log.critical("Building it will request swig.You can install the pre-builted library build by me.(only python3.11)")
    api.util.log.critical("You can find it in api/util/keyboard/PyHook3-1.6.1-cp311-cp311-win_amd64.whl")
    raise SystemExit
    
GetMessage=windll.user32.GetMessageW

def translate_key(key):
    global capslocked
    if key is None:
        key="<unkown>"
    key=key.replace('menu','alt')
    key=key.replace('control','ctrl')
    key=key.replace("Numpad","")
    key=key.replace("Escape","esc")
    key=key.replace("Delete","del")
    key=key.replace("Back","backspace")
    key=key.replace("Capital","CapsLock")
    key=key.replace("Oem_Plus","+")
    key=key.replace("Oem_Minus","-")
    key=key.replace("Oem_Comma",",")
    key=key.replace("Oem_Period",".")
    key=key.replace("Oem_1",";")  # 支支持美国（标准）键盘
    key=key.replace("Oem_2","/")  # 支支持美国（标准）键盘
    key=key.replace("Oem_3","~")  # 支支持美国（标准）键盘
    key=key.replace("Oem_4","[")  # 支支持美国（标准）键盘
    key=key.replace("Oem_5","\\")  # 支支持美国（标准）键盘
    key=key.replace("Oem_6","]")  # 支支持美国（标准）键盘
    key=key.replace("Oem_7","'")  # 支支持美国（标准）键盘
    key=key.replace("Oem_8","<unkown>")  # 支支持美国（标准）键盘
    key=key.replace("Oem_102","<")  # 支支持美国（标准）键盘
    key=key.replace("Multiply","*")
    key=key.replace("Add","+")
    key=key.replace("Divide","/")
    return key.lower()
def call_keyboard_event(evt):
    print(translate_key(evt.Key))
    return True
def call_mouse_event(evt):
    return True
    
def init():
    manger = hook.HookManager()
    manger.KeyDown = call_keyboard_event
    manger.HookKeyboard()
    manger.MouseAll = call_mouse_event
    manger.HookMouse()
    msg = wintypes.MSG()
    GetMessage(msg, 0, 0, 0)