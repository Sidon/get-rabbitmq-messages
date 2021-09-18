"""Module containing logic for handling settings."""
# Copyleft 2021 Sidon Duarte

import argparse
import contextlib
import logging
import sys
from typing import Any, ContextManager, Optional, cast

from rabbitgetapi import exceptions


class Settings:
    @staticmethod
    def register_argparse_arguments(__arg_parser: argparse.ArgumentParser) -> None:
        __arg_parser.add_argument(
            '-f',
            '--configfile',
            action='store',
            help='Configuration file (full or relative path)',
        )
        __arg_parser.add_argument(
            '--url',
            action='store',
            default='http://127.0.0.1:15672',
            help='RabbitMQ server url without slash, default = http://127.0.0.1:15672.',
        )
        __arg_parser.add_argument(
            '-v',
            '--vhost',
            action='store',
            default='%2F',
            help="RabbitMQ virtual server, default = '/'."
        )
        __arg_parser.add_argument(
            '--user',
            '-u',
            action='store',
            default='guest',
            help='RabbitMQ user, default = guest.',
        )
        __arg_parser.add_argument(
            '--password',
            '-p',
            action='store',
            default='guest',
            help='RabbitMQ password, default = guest.',
        )
        __arg_parser.add_argument(
            '--outputfile',
            '-o',
            action='store',
            default='./messages',
            help='file for output messages.',
        )
        __arg_parser.add_argument(
            '--separator',
            '-s',
            action='store',
            default=None,
            help='Character for line separator.',
        )
        __arg_parser.add_argument(
            '--mode',
            '-m',
            action='store',
            default='full',
            help='full = whole message, payload = just payload',
        )

    # @classmethod
    # def from_argparse(cls, args: argparse.Namespace) -> "Settings":
    #     """Generate the Settings from parsed arguments."""
    #     settings = vars(args)
    #     return cls(**settings)

