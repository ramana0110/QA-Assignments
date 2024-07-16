from scapy.all import rdpcap
#Reading packets from the pcap file
packets = rdpcap("E:\Ramana\EmbedUR\QA tools\Assignments\module1\macsec_cisco_trunk.pcap")
macsec_packets = []

for packet in packets:
#Checking whether the packet is of type MACsec
    if packet.haslayer("Ether") and packet["Ether"].type == 0x88E5:
        macsec_packets.append(packet)

#Printing the number of MACsec packets
print(len(macsec_packets))