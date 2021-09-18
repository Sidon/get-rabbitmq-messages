import argparse
import yaml

__config_data = {}


def __config_args(key_arg, __args, __arg_parser, __config_data):
    if vars(__args)[key_arg] != __arg_parser.get_default(key_arg):
        return vars(__args)[key_arg]
    if key_arg not in __config_data:
        return __arg_parser.get_default(key_arg)
    return __config_data[key_arg]


def build_data_queue_args(parser, __args):
    # __args = __arg_parser.parse_args()

    data_config = {}

    if __args.configfile:
        with open(__args.configfile, "r") as f:
            data_config = yaml.safe_load(f)

    for key in vars(__args):
        data_config[key] = __config_args(key, __args, parser, data_config)
    try:
        data_config['url'] = f"{data_config['url']}/api/queues/{data_config['vhost']}/{data_config['queue']}/get"
        data_config['payload_data'] = f"{{'count': {data_config['count']}, 'ackmode': 'ack_requeue_true', 'encoding': 'auto', 'truncate': 50000}}"
        data_config['auth'] = (data_config['user'], data_config['password'])
        data_config['headers'] = {'content-type': 'application/json', }
    except Exception as error:
        print("An exception occurred: ", error)
        raise

    return data_config
