import re,socket,time,sys,telnetlib
from struct import pack,unpack

pattern = "AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAkAAPAAlAAQAAmAARAAnAASAAoAATAApAAUAAqAAVAArAAWAAsAAXAAtAAYAAuAAZAAvAAwAAxAAyAAzA%%A%sA%BA%$A%nA%CA%-A%(A%DA%;A%)A%EA%aA%0A%FA%bA%1A%GA%cA%2A%HA%dA%3A%IA%eA%4A%JA%fA%5A%KA%gA%6A%LA%hA%7A%MA%iA%8A%NA%jA%9A%OA%kA%PA%lA%QA%mA%RA%nA%SA%oA%TA%pA%UA%qA%VA%rA%WA%sA%XA%tA%YA%uA%ZA%vA%wA%xA%yA%zAs%AssAsBAs$AsnAsCAs-As(AsDAs;As)AsEAsaAs0AsFAsbAs1AsGAscAs2AsHAsdAs3AsIAseAs4AsJAsfA"

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

def num_string(x):
    ''' Returns an array of numbers from a string FIX THIS'''
    return [int(l) for l in x.split() if l.isdigit()]

def make_nasm(code):
    import os, time
    with open('/tmp/nasm.s', 'w') as outf:
        outf.write(code)
    if os.system('nasm /tmp/nasm.s') != 0:
        raise ValueError("nasm failed")
    return open('/tmp/nasm', 'rb').read()




