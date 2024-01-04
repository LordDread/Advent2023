with open('input.test.txt') as input:
    contents = input.readlines()

almanac = {
    "seed_to_soil_map" : [],
    "soil_to_fertilizer_map" : [],
    "fertilizer_to_water_map" : [],
    "water_to_light_map" : [],
    "light_to_temperature_map" : [],
    "temperature_to_humidity_map" : [],
    "humidity_to_location_map" : []
}

def turn_page(page):
    switch = {
        "seed-to-soil map:": "seed_to_soil_map",
        "soil-to-fertilizer map:" : "soil_to_fertilizer_map",
        "fertilizer-to-water map:" : "fertilizer_to_water_map",
        "water-to-light map:" : "water_to_light_map",
        "light-to-temperature map:" : "light_to_temperature_map",
        "temperature-to-humidity map:" : "temperature_to_humidity_map",
        "humidity-to-location map:" : "humidity_to_location_map"
    }
    test = switch.get(page)
    if test is not None:
        return test

def read_map(input_number, dict_entry):
    for row in dict_entry:
        if input_number >= int(row[1]) and input_number <= int(row[1])+int(row[2]):
            difference = input_number - int(row[1])
            return int(row[0]) + difference
    return input_number

seeds_range_list = []
seeds = contents[0].rstrip().split(":")
seeds = seeds[1].rstrip().split()


for each, seed in enumerate(seeds):
    #print(each % 2)
    if each % 2 == 0:
        start_seed = seed
        continue
    premade_list = ["x"] * (int(start_seed) * int(seed))
    #print(f"ye{start_seed}")
    #seeds_range_list.append(list(range(int(start_seed), int(start_seed) + int(seed))))
    counter = 0
    for s in range(int(start_seed), int(start_seed) + int(seed)):
        #print(s)
        if s in seeds_range_list:
            print("found in list")
            counter += 1
            continue
        premade_list[counter] = s
        counter += 1
    seeds_range_list.extend(premade_list)

seeds = seeds_range_list
#print(f"seeds: {seeds}")



for line in contents[1:]:
    line = line.rstrip()
    if line == "":
        continue
    if turn_page(line) is not None:
        almanac_page = turn_page((line))
    else:
        almanac[almanac_page].append(line.rstrip().split())


location_number = []

for seed in seeds:
    if seed == "x":
        break
    input = int(seed)
    for values in almanac.values():
        input = read_map(input,values)
    location_number.append(input)

print(location_number)
print(min(location_number))

