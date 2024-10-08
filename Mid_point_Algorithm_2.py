import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation

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
	first_octant=[]
	second_octant=[]
	third_octant=[]
	fourth_octant=[]
	fifth_octant=[]
	sixth_octant=[]
	seventh_octant=[]
	eighth_octant=[]

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


		# check if  it is finished
		if (x < y):
			break
		
		first_octant.append([x+x_centre,y+y_centre])
		fourth_octant.append([-x+x_centre,y+y_centre])
		eighth_octant.append([x+x_centre,-y+y_centre])
		fifth_octant.append([-x+x_centre,-y+y_centre])

		
		# If x==y we have reached the end point of our octant 
		if x != y:
			second_octant.append([y+x_centre,x+y_centre])
			third_octant.append([-y+x_centre,x+y_centre])
			seventh_octant.append([y+x_centre,-x+y_centre])
			sixth_octant.append([-y+x_centre,-x+y_centre])

	return first_octant
	
							

# To draw a circle of radius 3 
# centered at (0, 0) 
f = midPointCircleDraw(0, 0, 3)
print(f)

count = 0
x = []
y = []
_x=[]
_y=[]
# as we impleament in realtime_drawing
def draw_graph(i,x,y):
    global count
    count += 1
	if x!=None:
    	_x.append(count)
    _y.append([y[])

    plt.cla()
    plt.plot(x,y)

anima = animation.FuncAnimation(plt.gcf(), draw_graph, interval=1500)
plt.show()