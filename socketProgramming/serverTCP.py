#!/usr/bin/env python3
import logging
import threading
import uuid
import time
import sys
import os
import random
import socket
import traceback

logging.basicConfig(filename='TCP_Server.log', level=logging.DEBUG, format='[%(asctime)s][%(filename)s] %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


class Server():
    def __init__(self):

        self.address = "localhost"
        self.port = 8090
        self.connected = False
        self.linked = False
        self.running = True

        self.trama_len = 84
        self.indicationACK = 0x06
        self.indicationENQ = 0x05
        self.indicationSanction = 0xB1
        self.indicationAutoTest = 0x07
        self.erroneousMsg = 0xF0
        self.padding = 0x55

    def crc16(self, data):
        crc = 0x0000
        polynomial = 0x1021
        for b in data:
            for i in range(0, 8):
                bit = ((b   >> (7-i) & 1) == 1)
                c15 = ((crc >> 15    & 1) == 1)
                crc <<= 1
                if (c15 ^ bit):
                    crc ^= polynomial
        crc &= 0xffff
        return crc


def handleClient(client_sock, server):

    try:
        recv_data = client_sock.recv(84)
        print("[*] Received: %s" % recv_data)

        if recv_data:
            b = bytearray(recv_data)

            if b[0] == server.indicationACK:
                b[0] = 0x5
                
                print("SEND ENQ")
                client_sock.send(server.indicationENQ)
            else:
                print("MSG UNKNOWN")
                client_sock.send(server.erroneousMsg)

    except:
        print("Nothing")






if __name__ == "__main__":

    server = Server()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind((server.address, server.port))

    # Five connections maximal
    sock.listen(5)
    print ('listening on %s port %d' % (server.address, server.port))

    logging.info('[controller.trinket] Listening...')

    while server.running:

        client, address = sock.accept()
        print ('accepted connection from %s port %d' % (address[0], address[1]))

        client_handler = threading.Thread(target=handleClient, args=(client, server))
        client_handler.start()


