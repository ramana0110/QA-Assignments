import re
unparsed = """
Interface             IP-Address      OK? Method Status        Protocol
FastEthernet0/0       15.0.15.1       YES manual up            up
FastEthernet0/1       10.0.12.1       YES manual up            up
FastEthernet0/2       10.0.13.1       YES manual up            up
FastEthernet0/3       unassigned      YES unset  up            down
Loopback0             10.1.1.1        YES manual up            up
Loopback100           100.0.0.1       YES manual up            up
"""

# Define a regex pattern to capture the interface details
pattern = re.compile(r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)')

# Split the output into lines
lines = unparsed.strip().split('\n')
    
# Initialize an empty list to store the parsed data
parsed_data = []
    
# Iterate over each line after the header
for line in lines[1:]:
    match = pattern.match(line)
    if match:
        # Extract matched groups
        interface, ip_address, ok, method, status, protocol = match.groups()
           
        # Create a dictionary for the interface
        interface_info = {
                'Interface': interface,
                'IP-Address': ip_address,
                'OK?': ok,
                'Method': method,
                'Status': status,
                'Protocol': protocol
            }
            
        # Append the dictionary to the list
        parsed_data.append(interface_info)
print(parsed_data) 