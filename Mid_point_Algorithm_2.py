import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
# F(p) = x2 + y2 – r2 
# if F(p)<0, the point is inside the circle
# F(p)=0, the point is on the perimeter
# F(p)>0, the point is outside the circle


def midPointCircleDraw(x_centre, y_centre, r):
	x = r
	y = -1
	print(f"initial points: x={x+x_centre}, y={y+y_centre}")
	# Initialising the value of P 
	P = 1 - r
	octant1=[]
	octant2=[]
	octant3=[]
	octant4=[]
	octant5=[]
	octant6=[]
	octant7=[]
	octant8=[]

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
		
		octant1.append([x+x_centre,y+y_centre])
		octant4.append([-x+x_centre,y+y_centre])
		octant8.append([x+x_centre,-y+y_centre])
		octant5.append([-x+x_centre,-y+y_centre])

		
		# If x==y we have reached the end point of our octant 
		if x != y:
			octant2.append([y+x_centre,x+y_centre])
			octant3.append([-y+x_centre,x+y_centre])
			octant7.append([y+x_centre,-x+y_centre])
			octant6.append([-y+x_centre,-x+y_centre])

	return [octant1,octant2[::-1],octant3,octant4[::-1],octant5,octant6[::-1],octant7,octant8[::-1]]
	


# To draw a circle of radius 3 
# centered at (0, 0) 
plt.axis([0,20,0,20])
octants = []
for a in range(1,11):
	for i in midPointCircleDraw(0, 0, a):
		octants = octants  + [j for j in i if not j in octants]
print(octants)

x = []
y = []


def draw_graph(i):
	x.append(octants[i][0])
	y.append(octants[i][1])

	plt.cla()
	plt.scatter(x,y)

anima = animation.FuncAnimation(plt.gcf(), draw_graph,frames=len(octants) ,interval=100)
plt.show()