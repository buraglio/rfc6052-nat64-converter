# Binary version
This repo is for the original python code. There is a go binary that is *much* faster and efficien and contains more utility, including this, that is available [here](https://github.com/buraglio/ipv6utils)


# RFC 6052 converter

This script allows you to convert between IPv6 and IPv4 addresses using the default well-known prefix (64:ff9b::/96) or specify a custom prefix.

## Use

Download the script

`chmod +x rfc6502-converter.py`

Convert an IPv6 synthesized address to IPv4:

`python3 rfc6502-converter.py -s 64:ff9b::1799:84e`
or
`./rfc6502-converter.py 

Convert an IPv4 address to an RFC 6052 synthesized IPv6 address:

`python rfc6502-converter.py -s 23.153.8.78`
or
`rfc6502-converter.py -s 23.153.8.78`

Use a custom prefix:

`./rfc6502-converter.py -s 3ffe:64::1799:84e -p 3ffe:64::/96`
or
`./rfc6502-converter.py -s 23.153.8.78 -p 3ffe:64::/96`
