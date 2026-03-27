 from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Capture packets
sniff(prn=packet_callback, count=10)