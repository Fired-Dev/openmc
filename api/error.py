class OMCError(Exception):
    pass


class InitError(OMCError):
    pass


class ClientError(OMCError):
    pass


class ServerError(OMCError):
    pass


class CommandError(ClientError):
    pass


class CommandNotFoundError(CommandError):
    pass


class RenderError(ClientError):
    pass


class RenderEngineNotInited(RenderError):
    pass


class I18NError(ClientError):
    pass


class I18NEngineNotLoadedError(I18NError):
    pass
