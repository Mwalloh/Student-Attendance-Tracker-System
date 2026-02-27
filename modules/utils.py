import ipaddress
import netifaces

class NetworkUtils:
    @staticmethod
    def get_local_network():
        try:
            # Get default gateway interface
            iface = netifaces.gateways()['default'][netifaces.AF_INET][1]

            addr_info = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]

            ip = addr_info['addr']
            netmask = addr_info['netmask']

            # Ignore link-local
            if ip.startswith("169.254"):
                raise ValueError("Link-local address")

            network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)

            return str(network)

        except Exception:
            return "192.168.0.0/24"
