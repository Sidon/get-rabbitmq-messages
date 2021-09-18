#!/usr/bin/env python3
# Copyleft 2021 Sidon Duarte
#
import http
import sys
from typing import Any

import colorama
import requests

from rabbitgetapi import cli
from rabbitgetapi import exceptions
from rabbitgetapi import build_parser


def main() -> Any:
    try:
        result = cli.dispatch(sys.argv[1:])
    except requests.HTTPError as exc:
        status_code = exc.response.status_code
        status_phrase = http.HTTPStatus(status_code).phrase
        result = (
            f"{exc.__class__.__name__}: {status_code} {status_phrase} "
            f"from {exc.response.url}\n"
            f"{exc.response.reason}"
        )
    except exceptions.GetRmqApiException as exc:
        result = f"{exc.__class__.__name__}: {exc.args[0]}"
    return _format_error(result) if isinstance(result, str) else result


def _format_error(message: str) -> str:
    pre_style, post_style = "", ""
    if not cli.args.no_color:
        colorama.init()
        pre_style, post_style = colorama.Fore.RED, colorama.Style.RESET_ALL

    return f"{pre_style}{message}{post_style}"


if __name__ == "__main__":
    sys.exit(main())
