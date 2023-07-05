import paramiko
import json

# JSON-bestand met switchgegevens
switches_file = 'data/switches.json'
credentials_file = 'data/credentials.json'
output_file = 'data/output.txt'

# SSH-client maken
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Laden van switchgegevens uit JSON-bestand
with open(switches_file) as file:
    switches_data = json.load(file)

# Laden van credentials uit JSON-bestand
with open(credentials_file) as file:
    credentials_data = json.load(file)

# Extract gebruikersnaam en wachtwoord uit credentials
username = credentials_data["username"]
password = credentials_data["password"]

# Open het output bestand in schrijfmodus
output = open(output_file, 'w')

# Loop over de switches
for switch in switches_data:
    hostname = switch["hostname"]

    # Verbinding maken met de switch
    client.connect(hostname=hostname, username=username, password=password, look_for_keys=False)

    # SSH-commando uitvoeren en uitvoer ophalen
    stdin, stdout, stderr = client.exec_command("show interfaces")
    command_output = stdout.read().decode()

    # Interfacegegevens extraheren
    interfaces = []
    lines = command_output.splitlines()  
    i = 0
    while i < len(lines):
        if lines[i].startswith("GigabitEthernet"):
            interface = lines[i].split()[0]
            status_line = lines[i+1]
            if lines[i+10].startswith("Last input"):
                last_input_line = lines[i+10]
            else:
                last_input_line = lines[i+10]
            last_input = last_input_line.split(":")[-1].strip()
            interfaces.append((interface, last_input))
            i += 12
        else:
            i += 1

    # Interfaces afdrukken naar de console + wegschrijven naar output.txt
    print("----------", hostname, "----------")
    output.write("---------- {} ----------\n".format(hostname))
    for interface, last_input in interfaces:
        if last_input == "Last input never, output never, output hang never":
            print(f"{interface} - {last_input}")
            output.write(f"{interface} - {last_input}")
            output.write("\n")

    # Verbinding sluiten
    client.close()

# Sluit het output bestand
output.close()

