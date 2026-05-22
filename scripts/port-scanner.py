import socket, sys
def scan_port(host, port, timeout=1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        result = s.connect_ex((host, port))
        s.close()
        return result == 0
    except: return False

def scan_range(host, start, end):
    open_ports = []
    for port in range(start, end+1):
        if scan_port(host, port):
            open_ports.append(port)
            print(f'  {port}: OPEN')
    return open_ports

if __name__=='__main__':
    host = sys.argv[1] if len(sys.argv)>1 else '127.0.0.1'
    print(f'Scanning {host}...')
    scan_range(host, 1, 1024)
