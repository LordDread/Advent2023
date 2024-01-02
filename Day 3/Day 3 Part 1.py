with open('input.txt') as input:
    contents = input.readlines()

def test_for_symbol(test):
    #print(f"testing:{test}")
    if test != '.' and not test.isdigit():
        return True
    else:
        return False

def check_for_symbol(source,x,y,length):
    #print(f"x:{x} y:{y} Len:{length}")

    #--------------above check--------------
    if y > 0:
        exception_handle_start = 1
        exception_handle_end = 1
        if x <= 0:
            exception_handle_start = 0
        if x+length >= len(source[y].rstrip()) - 1:
            exception_handle_end = 0
        for x_count in source[y - 1][x - exception_handle_start:x + length + exception_handle_end]:
            if test_for_symbol(x_count):
                #print(x_count)
                return True

    #-----------Before check------------
    if x > 0 :
        #print(f"before test:{source[y][x - 1]}")
        if test_for_symbol(source[y][x - 1]):
            #print(source[y][x - 1])
            return True

    # -----------After check------------
    if x + length - 1 < len(source[y].rstrip()) - 1:
        #print("after test")
        if test_for_symbol(source[y][x + length]):
            #print(source[y][x + length])
            return True

    #------------check below----------
    if y < len(source)-1:
        #print(f"x-1 = {x - 1} x+len = {x + length}")
        #print("below:")
        exception_handle_start = 1
        exception_handle_end = 1
        if x <= 0:
            exception_handle_start = 0
        #print(len(source[y])-1)
        if x+length >= len(source[y].rstrip())-1:
            exception_handle_end = 0
        for x_count in source[y + 1][x - exception_handle_start:x + length + exception_handle_end]:
            #print(f"testing:{x_count}")
            if test_for_symbol(x_count):
                #print(x_count)
                return True
    return False



sum_part_numbers = 0
for y_coordinate, line in enumerate(contents):
    #print(f"-------------------{y_coordinate}")
    part_number = ''
    for x_coordinate, char in enumerate(line.rstrip()):
        if char.isdigit():
            part_number= part_number+char
        if len(part_number) > 0 and (not char.isdigit() or x_coordinate >= len(line.rstrip())-1):
            #print(part_number)
            #print(y_coordinate)
            #print(x_coordinate)
            if x_coordinate == len(line.rstrip()) - 1 and char.isdigit():
                x_coordinate += 1
            #print(f"test: x:{x_coordinate} y:{y_coordinate} Len:{len(part_number)}")
            if check_for_symbol(contents,x_coordinate - len(part_number),y_coordinate,len(part_number)):
                #print(part_number)
                sum_part_numbers += int(part_number)
            part_number=''
print(sum_part_numbers)
