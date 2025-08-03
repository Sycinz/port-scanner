import socket

def scan_ports(target, start_port, end_port):
    print(f"🔍 Scanning host {target} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, 'tcp')
            except OSError:
                service = "unknown"
            print(f"[+] Port {port} is open (service: {service})")
        sock.close()

if __name__ == "__main__":
    target_ip = input("Type IP adress in here (for example 192.168.1.1): ")
    start = int(input("Port range from: "))
    end = int(input("Port range to: "))
    scan_ports(target_ip, start, end)
