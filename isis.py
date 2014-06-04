import re,socket,time,sys,telnetlib
from struct import pack,unpack


def is_ipv6(ip):
    return ':' in ip

def get_socket(chal):
    '''chal is a 2-tuple with an address and a port  ex: ('127.0.0.1',111)'''
    #is ipv6?
    ip,port=chal
    if is_ipv6(ip):
        s=socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)
        s.settimeout(5)
        s.connect((ip,port,0,0))
    else:#ipv4
        s=socket.socket()
        s.settimeout(5)
        s.connect(chal)
    return s

def lei(*nums):
    '''
    wrapper for struct.pack("I/i"), will identify signdness and
    takes a variable number of arguments
    '''
    if(len(nums)==1):
        num=nums[0]
        if(num>0):
            return pack("<I",num) # little-endian, unsigned int
        else:
            return pack("<i",num) # little-endian int
    else:
        return ''.join(map(lei,nums))

def lei64(*nums):
    '''
    wrapper for struct.pack("Q/q"), will identify signdness and
    takes a variable number of arguments
    '''
    if(len(nums)==1):
        num=nums[0]
        if(num>0):
            return pack("<Q",num) # little-endian, unsigned int
        else:
            return pack("<q",num) # little-endian int
    else:
        return ''.join(map(lei64,nums))

def ulei(nums):
	'''unpacks arbitray amount of 32bit packed values returns list'''
	lis, unList = [], []
	for i in chunk(nums,4):
		#right justified due to bit read order adjust as necessary
		i = i.rjust(4,'0')
		unList.append(i)
	while len(unList) != 0:
		struc = unpack("<I", unList[0])
		lis.append(struc[0])
		del unList[0]
	return lis

def ulei64(nums):
	'''unpack arbitrary amount of 64 bit packed values'''
	lis,unList = [],[]
	for i in chunk(nums, 8):
		#Right justified due to bit read order adjust as necessary
		i = i.rjust(8,'0')
		unList.append(i)
	while len(unList)!=0:
		struc = unpack("<Q", unList[0])
		lis.append(struc[0])
		del unList[0]
	return lis

def chunk(iterable, chunk_size):
    '''Divide iterable into chunks of chunk_size'''
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i:i+chunk_size]



def telnet_shell(sock):
    '''pass to this function a socket object with a listening shell(socket reuse)'''
    tc = telnetlib.Telnet()  
    tc.sock = sock
    tc.interact() 
    return

def recv_until(s, data):
	'''receive data from s until string data is found s(socket, "string")'''
	p = ""
	while data not in p:
		p += s.recv(0x1)
	return p

def recv_all(s):
    '''receive and discard all data from a connection'''
    while len(s.recv(1024)) == 1024:
        pass






