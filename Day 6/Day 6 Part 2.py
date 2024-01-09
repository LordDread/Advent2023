from functools import reduce
import operator

with open('input.txt') as input:
    contents = input.readlines()

#times = []
#record_distances = []


times = contents[0].rstrip().split(":")[1:]
times = times[0].lstrip().split(" ")

temp_times = ""
for time in times:
    if bool(time):
        temp_times += time
times = int(temp_times)
print(times)

record_distances = contents[1].split(" ")[1:]


temp_records = ""
for record in record_distances:
    if bool(record_distances):
        temp_records += record
record_distances = int(temp_records)
print(record_distances)

number_of_ways_to_win =[]

counter = 0
for hold_button_time in range(times):
    #print(hold_button_time)
    if hold_button_time * (times - hold_button_time) > record_distances:
        number_of_ways_to_win = (times + 1 - (counter * 2))
        break
    counter += 1

print(number_of_ways_to_win)

