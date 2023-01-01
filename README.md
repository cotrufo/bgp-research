# bgp-research

This is a script that created by me (Alessandro Cotrufo), that tests against an IP that is vulnerable to BGP Hijacking, here is a friendly-explanation on how it works:

The attacker enters the target and destination IP addresses. These are the IP addresses of the network and the intended destination network, respectively.

Next, a BGP update message is created using the Scapy library's IP and Raw classes. The IP class is used to create an IP packet and set the destination IP address to the target IP address entered by the attacker. The Raw class is used to create a packet payload containing a sequence of bytes that represent a BGP update message. This BGP update message is then sent to the target IP address using the Scapy send() function.

The script then sends a BGP query to the target IP address and receives a response using the Scapy sr() function. This function sends a packet and receives a response, and returns a pair of lists representing the sent and received packets.

The byte sequence b"\x02\x01\x00\x01\x01\x00" + b"\x00" * 54 represents a BGP update message with a certain format specified in the BGP protocol.

The first two bytes, \x02\x01, represent the BGP message type, which is 2 for update messages. The next two bytes, \x00\x01, represent the number of withdrawn routes in the update message. The next two bytes, \x01\x00, represent the number of path attributes in the update message.

The remaining 54 bytes, b"\x00" * 54, represent the path attributes and the withdrawn routes. In this case, they are all set to 0 since they are not used in this script.

In a real BGP update message, the path attributes and withdrawn routes fields would contain information about the new routes and the routes being withdrawn, respectively. The BGP update message is then sent to the target IP address using the Scapy send() function, and a BGP query is sent to the target IP address to receive a response containing information about the new routes.

The script then checks the received packets in the response to see if any of them indicate that the target IP address is using the new BGP routes specified in the BGP update message. It does this by looking for packets with certain characteristics, such as having an IP source address equal to the target IP address and a TCP source port equal to 179 (the well-known port for BGP). If a packet with these characteristics is found, the script prints a message saying that the BGP hijack was successful and prints the new BGP routes contained in the packet's payload. If no such packet is found, the script prints a message saying that the BGP hijack was not successful.

This script was made for the purpose of presenting: https://www.researchgate.net/publication/366183227_Exploring_the_Threat_of_BGP_Hijacking
