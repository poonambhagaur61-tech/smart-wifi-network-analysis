 from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

# Capture packets
sniff(prn=packet_callback, count=10)
import psutil

data = psutil.net_io_counters()
print(data.bytes_sent, data.bytes_recv)