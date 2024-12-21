# Python Port Scanner

This project is a simple port scanner built in Python that utilizes the `nmap` library to scan specified IP addresses or URLs for open ports. It includes a user-friendly login interface for authentication before accessing the scanning functionality.

## Project Structure

```
python-port-scanner
├── src
│   ├── port_scanner.py       # Main logic for the port scanner
│   ├── static
│   │   └── index.html        # Main interface for the application
│   └── templates
│       └── login.html        # HTML structure for the login page
├── requirements.txt           # List of dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-port-scanner
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the login page:
   - Open `src/static/index.html` in a web browser to access the login interface.

2. After logging in, you can use the port scanner functionality by executing the following command in the terminal:
   ```
   python src/port_scanner.py <target>
   ```
   Replace `<target>` with the IP address or URL you wish to scan.

## Features

- User authentication via a login page.
- Scanning of specified IP addresses or URLs for open ports.
- Display of scan results in a formatted table.

## Dependencies

- nmap
- pystyle
- prettytable

## License

This project is licensed under the MIT License. See the LICENSE file for more details.