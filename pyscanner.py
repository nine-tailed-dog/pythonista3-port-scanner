import socket

print('\n')

hostname = input('Please enter a target hostname to scan\n')
hostname = str(hostname)
host = socket.gethostbyname(hostname)


print('\n')

print(('='*40))
print(('Please wait while scanning target {}'.format(host)))
print(('='*40))

try:
	for port in range(1,65536):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.9)
		result = s.connect_ex((host,port))
		if result == 0:
			print(('port {} is open'.format(port)))
		s.close()

except socket.error:
	print('there was an error connecting')
	
except KeyboardInterrupt:
	print(('-'*40))
	print('scan stopped')
			
except:
	print('error occurred')
	
print(('='*40))
print('scan complete')

