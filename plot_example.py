# ##pip install matplotlib
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,15,25,30,20]
# y=[10,5,10,5,10]

# user_inp=input("Enter item separated by space: ") # 1 2 3 4
# x=list(map(int,user_inp.split()))
# user_inp=input("Enter item separated by space: ") # 1 2 3 4
# y=list(map(int,user_inp.split()))

plt.plot(x,y)
plt.show()

plt.plot(x,y, marker='o',linestyle='--',color='red', label='My Line')
# linestyle supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Customaized line plot')
plt.legend()#Show a legend box on the plot with the text "My Line" representing that line.
plt.show()

# plotting------------------------------------------------>
import matplotlib.pyplot as plt
import numpy as np

xpoint= np.array([1,2,6,8])
ypoint= np.array([3,8,1,10])

plt.plot(xpoint,ypoint,"o",linestyle="-",color="g")
# plt.plot(
#     xpoint, ypoint,
#     color='purple',                # Line color
#     linestyle='--',                # Dashed line
#     linewidth=2.5,                 # Line thickness
#     marker='o',                    # Marker shape (circle)
#     markersize=10,                 # Marker size
#     markerfacecolor='yellow',      # Fill color of marker
#     markeredgecolor='black',       # Edge color of marker
#     markeredgewidth=2,             # Edge width of marker
#     drawstyle='steps-post',        # Step style line
#     alpha=0.8,                     # Transparency
#     label='My Line',               # Label for legend
#     zorder=2                       # Draw order
# )
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot with All Customizations')
plt.legend()
plt.grid(True)
plt.show()

## ----------------------------------------------------------------------------------------------------------------------------------------------------------
# # marker supported values are 'o' (circle), '.' (point), ',' (pixel), 'x' (x), '+' (plus), '^' (triangle up), 'v' (triangle down), '>' (triangle right), 
#      '<' (triangle left), 's' (square), 'p' (pentagon), '*' (star), 'h' (hexagon 1), 'H' (hexagon 2), 'D' (diamond), 'd' (thin diamond),
#        '|' (vertical line), '_' (horizontal line), 'None', '', or ' ' (no marker).

# # linestyle supported values are '-' (solid), '--' (dashed), '-.' (dash-dot), ':' (dotted), 'None', ' ', or '' (no line), 'solid', 'dashed', 'dashdot', 'dotted'.

# # color supported values are color names like 'red', 'blue', 'green', 'black', 'yellow', 'cyan', 'magenta', short codes like 'r', 'g', 'b', 'k', 'y', 'c', 'm', 'w',
#        hex codes like '#FF5733', or RGB tuples like (0.1, 0.5, 0.8).

# # drawstyle supported values are 'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'.
# # markerfacecolor (mfc) sets the fill color of the marker and accepts same values as color.
# # markeredgecolor (mec) sets the edge color of the marker and accepts same values as color.
# # markeredgewidth (mew) sets the thickness of the marker edge in float values like 1.0, 2.5, etc.
# # markersize (ms) sets the size of the marker in float values like 5, 10, etc.
# # linewidth (lw) sets the line thickness in float values like 2, 3.5, etc.
# # alpha controls transparency where 0 is fully transparent and 1 is fully opaque.
# # label is used to name the line for the legend, e.g., 'label="My Line"'.
# # zorder controls layer order — higher values appear on top.
# #------------------------------------------------------------------------------------------------------------------------------------------------------------------

# marker------------------------------------------->
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,15,25,30,20]

plt.plot(x, y, marker='o', label='circle')
plt.plot(x, y, marker='s', label='square')
plt.plot(x, y, marker='^', label='trinangle')
plt.plot(x, y, marker='*', label='star')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("basic marker type")
plt.legend()
plt.show()

# line-------------------------------->
import matplotlib.pyplot as plt


x=[1,2,3,4,5]
y=[10,15,20,25,30]
y1=[5,10,15,20,25]

plt.plot(x,y, label='line 1')
plt.plot(x,y1, label='line 2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('label plot with positioned legend')
plt.legend(loc='upper left', fontsize=12, frameon=False)
plt.show()

# grid and Plot---------------------------------------->
import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[10,15,20,25,30]


# plt.plot(x,y)
# plt.grid(color='red',linestyle='--', linewidth=2)
# plt.show()

plt.subplot(1,2,1) # 1 row, 2 columns, 1st plot -->(nrows, ncols, index)
plt.plot(x,y,'o',linestyle='solid')
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(x, [i**2 for i in y],'o',linestyle='solid')
plt.grid(True)
plt.show()
# *********************************************
import matplotlib.pyplot as plt

plt.subplot(2,2,1) # (nrows, ncols, index)
plt.plot([1,2,3],[4,5,6])
plt.title('plot1')

plt.subplot(2,2,2)
plt.plot([3,2,1],[6,5,4])
plt.title('plot2')

plt.subplot(2,2,3)
plt.plot([1,2,3],[4,5,6], color='red')
plt.title('red plot3')

plt.subplot(2,2,4)
plt.plot([3,2,1],[6,5,4], color='purple')
plt.title('purple plot4')

plt.show()
# scatter---------------------------------------------------->

import matplotlib.pyplot as plt

x=[2,4,5,7,8]
y=[10,15,20,25,30]

plt.scatter(x,y, color='red',marker='o',s=100, edgecolors='black')
plt.title('Customized Scatter Plot')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.show()

# Bar---------------------------------------------------------------->
import matplotlib.pyplot as plt

categories =['Categories A', 'Categories B', 'Categories C', 'Categories D']
values=[30,45,20,60]

plt.bar(categories,values, color=['orange','pink','skyblue','gray'],edgecolor='black')
plt.title("Bar Plot")
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

# Histogram------------------------------------------->
import matplotlib.pyplot as plt

data=[2,3,3,4,4,4,5,5,5,5,6,6,7,7,8]

plt.subplot(1,3,1)
plt.hist(data, bins=6, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('value')
plt.ylabel('frequency')
# plt.show()

# import numpy as np
# x=np.random.normal(170,10,250)
# plt.hist(x)
# plt.show()

exam_score=[65,75,80,86,90,95,98,92,100]
plt.subplot(1,2,2)
plt.hist(exam_score, bins=10, color='green', edgecolor='black')
plt.title('exam_score Histogram')
plt.xlabel('exam_score')
plt.ylabel('frequency')
plt.show()
