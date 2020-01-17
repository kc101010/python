#		Factorial challenge from CoderByte
#		CoderByte Username: kc101010
#
# 		Contains minor changes to allow the program to correctly function and avoid error


def FirstFactorial(num):
	temp = num
	num * num
	
	for i in range(0, num - 2):
	
	 temp -= 1 
	 num *= temp 
		
		
	return num
	
	
print(FirstFactorial(int(input("Please enter a number:"))))