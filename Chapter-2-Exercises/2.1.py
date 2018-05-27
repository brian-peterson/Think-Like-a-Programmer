'''
Using the same rule as the shapes programs from earlier in the chapter (only
two output statements—one that outputs the hash mark and one that outputs
an end-of-line), write a program that produces the following shape:

########
 ######
  ####
   ##

'''
def main():
	space = 0
	for row in range(8,0,-2):
		print(space*' ' + row*'#')
		space += 1
		
main()
