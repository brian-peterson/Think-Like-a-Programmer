# -*- coding: utf-8 -*-

'''
2.6
If you’ve learned about binary numbers and how to convert from decimal
to binary and the reverse, try writing programs to do those conversions with
unlimited length numbers (but you can assume the numbers are small
enough to be stored in a standard C++ int).
'''
def  binaryToDecimal(n):
	decValue = 0
	base = 1

	while(n):
		lastDigit = n % 10
		n = n//10
		decValue += lastDigit*base
		base = base*2
	return decValue

num = input('enter a binary number to convert to decimal: ')
print(binaryToDecimal(num))
