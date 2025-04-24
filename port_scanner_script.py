import socket

# Dictionary with service descriptions
service_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    139: "NetBIOS",
    111: "RPC",
    631: "CUPS",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP-alt",
    1433: "MSSQL",
    1521: "Oracle DB",
    5432: "PostgreSQL",
    6379: "Redis",
    8000: "Web Dev",
    8443: "HTTPS-alt",
    8888: "Jupyter"
}

# List of common ports
common_ports = list(service_ports.keys())

# Port scanning function
def scan_ports(target, ports):
    print(f"\nScanning host {target} on ports: {', '.join(map(str, ports))}\n")
    for port in ports:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            s.settimeout(0.5)
            # Check if the port is open
            status = s.connect_ex((target, port))
            # Get the service name for the port
            service = service_ports.get(port, "Unknown")
            if status == 0:
                print(f"Port {port:>5} - OPEN   ({service})")
            else:
                print(f"Port {port:>5} - CLOSED ({service})")
            # Close the socket connection
            s.close()
        except Exception as e:
            # Print an error message if an exception occurs
            print(f"Port {port} - Error: {e}")

# === INPUT ===
# Prompt the user to enter the IP address to scan
target = input("Enter the IP address to scan: ")

# Present scanning mode choices to the user
print("\n1) Range of ports (e.g., 20-80)")
print("2) Enter ports manually (e.g., 21,22,80,443)")
print("3) Scan predefined common ports")
mode = input("Choose mode [1/2/3]: ")

if mode == '1':
    # User chooses to scan a range of ports
    portrange = input("Enter the range (e.g., 20-80): ")
    lowPort = int(portrange.split("-")[0])
    highPort = int(portrange.split("-")[1]) + 1
    ports = list(range(lowPort, highPort))

elif mode == '2':
    # User chooses to enter specific ports manually
    portlist = input("Enter ports separated by commas (e.g., 21,22,80,443): ")
    ports = [int(p.strip()) for p in portlist.split(",")]

elif mode == '3':
    # User chooses to scan predefined common ports
    ports = common_ports
    print("Using the predefined list of common ports.")

else:
    # Invalid choice, exit the program
    print("Invalid choice. Exiting.")
    exit()

# Start the port scan
scan_ports(target, ports)
