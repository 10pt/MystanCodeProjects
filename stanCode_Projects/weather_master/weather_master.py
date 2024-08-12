"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100

def main():
	"""
	Shows maximum/minimum/average temperatures, and total cold days(<16).
	"""
	print("stanCode \"Weather Master 4.0\"!")
	n = int(input('Next Temperature: (or '+str(EXIT)+(' to quit)? ')))

	if n == EXIT:
		print('No temperatures were entered.')

	else:
		maximum = n
		minimum = n

		total = n
		day = 1
		if n < 16:
			cold = 1
		else:
			cold = 0
		while True:
			n = int(input('Next Temperature: (or '+str(EXIT)+(' to quit)? ')))

			if n == EXIT:
				average = total / day
				print(('Highest temperature = '+str(int(maximum))))
				print(('Lowest temperature = ')+str(int(minimum)))
				print(('Average = ')+str(average))
				print((str(cold)+' cold day(s)'))
				break
			else:

				day += 1
				total += n
				if n > maximum:
					maximum = n
				if n < minimum:
					minimum = n
				if n < 16:
					cold += 1



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
