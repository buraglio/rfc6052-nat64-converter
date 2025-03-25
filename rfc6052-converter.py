#!/usr/bin/env python3
#take a synthesized address and convert it 
#to the original and vice versa

import ipaddress
import argparse

def ipv6_to_ipv4(synthesized_ipv6, prefix):
    ipv6_addr = ipaddress.IPv6Address(synthesized_ipv6)
    prefix_network = ipaddress.IPv6Network(prefix, strict=False)
    
    prefix_len = prefix_network.prefixlen // 8  # Convert bits to bytes
    prefix_bytes = prefix_network.network_address.packed[:prefix_len]
    ipv6_bytes = ipv6_addr.packed
    
    if not ipv6_bytes.startswith(prefix_bytes):
        raise ValueError("The provided IPv6 address does not match the given prefix.")
    
    embedded_ipv4 = ipv6_bytes[prefix_len:prefix_len + 4]
    return str(ipaddress.IPv4Address(embedded_ipv4))

def ipv4_to_ipv6(ipv4, prefix):
    ipv4_addr = ipaddress.IPv4Address(ipv4)
    prefix_network = ipaddress.IPv6Network(prefix, strict=False)
    
    prefix_len = prefix_network.prefixlen // 8  # Convert bits to bytes
    prefix_bytes = prefix_network.network_address.packed[:prefix_len]
    ipv6_bytes = prefix_bytes + ipv4_addr.packed
    
    return str(ipaddress.IPv6Address(ipv6_bytes))

def main():
    parser = argparse.ArgumentParser(description="Convert between RFC 6052 synthesized IPv6 and IPv4 addresses.")
    parser.add_argument("-s", "--source", required=True, help="Source IPv6 or IPv4 address.")
    parser.add_argument("-p", "--prefix", default="64:ff9b::/96", help="Prefix for translation (default: 64:ff9b::/96).")
    
    args = parser.parse_args()
    
    try:
        if ":" in args.source:
            converted_ip = ipv6_to_ipv4(args.source, args.prefix)
            print(f"IPv6 {args.source} -> IPv4 {converted_ip}")
        else:
            converted_ip = ipv4_to_ipv6(args.source, args.prefix)
            print(f"IPv4 {args.source} -> IPv6 {converted_ip}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

