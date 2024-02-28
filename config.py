import logging
import typing
import os

log = logging.getLogger("Config")

__debug = False


def debug() -> bool:
    return __debug


def set_debug(value: bool) -> None:
    global __debug
    __debug = value
    log.info(f"Debug mode is {'on' if __debug else 'off'}.")


def open_ai_key() -> typing.Optional[str]:
    """OpenAI key"""
    value = os.environ.get("OPENAI_API_KEY")

    if value:
        return value

    raise EnvironmentError("Required environment variable OPENAI_API_KEY is not set.")
