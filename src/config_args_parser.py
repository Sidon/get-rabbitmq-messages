import argparse
import yaml

__config_data = {}


def __config_args(key_arg, __args, __arg_parser, __config_data):
    if vars(__args)[key_arg] != __arg_parser.get_default(key_arg):
        return vars(__args)[key_arg]
    if key_arg not in __config_data:
        return __arg_parser.get_default(key_arg)
    return __config_data[key_arg]


def config_parser(__arg_parser):
    __arg_parser.add_argument(
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
        '-q',
        '--queue',
        action='store',
        default=None,
        help='The queue from where the messages will be obtained.'
    )
    __arg_parser.add_argument(
        '-c',
        '--count',
        action='store',
        type=int,
        default=10,
        help='controls the maximum number of messages to get. Default=5.'
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


# def build_data_args(__args, __arg_parser):
def build_data_args():
    __arg_parser = argparse.ArgumentParser(description='Get rabbitmq messages', allow_abbrev=False)
    config_parser(__arg_parser)
    __args = __arg_parser.parse_args()
    # data_args = config_args_parser.build_data_args(__args, arg_parser)

    data_config = {}

    if __args.configfile:
        with open(__args.configfile, "r") as f:
            data_config = yaml.safe_load(f)

    for key in vars(__args):
        data_config[key] = __config_args(key, __args, __arg_parser, data_config)

    try:
        data_config['payload_data'] = f"{{'count': {data_config['count']}, 'ackmode': 'ack_requeue_true', 'encoding': 'auto', 'truncate': 50000}}"
        data_config['url'] = f"{data_config['url']}/api/queues/{data_config['vhost']}/{data_config['queue']}/get"
        data_config['auth'] = (data_config['user'], data_config['password'])
        data_config['headers'] = {'content-type': 'application/json', }
    except Exception as error:
        print("An exception occurred: ", error)
        raise

    return data_config
