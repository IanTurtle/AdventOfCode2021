with open('input') as f:
    instructions = [ (instruction.split()[0], int(instruction.split()[1])) 
                     for instruction in f.readlines() ]

aim = 0
depth = 0
horizontal = 0

for instruction in instructions:
    command = instruction[0]
    distance = instruction[1]
	
    if command == "down":
        aim += distance
    elif command == "up":
        aim -= distance
    elif command == "forward":
        horizontal += distance
        depth += (aim * distance)

product = horizontal * depth
print(product)
