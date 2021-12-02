with open('input') as f:
    instructions = [ (instruction.split()[0], int(instruction.split()[1])) 
                     for instruction in f.readlines() ]

horizontal = 0
depth = 0

for instruction in instructions:
    command = instruction[0]
    distance = instruction[1]
	
    if command == "forward":
        horizontal += distance
    elif command == "down":
        depth += distance
    elif command == "up":
        depth -= distance

product = horizontal * depth
print(product)
