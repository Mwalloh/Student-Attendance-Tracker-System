#   Providing a common function that is used to get the network range 
#   The IP addresses and networks connected on a device (Modules inside python)
import ipaddress
import netifaces

class NetworkUtils:
    #Refering to any object...
    @staticmethod

    #get network range
    def get_local_network():
        try:
            #this used to get various interfaces and their names
            iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
            #this gets the IP addresses 
            addr_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]

            ip = addr_info['addr']
            netmask = addr_info['netmask']

            # Ignore link-local
            if ip.startswith("169.254"):#global IP address
                raise ValueError("Link-local address") #19.....

            network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)

            return str(network)

        except Exception:
            #Hardware IP Address that is used in alll devices connected to a network
            return "192.168.0.0/24"
