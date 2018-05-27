
'''
Write a program that uses only two output statements, cout << "#" and cout << "\\n",
to produce a pattern of hash symbols shaped like a sideways triangle:

#
##
###
####
###
##
#

'''

def main():
	space = 0
	for row in range(0,8,1):
		if row > 0:
			print((4-(abs(4-row)))*'#')
			
main()