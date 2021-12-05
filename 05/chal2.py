import numpy as np

class Grid:
        
	def __init__(self, shape):
		self.grid = np.zeros(shape, dtype = np.int64)
    
	def update_grid(self, coords1, coords2):
		x1 = int(coords1[0])
		y1 = int(coords1[1])
		x2 = int(coords2[0])
		y2 = int(coords2[1])
		
		if x1 == x2:
			ymax = max(y1, y2)
			ymin = min(y1, y2)
			self.grid[ymin:ymax+1, x1] += 1
		elif y1 == y2:
			xmax = max(x1, x2)
			xmin = min(x1, x2)
			self.grid[y1, xmin:xmax+1] += 1
		else:
			xdiff = x2-x1
			xstep = int(xdiff/np.absolute(xdiff))
			ydiff = y2-y1
			ystep = int(ydiff/np.absolute(ydiff))

			x = np.arange(x1, x2+xstep, step = xstep)
			y = np.arange(y1, y2+ystep, step = ystep)
			
			for xnew, ynew in np.transpose(np.vstack([x,y])):
				self.grid[ynew, xnew] += 1
			
def main():
	x = Grid((1000,1000))

	with open('input', 'r') as f:
		lines = [line.strip().split(" -> ") for line in f.readlines() ]
	f.close() 		
	coords = [ [start.split(","), end.split(",")]
			   for start, end in lines ]
	
	for coord1, coord2 in coords:
		x.update_grid(coord1, coord2)
		
	print((x.grid >= 2).sum())
main()

