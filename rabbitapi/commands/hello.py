# Copyright 2021 Sidon Duarte
from rabbitapi.build_parser import build_data_queue_args
from typing import List


def hello() -> None:
    print('hello')


def main(args: List[str]) -> None:
    data_args = build_data_queue_args()
    if data_args['separator']:
        separator = f"\n{80 * data_args['separator']}"
    else:
        separator = '\n'
    print(data_args)
