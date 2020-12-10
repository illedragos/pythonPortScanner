import socket
import threading
from queue import Queue

target = "127.0.0.1"
queque = Queue()
open_ports = []


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def fill_queque(port_list):
    for port in port_list:
        queque.put(port)


def worker():
    while not queque.empty():
        port = queque.get()
        if portscan(port):
            print("Port {} is open".format(port))
            open_ports.append(port)


port_list = range(1, 1024)
fill_queque(port_list)

thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are :", open_ports)

# PORT SCAN WITHOUT MULTITHREADING
# for port in range(1, 1024):  # standard ports
#    result = portscan(port)
#    if result == True:
#        print("Port {} is open".format(port))
#    else:
#        print("Port {} is closed".format((port)))
