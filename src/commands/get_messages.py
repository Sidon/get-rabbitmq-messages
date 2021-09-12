#!/usr/bin/python
import argparse
import csv
import json
import pprint
import requests
import yaml


# def get_messages(url, headers, payload_data, auth):
#     response = requests.post(url, headers=headers, data=payload_data, auth=auth)
#     separator = '\n'
#     if config_data['separator']:
#         separator = f"\n{80 * config_data['separator']}"
#
#     with open(config_data['outputfile'], 'w') as file_handler:
#         for msg in response.json():
#             message = msg if mode=='full' else msg['payload']
#             output_message = f"\n{pprint.pformat(message, indent=4)}"
#             file_handler.write(output_message)
#             file_handler.write(separator)


def _get_messages(url, headers, payload_data, auth):
    return requests.post(url, headers=headers, data=payload_data, auth=auth)


def main(args: List[str]) -> Response:
    arg_parser = argparse.ArgumentParser(description='Get rabbitmq messages', allow_abbrev=False)
    arg_parser.add_argument(
        '--configfile',
        action='store',
        help='Configuration file (full or relative path)',
    )

    arg_parser.add_argument(
        '--url',
        action='store',
        default='http://127.0.0.1:15672',
        help='RabbitMQ server url without slash, default = http://127.0.0.1:15672.',
    )

    arg_parser.add_argument(
        '-v',
        '--vhost',
        action='store',
        default='%2F',
        help="RabbitMQ virtual server, default = '/'."
    )

    arg_parser.add_argument(
        '-q',
        '--queue',
        action='store',
        default=None,
        help='The queue from where the messages will be obtained.'
    )

    arg_parser.add_argument(
        '-c',
        '--count',
        action='store',
        type=int,
        default=10,
        help='controls the maximum number of messages to get. Default=5.'
    )

    arg_parser.add_argument(
        '--user',
        '-u',
        action='store',
        default='guest',
        help='RabbitMQ user, default = guest.',
    )

    arg_parser.add_argument(
        '--password',
        '-p',
        action='store',
        default='guest',
        help='RabbitMQ password, default = guest.',
    )

    arg_parser.add_argument(
        '--outputfile',
        '-o',
        action='store',
        default='./messages',
        help='file for output messages.',
    )

    arg_parser.add_argument(
        '--separator',
        '-s',
        action='store',
        default=None,
        help='Character for line separator.',
    )

    arg_parser.add_argument(
        '--mode',
        '-m',
        action='store',
        default='full',
        help='full = whole message, payload = just payload',
    )

    __args = arg_parser.parse_args()
    config_data = {}

    def __config(key_arg):
        if vars(__args)[key_arg] != arg_parser.get_default(key_arg):
            return vars(__args)[key_arg]
        if key_arg not in config_data:
            return arg_parser.get_default(key_arg)
        return config_data[key_arg]

    if __args.configfile:
        with open(__args.configfile, "r") as f:
            config_data = yaml.safe_load(f)

    for key in vars(__args):
        config_data[key] = __config(key)

    try:
        url = f"{config_data['url']}/api/queues/{config_data['vhost']}/{config_data['queue']}/get"
        payload_data = f"{{'count': {config_data['count']}, 'ackmode': 'ack_requeue_true', 'encoding': 'auto', 'truncate': 50000}}"
        auth = (config_data['user'], config_data['password'])
        mode = config_data['mode']
    except Exception as error:
        print("An exception occurred: ", error)
        raise

    headers = {
        'content-type': 'application/json',
    }

    return _get_messages(url, headers, payload_data, auth)
