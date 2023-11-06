#import visualisation library 
import matplotlib.pyplot as plt
  
#x and y axis values
x = [1,2,3]
y = [4,5,6]
  
#plotting the points 
plt.plot(x, y)
  
#naming axes
plt.xlabel('x axis')

plt.ylabel('y axis')
  
#giving a title to my graph
plt.title('First Graph')
  
# function to show the plot
plt.show()
