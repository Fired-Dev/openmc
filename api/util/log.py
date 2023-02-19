# TODO: 改进对Logging的支持(e.g.彩色)
try:
    from loguru import logger
except ModuleNotFoundError:
    try:
        from zdppy_log import Log
        logger = Log()
    except ModuleNotFoundError:
        print('警告：找不到受支持的日志框架（loguru/zdppy_log），这意味着一些先进的功能将无法实现，我强烈建议你安装一个。')
        import logging
        loggeer = logging.Logger()
debug = logger.debug
info = logger.info
warn = logger.warning
error = logger.error
critical = logger.critical
