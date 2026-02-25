# Controlled network scanner

def scan_network():
    '''Simulates scanning the network for connected devices.'''
    connected_devices = [
        "ed:de:ec:31:01:9d",  # Kevin Hart
        "95:f9:5e:6b:7e:1d",  # Aya Nakamura
        "74:38:1b:12:a4:2e",  # Chong Li
        "aa:bb:cc:dd:ee:ff"   # Unknown device
    ]
    return connected_devices


if __name__ == "__main__":
    print(scan_network())