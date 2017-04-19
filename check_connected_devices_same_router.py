import socket
from multiprocessing import Pool

# for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
#ex 192.168.1
def get_subnet():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	my_local_ip = s.getsockname()[0]
	s.close()
	return '.'.join(my_local_ip.split('.')[:3])

def check_ip_exist(ip):
	try:
		print socket.gethostbyaddr(ip)
	except socket.herror:
		pass
def check_range_ip():
	subnet = get_subnet()
	list_ip = [subnet + '.' + str(i) for i in xrange(1,255)]
	p = Pool(50)
	p.map(check_ip_exist, list_ip)

if __name__ == '__main__':
	check_range_ip() 
    

