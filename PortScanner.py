#Easy and Simple Port Scanner 
import socket 
import time 
from tqdm import tqdm as t
import time 




print('-------ShadowPortX v1.0--------')

target = input('Enter the target port to scan :')

start = time.time()

open_ports = []

print(f'\nscanning {target} port...\n')

for port in t(range(1, 1025), desc="Scanning Ports", colour="yellow", ncols=100):
    time.sleep(0.02)
    #print(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.02)

    result = s.connect_ex((target, port))

    if result == 0:
        t.write(f'[OPEN] port {port}')
        open_ports.append(port)
    s.close()

end = time.time()

print("--------------------------------------")
print("-----------SCAN COMPLETED-------------")
print("--------------------------------------")

print(f'Total open ports : {len(open_ports)} ')
print(f'Ports : {open_ports} ')
print(f'Total time taken : {round(end - start, 2)}s')