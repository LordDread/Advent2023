from functools import reduce
import operator

with open('input.txt') as input:
    contents = input.readlines()

#times = []
#record_distances = []


times = contents[0].rstrip().split(":")[1:]
times = times[0].lstrip().split(" ")
times = [number for number in times if number != ""]

print(times)

record_distances = contents[1].split(" ")[1:]
record_distances = [number for number in record_distances if number != ""]

print(record_distances)

number_of_ways_to_win =[]

for each, time in enumerate(times):
    time = int(time)
    counter = 0
    for hold_button_time in range(time):
        #print(hold_button_time)
        if hold_button_time * (time - hold_button_time) > int(record_distances[each]):
            number_of_ways_to_win.append(time + 1 - (counter * 2))
            break
        counter += 1

###### Reduces used to apply a function to a sequence of values ######
print(reduce(operator.mul, number_of_ways_to_win))

