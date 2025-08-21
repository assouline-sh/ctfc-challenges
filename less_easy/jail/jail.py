#!/usr/bin/env python3
blocklist = ["/","setattr","compile","os","import","_","breakpoint","exit","lambda","eval","exec","read","print","open","'","=","builtins","clear"]
#print("="*25)
#print(open(__file__).read())
print("="*60)
print("Welcome to jail! We'll let you out if you find the flag :)\n")
print("But be careful! Some commands are in a \"blocklist\"")
print("="*60)

while True:
	x = input('Enter command: ')
	for c in blocklist:
		if c in x:
			print("Blocklisted content detected! Exiting!")
			exit(0)
	try:
		exec(x)
	except NameError as e:
		print(e)

