import ipaddress
import os
import socket
import struct
import sys
import threading
import time

# SUBNET TO TARGET
SUBNET = '172.26.246.0/24'
MESSAGE = 'DEEZ NUTS!!!'

class IP:
    def __init__(self, buff):
        header = struct.unpack('<BBHHHBBH4s4s', buff)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        # HUMAN READABLE IP ADDRESSES
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_addres = ipaddress.ip_address(self.dst)

        # MAP PROTOCOL CONSTANTS TO THEIR NAMES
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print('%s No protocol for %s' % (e, self.protocol_num))
            self.protocol = str(self.protocol_num)

   
class ICMP:
    def __init__(self, buff):
        header = struct.unpack('<BBHHH', buff)
        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]

def udp_sender():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sender:
        for ip in ipaddress.ip_network(SUBNET).hosts():
            sender.sendto(bytes(MESSAGE, 'utf8'), (str(ip), 65212))

class Scanner:
    def __init__(self,host):
        self.host = host
        if os.name == 'nt':
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP
        self.socket = socket.socket(socket.AF_INET,
                                        socket.SOCK_RAW, socket_protocol
        )
        self.socket.bind((host, 0))
        self.socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

        if os.name == 'nt':
            self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    def sniff(self):
        hosts_up = set([f'{str(self.host)} *'])
        try:
            while True:
                # READ A PACKET
                raw_buffer = self.socket.recvfrom(65535)[0]
                # CREATE AN IP HEADER FROM THE FIRST 20 BYTES
                ip_header = IP(raw_buffer[0:20])
                # ACCEPT ICMP
                if ip_header.protocol == 'ICMP':
                    offset = ip_header.ihl * 4
                    buff = raw_buffer[offset:offset + 8]
                    icmp_header = ICMP(buff)
                    # CHECK FOR TYPE 3 AND CODE
                    if icmp_header.code == 3 and icmp_header.type == 3:
                         if ipaddress.ip_address(ip_header.src_address) in ipaddress.IPv4Network(SUBNET):
                            if raw_buffer[len(raw_buffer) - len(MESSAGE):] == bytes(MESSAGE, 'utf8'):
                                tgt = str(ip_header.src_address)
                                if tgt != self.host and tgt not in hosts_up:
                                    hosts_upp.add(str(ip_header.src_address))
                                    print(f'Host Up: {tgt}')

        except KeyboardInterrupt:
            if os.name == 'nt':
                self.socket.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

            print('\nUser interrupted.')
            if hosts_up:
                print(f'\n\nSummary: Hosts up on {SUBNET}')
            for host in sorted(hosts_up):
                print(f'{host}')
            print('')
            sys.exit()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        host = sys.argv[1]
    else:
        host = '172.26.246.207'
    s = Scanner(host)
    time.sleep(5)
    t = threading.Thread(target=udp_sender)
    t.start()
    s.sniff()