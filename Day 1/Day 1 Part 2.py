with open('input.txt') as input:
    contents = input.readlines()

numbers = ['zero','one','two', 'three','four','five','six','seven','eight','nine']
sequence = []

for line in contents:
    temp_sequence = []
    digit_test = ''
    #print(line)
    for char in line:
        #print("char: "+char)
        if not char.isdigit():
            digit_test = digit_test + char
            #print("digit: "+digit_test)
            if any(ele in digit_test for ele in numbers):
               #print(digit_test)
               check_digit = [index for (index, item) in enumerate(numbers) if item in digit_test]
               #print("Check"+str(check_digit))
               temp_sequence.append(str(check_digit[0]))
               digit_test = str(digit_test[-1])
               #print(digit_test)
        if char.isdigit():
            temp_sequence.append(char)
            digit_test = ''
            #print("["+char+"]")
    #print(temp_sequence)
    sequence.append(int(temp_sequence[0] + temp_sequence[-1]))
    #print(sequence)
print(sum(sequence))
