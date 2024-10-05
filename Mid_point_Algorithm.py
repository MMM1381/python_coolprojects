

# F(p) = x2 + y2 – r2 
# if F(p)<0, the point is inside the circle
# F(p)=0, the point is on the perimeter
# F(p)>0, the point is outside the circle


def midPointCircleDraw(x_centre, y_centre, r):
	x = r
	y = 0
	print(f"initial points: x={x+x_centre}, y={y+y_centre}")
	# Initialising the value of P 
	P = 1 - r 

	while x > y:
		#by given pixel (x, y), the next pixel to be plotted is either (x, y+1) or (x-1, y+1).
		y += 1
		
		# Mid-point inside or on the perimeter
		if P <= 0: 
			P = P + 2*y + 1
		# Mid-point outside the perimeter 
		else:		 
			x -= 1
			P = P + 2*y - 2*x + 1


		# check if is finished
		if (x < y):
			break
		
		print(f"first octant: x={x+x_centre}, y={y+y_centre}")
		print(f"fourth octant: x={-x+x_centre}, y={y+y_centre}")
		print(f"eighth octant: x={x+x_centre}, y={-y+y_centre}")
		print(f"fifth octant: x={-x+x_centre}, y={-y+y_centre}")

		
		# If x==y we have reached the end point of our octant 
		if x != y:
			print(f"second octant: x={y+x_centre}, y={x+y_centre}")
			print(f"third octant: x={-y+x_centre}, y={x+y_centre}")
			print(f"seventh octant: x={y+x_centre}, y={-x+y_centre}")
			print(f"sixth octant: x={-y+x_centre}, y={-x+y_centre}")

							

# To draw a circle of radius 3 
# centered at (0, 0) 
midPointCircleDraw(0, 0, 3)

