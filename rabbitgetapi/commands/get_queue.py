# Copyleft 2021 Sidon Duarte
import argparse
from typing import List
import requests
import pprint
from rabbitgetapi.build_parser import build_data_queue_args
from rabbitgetapi import settings


def save_messages(url, headers, data, auth, output_file, mode, message_separator):
    response = requests.post(url, headers=headers, data=data, auth=auth)
    if response.status_code == 200:
        with open(output_file, 'w') as file_handler:
            for msg in response.json():
                message = msg if mode == 'full' else msg['payload']
                output_message = f"\n{pprint.pformat(message, indent=4)}"
                file_handler.write(output_message)
                file_handler.write(message_separator)
    else:
        print(response)


def main(args: List[str]) -> None:
    parser = argparse.ArgumentParser(prog='rabbitgetapi getqueue')
    settings.Settings.register_argparse_arguments(parser)

    parser.add_argument(
        '-q',
        '--queue',
        action='store',
        help='The queue from where the messages will be obtained.'
    )
    parser.add_argument(
        '-c',
        '--count',
        action='store',
        type=int,
        default=10,
        help='controls the maximum number of messages to get. Default=10.'
    )

    parsed_args = parser.parse_args(args)
    data_args = build_data_queue_args(parser, parsed_args)

    if data_args['separator']:
        separator = f"\n{80 * data_args['separator']}"
    else:
        separator = '\n'

    save_messages(
        data_args['url'],
        data_args['headers'],
        data_args['payload_data'],
        data_args['auth'],
        data_args['outputfile'],
        data_args['mode'],
        separator
    )
