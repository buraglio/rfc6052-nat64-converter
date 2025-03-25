# RFC 6052 Converter

This application converts between synthesized IPv6 addresses (RFC 6052) and their corresponding IPv4 addresses. This contains all of the functionality of the
cli script but has more requirements due to using flask to run as a webapp with an API

## Features
- Convert IPv4 addresses to synthesized IPv6 addresses using a configurable prefix
- Convert synthesized IPv6 addresses back to IPv4
- Web-based form interface for easy conversion
- API endpoint for programmatic use
- Daemon mode for running as a background service

## Requirements

Python 3.x

`flask`

`gunicorn`

`argparse`

## Installation

Ensure you have Python installed, then download the script.

Install all requirements:
`pip3 install flask gunicorn argparse`


## Installation
1. Install dependencies:

`pip install flask gunicorn argparse`

Profit (maybe, but not likely).

~Optional:~

Set up a venv (not required. These things drive me nuts but I am beginning to see utility)
cd to the directory where you want to run this thing. 
`python3 -m venv .`
`source bin/activate`
`python3 -m pip install flask gunicorn argparse`

2. Run the application:

`python rfc6052_converter.py`
or
`./rfc6052_converter.py`

## API Usage
- Convert IP using API:
  ```
  GET /convert?source=<IP>&prefix=<PREFIX>
  ```
- Example:
  ```
  GET /convert?source=192.0.2.1&prefix=64:ff9b::/96
  ```

## Running as a Daemon
To run in the background:

`python rfc6052_converter.py -d`
or
`./rfc6052_converter.py -d`

Open a browser and navigate to `http://[::1]:5001`

## Best practice
Wrap this thing in nginx and add an SSL certificate.

## To Do
Make an init or systemctl script to start this piece of junk on boot
Make this more resilient and efficient