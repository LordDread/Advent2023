with open('input.txt') as input:
    contents = input.readlines()

def find_start_of_digits(source, x):
    if x ==0:
        return x
    if source[x-1].isdigit():
        reverse_seek = x - 1
        while source[reverse_seek].isdigit():
            #print(f"Reverse Seeking: {source[reverse_seek]}")
            reverse_seek -= 1
        reverse_seek += 1
        return reverse_seek
    else:
        return x

def part_reader(source,rev_seek, x,):
    #print(f"x:{x} rev_seek:{rev_seek}")
    parts_list = []
    part_number = ""
    for x_coord , digit in enumerate(source[rev_seek:]):
        #print(f"x coord: {x_coord}")
        #print(f"testing: {digit}")
        if digit.isdigit():
            part_number += digit
        elif part_number != "":
            parts_list.append(part_number)
            part_number = ""
        #print(f"x_coord: {x_coord}  {not digit.isdigit()} :: {x_coord >= x - rev_seek + 1}")
        if (not digit.isdigit()) and x_coord >= x - rev_seek + 1:
            #print(f"reached end with: {digit} at {x_coord}")
            break
    if part_number != "":
        parts_list.append(part_number)
    #print(f"list:{parts_list}")
    return parts_list

def look_for_numbers(x,y):
    #print(f"x:{x} y:{y} Len:{length}")
    #print(f"x in number search:{x}")
    parts_list = []
    gear_ratio = 0
    #--------------above check--------------
    if y > 0:
        test = part_reader(contents[y - 1].rstrip(),find_start_of_digits(contents[y - 1].rstrip(),x),x)
        #print(test)
        if bool(test):
            for each in test:
                parts_list.append(each)
        #print("done testing above")
    #-----------Before check------------
    if x > 0 :
        test =part_reader(contents[y].rstrip(), find_start_of_digits(contents[y].rstrip(),x),x)
        #print(test)
        if bool(test):
            for each in test:
                parts_list.append(each)
        #print("done testing before/after")
    #------------check below----------
    if y < len(contents)-1:
        test = part_reader(contents[y + 1].rstrip(),find_start_of_digits(contents[y + 1].rstrip(),x), x)
        #print(test)
        if bool(test):
            for each in test:
                parts_list.append(each)
        #print("done testing below")
    #print(f"found: {parts_list}")
    if len(parts_list) != 2:
        return 0
    else:
        gear_ratio = int(parts_list[0]) * int(parts_list[1])
        #print(f"adding: {parts_list}")
    return gear_ratio

sum_part_numbers = 0
for y_coordinate, line in enumerate(contents):
    #print(f"-------------------{y_coordinate}")
    part_number = ""
    for x_coordinate, char in enumerate(line.rstrip()):
        #print(f"char: {char}")
        if char == "*":
            #print(f"x in iterator: {x_coordinate}")
            sum_part_numbers += look_for_numbers(x_coordinate, y_coordinate)

#print(f"looking for: {(456*111)+(234*789)+(213*768)+(888*111)+(24*785)} ")
print(sum_part_numbers)
