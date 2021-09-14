#!/usr/bin/python
import argparse, requests, pprint
import config_args_parser


def save_messages(url, headers, data, auth, output_file, message_separator):
    response = requests.post(url, headers=headers, data=data, auth=auth)
    with open(output_file, 'w') as file_handler:
        for msg in response.json():
            message = msg if data_args['mode'] == 'full' else msg['payload']
            output_message = f"\n{pprint.pformat(message, indent=4)}"
            file_handler.write(output_message)
            file_handler.write(message_separator)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description='Get rabbitmq messages', allow_abbrev=False)
    config_args_parser.config_parser(arg_parser)
    __args = arg_parser.parse_args()
    data_args = config_args_parser.build_data_args(__args, arg_parser)
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
        separator
    )

