import api.util.log

try:
    from http3 import *
except ModuleNotFoundError:
    try:
        from httpx import *
    except ModuleNotFoundError:
        api.util.log.critical(
            "No support network library find.Note that we doesn't support requests.We only support HTTP3/HTTPX"
        )
        raise RuntimeException
