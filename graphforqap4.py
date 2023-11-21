#make a graph plotting monthly sales total over a year. 
#author. nkm
#date. november. 21,2023

import matplotlib.pyplot as plt

xaxisMonths = ["Jan.", "Feb.", "Mar.", "Apr.","May.", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
yaxisSales = [1234461, 2345675, 4567686, 6788941, 4321111, 9807333, 6868641, 5757691, 6969662, 8989898, 0,0 ]

plt.plot(xaxisMonths,yaxisSales)

plt.xlabel("MONTHS OF THE YEAR")
plt.ylabel("TOTAL MONTHLY SALES")
plt.title("A DESPERATE ATTEMPT AT BONUS POINTS GRAPH")

plt.show()

