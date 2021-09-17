#!/usr/bin/python
import argparse, requests, pprint
import config_args_parser


def save_messages(url, headers, data, auth, output_file, mode, message_separator):
    response = requests.post(url, headers=headers, data=data, auth=auth)
    if response.status_code == 200:
        with open(output_file, 'w') as file_handler:
            for msg in response.json():
                message = msg if mode == 'full' else msg['payload']
                output_message = f"\n{pprint.pformat(message, indent=4)}"
                file_handler.write(output_message)
                file_handler.write(message_separator)


def main():
    data_args = config_args_parser.build_data_args()
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


if __name__ == "__main__":
    main()
