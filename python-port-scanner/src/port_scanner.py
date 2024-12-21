import nmap
import argparse
from prettytable import PrettyTable

def parse_arguments():
    parser = argparse.ArgumentParser(description='Simple Port Scanner')
    parser.add_argument('target', help='IP address or URL to scan')
    parser.add_argument('-p', '--ports', help='Comma-separated list of ports to scan (default: 1-1024)', default='1-1024')
    return parser.parse_args()

def scan_ports(target, ports):
    nm = nmap.PortScanner()
    nm.scan(target, ports)
    return nm[target]['tcp']

def display_results(results):
    table = PrettyTable()
    table.field_names = ["Port", "State"]
    for port, state in results.items():
        table.add_row([port, state])
    print(table)

def main():
    args = parse_arguments()
    target = args.target
    ports = args.ports
    print(f'Scanning {target} for ports: {ports}')
    
    try:
        results = scan_ports(target, ports)
        display_results(results)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()