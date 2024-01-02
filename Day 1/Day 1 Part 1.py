with open('input.txt') as input:
    contents = input.readlines()

sequence = []
for line in contents:
    temp_sequence = []
    for char in line:
        if char.isdigit():
            temp_sequence.append(char)
    sequence.append(int(temp_sequence[0]+temp_sequence[-1]))
#print(sequence)
print(sum(sequence))
