# PortScanner

PortScanner is a simple tool to scan open ports of an IP address or URL.

## Requirements

- Python 3.x
- Nmap (for scanning ports)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shusjeshsje/portscanner.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Nmap (if not installed):
   - On Linux: `sudo apt install nmap`
   - On macOS: `brew install nmap`
   - On Windows: Download and install from [Nmap Official Website](https://nmap.org/download.html)

## Usage

To scan ports, run the following command:
```bash
python portscanner.py --scan <IP_ADDRESS_OR_URL>
