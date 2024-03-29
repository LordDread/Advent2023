with open('input.txt') as input:
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

def read_map(input_number,dict_entry):
    for row in dict_entry:
        if input_number >= int(row[1]) and input_number <= int(row[1])+int(row[2]):
            difference = input_number - int(row[1])
            return int(row[0]) + difference
    return input_number


seeds = contents[0].rstrip().split(":")
seeds = seeds[1].rstrip().split()

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
    input = int(seed)
    for values in almanac.values():
        input = read_map(input,values)
    location_number.append(input)

print(location_number)
print(min(location_number))
