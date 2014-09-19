'''http://shell-storm.org/blog/A-binary-analysis-count-me-if-you-can/'''
import sys,subprocess
import commands

if __name__ == "__main__":
    pwd  = ""
    base = 0x2e
    off  = 0x00
    sav  = 0x00
    while pwd.find("Good Password") == -1:
        base += 1
	if chr(base) == '<' or chr(base) == ">" or chr(base) == ";":
		continue
        pwd = pwd[:off] + chr(base) + pwd[off+1:];

	cmd = "/home/blankwall/pin/pin -t /home/blankwall/pin/source/tools/ManualExamples/obj-ia32/inscount1.so  -- /home/blankwall/Desktop/a.out <<< %s; cat inscount.out" %(pwd)


	p = subprocess.Popen(["/bin/bash", "-c",cmd], stdout=subprocess.PIPE)
	out = p.communicate()
	
	print out
	if "YES" in out[0]:
		print pwd
		break
	try:
		x = [int(s) for s in out[0].split() if s.isdigit()][0]
	except:
		continue

	res = x
        print "insert('%s' INS: %d) ins" %(pwd, res)
	print res-sav
	if base > 125:
		break

        if sav == 0x00:
            sav = res
        if res - sav > 15000:
            off += 1
            if off >= len(pwd):
		pwd += " "
#                break
            base = 0x2d
            sav = 0
        sav = res
   
    print "The password is %s" %(pwd)
    sys.exit(0)
