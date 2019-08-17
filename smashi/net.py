import subprocess
import socket
import ifaddr

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('169.254.0.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def get_all_ips():
	ips = {}
	adapters = ifaddr.get_adapters()

	for adapter in adapters:
		for ip in adapter.ips:
			#print "%s: %s/%s" % (adapter.nice_name, ip.ip, ip.network_prefix)
			ips[ip.ip] = adapter.nice_name

	return ips

def get_current_adapter():
	ip = get_ip()
	all_ips = get_all_ips()
	return all_ips[ip]

def check_internet():
    try:
        s = socket.create_connection(('8.8.8.8', 80), 5)
        return True
    except:
        return False

