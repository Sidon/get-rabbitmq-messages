``Rabbitapi`` - Get RabbitMQ messages via API


Description
***********

Get RabbitMQ messages from a specific queue to a file, via api.


Requirements
************

::

    Python 3


Environment
***********

::

    linux


Install
#######

::

    pip install getrabbitgetapi


Usage
#####

::

    ❯ rabbitgetapi getqueue -h
    usage: rabbitgetapi getqueue [-h] [-f CONFIGFILE] [--url URL] [-v VHOST] [--user USER] [--password PASSWORD] [--outputfile OUTPUTFILE]
                                 [--separator SEPARATOR] [--mode MODE] [-q QUEUE] [-c COUNT]

    optional arguments:
      -h, --help            show this help message and exit
      -f CONFIGFILE, --configfile CONFIGFILE
                            Configuration file (full or relative path)
      --url URL             RabbitMQ server url without slash, default = http://127.0.0.1:15672.
      -v VHOST, --vhost VHOST
                            RabbitMQ virtual server, default = '/'.
      --user USER, -u USER  RabbitMQ user, default = guest.
      --password PASSWORD, -p PASSWORD
                            RabbitMQ password, default = guest.
      --outputfile OUTPUTFILE, -o OUTPUTFILE
                            file for output messages.
      --separator SEPARATOR, -s SEPARATOR
                            Character for line separator.
      --mode MODE, -m MODE  full = whole message, payload = just payload
      -q QUEUE, --queue QUEUE
                            The queue from where the messages will be obtained.
      -c COUNT, --count COUNT
                            controls the maximum number of messages to get. Default=10.

:Authors:
    Sidon Duarte,

:Version: 0.0.1 at 2021/09/12
