
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

logging.basicConfig(filename='TCP_Client.log', level=logging.DEBUG, format='[%(asctime)s][%(filename)s] %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class Client():
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


if __name__ == "__main__":

    logging.info('[controller.trinket] Trying to connect...')
    client = Client()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 8090)
        print ('connecting to %s port %s' % (client.address, client.port))
        sock.connect(client.address, client.port)
        client.connected = True

        logging.info('[controller.trinket] Connected...')

    except:
        logging.info('[controller.trinket] No Connected. Waiting 10 sec... ')
        time.sleep(10)


    while client.running:
        
        try:
            data = sock.recv(84)
            logging.debug('<< ' + ' '.join(hex(b) for b in data if b != 0x55))   

            ## Do Something
            if data:

                b = bytearray(data)
                if b[0] == client.indicationENQ:
                    b[0] = 0x6

                    print("SEND ACK")
                    sock.send(client.indicationACK)

                else:
                    print("MSG UNKNOWN")
                    sock.send(0x0F)



        except:
            logging.info('[controller.trinket] Error com cycle')
            traceback.print_exc()
            client.connected = False
            sock.close()
