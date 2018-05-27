'''
Using the same rule as the shapes programs from earlier in the chapter (only
two output statements—one that outputs the hash mark and one that outputs
an end-of-line), write a program that produces the following shape:

   ##
  ####
 ######
########
########
 ######
  ####
   ##
'''

# t = top half
# b = bottom half
def main():
	tspace = 3
	bspace = 0
	for trow in range(0,10,2):					
		if trow > 0:
			print(tspace*' ' + '#'* trow)
			tspace -= 1
			
	for brow in range(8,0,-2):
		print(bspace*' ' + '#' * brow)
		bspace += 1

main()