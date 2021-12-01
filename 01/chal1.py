with open('input') as f:
    depths = [ int(depth) for depth in f.readlines() ]

increases = 0

for i in range(0, len(depths)-1):
   if depths[i+1] > depths[i]:
       increases+=1
	   
print(increases)
	   
    
