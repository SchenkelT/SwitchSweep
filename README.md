![GitHub last commit](https://img.shields.io/github/last-commit/SchenkelT/SwitchSweep)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/SchenkelT/SwitchSweep)

# Cisco Interface Downtime Collector

This Python script collects information about the downtime of Cisco interfaces on switches.

## Requirements

- Python 3.x
- Paramiko library (for SSH connections)

## Installation

1. Ensure that Python 3.x is installed on your system.
2. Install the Paramiko library using pip:

```
pip install paramiko

```

## Usage

1. Edit the `switches.json` file and add the IP addresses of your Cisco switches along with the username and password in `credentials.json`.
2. Run the script using the following command:

```
python Interface_Downtime.py
```

The script will establish SSH connections to the specified switches, check the downtime of the interfaces, and display the results on the console.

The output will also be saved in an `output.txt` file.

## Contributing

Contributions to this project are welcome! If you would like to propose improvements, report issues, or add new features, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
