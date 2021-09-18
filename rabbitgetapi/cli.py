# Copyleft 2021 Sidon Duarte

import argparse
from typing import Any, List, Tuple

from importlib_metadata import entry_points
from importlib_metadata import version

import rabbitgetapi

args = argparse.Namespace()


def list_dependencies_and_versions() -> List[Tuple[str, str]]:
    deps = (
        "importlib_metadata",
        "requests",
    )
    return [(dep, version(dep)) for dep in deps]  # type: ignore[no-untyped-call] # python/importlib_metadata#288  # noqa: E501


def dep_versions() -> str:
    return ", ".join(
        "{}: {}".format(*dependency) for dependency in list_dependencies_and_versions()
    )


def dispatch(argv: List[str]) -> Any:
    registered_commands = entry_points(group="rabbitgetapi.registered_commands")
    parser = argparse.ArgumentParser(prog="rabbitgetapi")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s version {} ({})".format(rabbitgetapi.__version__, dep_versions()),
    )
    parser.add_argument(
        "--no-color",
        default=False,
        required=False,
        action="store_true",
        help="disable colored output",
    )
    parser.add_argument(
        "command",
        choices=registered_commands.names,
    )
    parser.add_argument(
        "args",
        help=argparse.SUPPRESS,
        nargs=argparse.REMAINDER,
    )

    parser.parse_args(argv, namespace=args)

    main = registered_commands[args.command].load()

    return main(args.args)
