import ipaddress
from scapy.all import conf, get_if_addr

class NetworkUtils:
    @staticmethod
    def get_local_network():
        try:
            conf.route.resync() # Refresh Mac routes
            res = conf.route.route("0.0.0.0")
            iface_name = res.name if hasattr(res, 'name') else str(res)
            
            # Look for the REAL network, skipping 169.254 (APIPA)
            for network, mask, gateway, iface, addr, *extra in conf.route.routes:
                # Check if it's the right interface and not the default route
                if iface == iface_name and network != 0:
                    net_ip = ipaddress.IPv4Address(network)
                    
                    # IGNORE LINK-LOCAL (169.254.x.x)
                    if not net_ip.is_link_local:
                        cidr = bin(mask).count('1')
                        # If Scapy gives /32 (single host), fix it to /24 (network)
                        if cidr == 32: cidr = 24
                        return f"{net_ip}/{cidr}"
            
            # EMERGENCY FALLBACK: Use your own IP directly
            my_ip = get_if_addr(iface_name)
            if my_ip and not my_ip.startswith("169.254"):
                return f"{my_ip.rsplit('.', 1)[0]}.0/24"
                
            return "192.168.0.0/24" # Ultimate default
        except Exception as e:
            return "192.168.0.0/24"
