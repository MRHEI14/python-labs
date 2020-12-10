'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''
miles = 10
kilometer = miles * 1.6
minutes_to_hour = 30 / 60
seconds_to_hour = 30 / 3600
total_hour = minutes_to_hour + seconds_to_hour
speed = kilometer / total_hour
print(speed)
