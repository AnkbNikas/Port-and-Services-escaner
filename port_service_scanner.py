import nmap

def scan_ports_services(ip_address):
    nm = nmap.PortScanner()
    print(f"Scanning host: {ip_address}")
    nm.scan(hosts=ip_address, arguments='--min-rate 5000 -p- -sV')
    for host in nm.all_hosts():
        print(f"\nHost : {host} ({nm[host].hostname()})")
        print(f"State : {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"Protocol : {proto}")
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                print(f"Port : {port}\tState : {nm[host][proto][port]['state']}\tService : {nm[host][proto][port]['name']}")

if __name__ == "__main__":
    ip_address = input("Enter the IP address to scan: ")
    scan_ports_services(ip_address)
