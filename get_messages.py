#!/usr/bin/python
import argparse
import requests
import csv
import yaml

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
    default='NOTIFY_INTENTIONS',
    help='The queue from where the messages will be obtained.'
)

arg_parser.add_argument(
    '-c',
    '--count',
    action='store',
    type=int,
    default=5,
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


args = arg_parser.parse_args()

config = None
if args.configfile:
    with open(args.configfile, "r") as f:
        config = yaml.safe_load(f)
else:
    config = {
        'url': args.url,
        'vhost': args.vhost,
        'queue': args.queue,
        'count': args.count,
        'user': args.user,
        'password': args.password,
        'outputfile': args.outputfile,
    }

try:
    url = f"{config['url']}/api/queues/{config['vhost']}/{config['queue']}/get"
    payload_data = f"{{'count': {config['count']}, 'ackmode': 'ack_requeue_true', 'encoding': 'auto', 'truncate': 50000}}"
    auth = (config['user'], config['password'])
except Exception as error:
    print(config)
    print("An exception occurred: ", error)
    raise

headers = {
    'content-type': 'application/json',
}

response = requests.post(url, headers=headers, data=payload_data, auth=auth)

with open(config['outputfile'], 'w') as file_handler:
    for message in response.json():
        file_handler.write("{}\n".format(message['payload']))

