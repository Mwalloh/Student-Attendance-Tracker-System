from scapy.all import ARP, Ether, srp, conf, get_if_addr , get_if_hwaddr


conf.route.resync()

real_iface = conf.route.route("0.0.0.0")[0]

class NetworkScanner:
    def __init__(self, network_range: str):
        
        self.network_range = network_range

    def scan(self) -> list:
        arp_request = ARP(pdst=self.network_range)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast / arp_request
        
        
        answered, _ = srp(packet, timeout=2, verbose=False, iface=real_iface)

        devices = []
        for _, response in answered:
            
            devices.append({ 'mac': response.hwsrc})

        my_mac = get_if_hwaddr(real_iface)
        my_ip = get_if_addr(real_iface)

        if not any(d['mac'] == my_mac for d in devices):
            devices.append({'ip': my_ip, 'mac': my_mac})

        return devices

if __name__ == "__main__":
    
    network = "192.168.100.37/24"
    scanner = NetworkScanner(network)
    
    print(f"Scanning {network} on interface {real_iface}...")
    devices = scanner.scan()
    
  
    if not devices:
        print("No devices found. Ensure you are running with 'sudo'.")
    else:
        print(f"Found {len(devices)} devices:")
        for device in devices:
            print(f" MAC: {device['mac']}")