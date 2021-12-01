with open('input') as f:
    depths = [ int(depth) for depth in f.readlines() ]

increases = 0
previous_window = sum(depths[0:2])

for i in range(1, len(depths)-2):
    current_window = sum(depths[i:i+3])
    if current_window > previous_window:
        increases+=1
    previous_window = current_window

print(increases) 
    
