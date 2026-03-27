 from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Capture packets
sniff(prn=packet_callback, count=10)
import psutil

data = psutil.net_io_counters()
print(data.bytes_sent, data.bytes_recv)
from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        print(packet["IP"].src, "->", packet["IP"].dst)

sniff(prn=packet_callback, count=20)