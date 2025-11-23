#Easy and Simple Port Scanner 
import socket 
import time 



print('-------ShadowPortX v1.0--------')

target = input('Enter the target port to scan :')

start = time.time()

open_ports = []

print(f'\nscanning the {target} port...\n')

for port in range(1, 100):
    print(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f'[OPEN] port {port}')
        open_ports.append(port)
    s.close()

end = time.time()

print("--------------------------------------")
print("-----------SCAN COMPLETED-------------")
print("--------------------------------------")

print(f'Total open ports : {len(open_ports)} ')
print(f'Ports : {open_ports} ')
print(f'Total time taken : {round(end - start, 2)}s')