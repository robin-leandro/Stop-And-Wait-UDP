import socket
import struct


class PseudoTCPNode:
    HEADER_SIZE = 1
    PACKET_SIZE = 1
    SOCKET_TIMEOUT = .50
    HEADER_SYN = 0x01
    HEADER_ACK = 0x02
    HEADER_FIN = 0x04

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(PseudoTCPNode.SOCKET_TIMEOUT)

    def bind(self, address):
        self.sock.bind(address)

    def accept(self):
        pass

    def recv(self):
        pass

    def connect(self, address):
        # Instantiate a socket to send the data
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        new_socket.settimeout(self.SOCKET_TIMEOUT)

        while True:
            # Send SYN
            new_socket.sendall(PseudoTCPNode.HEADER_SYN)

            # Wait for SYN-ACK
            syn_ack = new_socket.recv(PseudoTCPNode.PACKET_SIZE)

            # If nothing was received or the packet was not SYN-ACK, try again
            if not syn_ack or not self._are_flags_set(syn_ack, self.HEADER_SYN, self.HEADER_ACK):
                break



        # Send ACK
        pass

    def send(self):
        pass
