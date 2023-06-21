from http import server
import socket
from  _thread import *
import sys



SERVER = "10.0.0.82"    # this is my local IPv4
PORT = 5555
NUM_CONNECTIONS = 2



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((SERVER, PORT))
except socket.error as e:
    str(e)

s.listen(NUM_CONNECTIONS)
print("Server start - Waiting for connection")



def threaded_client(conn):

    conn.send(str.encode("Connected"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))