#!/usr/bin/python3

from scapy.all import *
from time import sleep
from ipaddress import IPv4Network
import argparse

TIMEOUT = 0.3

def knock_knock_everywhere(params):
    port_range = params['port-range'] if params.get('port-range') is not None else '1:9999'
    ip =         params['ip']         if params.get('ip')         is not None else '192.168.1.1'
    
    port_range = port_range.split(':')
    first_port = int(port_range[0])
    last_port = int(port_range[1])

    print('Starting port knocking attack }:)')
    
    for port in range(first_port, last_port):
        packet = IP(dst=ip, ttl=5)/ICMP()
        reply = sr1(packet, timeout=TIMEOUT)
        if reply is None:
            continue
        print('Port {} answer us ;)'.format(port))
        
        for port2 in range(first_port, last_port):
            reply = sr1(packet, timeout=TIMEOUT)
            if reply is None:
                continue
            print('Port knocking is broken }:)')
            print('Ports are {} and {}'.format(port, port2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--ip',
        type=str,
        help='Victim\'s ip.',
    )
    parser.add_argument(
        '--port-range',
        type=str,
        nargs='?',
        help='Port range to explore example: (1:9999)',
    )
    params = vars(parser.parse_args())
    knock_knock_everywhere(params)
