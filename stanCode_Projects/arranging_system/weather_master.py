"""
File: weather_master.py
Name:Joanne
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
	This program can screen out the highest and lowest temperature
	from all the data you input and calculate the average of the
	temperatures and also shows how many days the temperature are
	lower than 16 degrees Celsius.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature: (or '+str(EXIT)+' to quit)? '))
	cold_day = 0
	days = 1
	# to calculate the average
	if data == EXIT:
		print('No temperatures were entered.')
	# avoid the situation if there's no data input
	else:
		maximum = data
		minimum = data
		plus = data
		average = plus / days
		if data < 16:
			cold_day += 1
	# still can compute if there's only one data input
		while True:
			data = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if data == EXIT:
				break
			# end the loop
			else:
				days += 1
				# make sure the divisor is correct
				plus = plus + data
				# to sum up all the data
				average = plus / days
				if data > maximum:
					maximum = data
				elif data < minimum:
					minimum = data
				if data < 16:
					cold_day += 1
		print('Highest temperature = '+str(maximum))
		print('Lowest temperature = '+str(minimum))
		print('Average = '+str(average))
		print(str(cold_day)+' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
