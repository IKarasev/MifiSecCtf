#!/bin/sh

# Use FLASK_DEBUG=True if needed
FLASK_DEBUG=True
FLASK_APP=$(dirname $(readlink -f $0))/standalone.py python3 -m flask run --host 0.0.0.0 --port 5541 --with-threads
