import numpy as np
import matplotlib.pyplot as plt

# Creating two empty Lists
timeList = []
azimutList = []
elevationList =[]

# Separting tuples into 2 lists (azimut and elevation)
for i in range (len(dataList)) :
    azimutList.append(dataList[i][0])
    elevationList.append(dataList[i][0])

# Creating a list base on hours, a point is created every 5 minutes
for m in range (24*12):
    timeList.append(m*5/60)


# plotting the points 
plt.plot(timeList, azimutList, label = "Azimut")
plt.plot(timeList, elevationList, label = "Hauteur")
  
# naming the x axis
plt.xlabel('Heure de la journée')
# naming the y axis
plt.ylabel('Degré de l\'angle')
  
# giving a title to my graph
plt.title('Evolution de l\'azimut et la hauteur au cours d\'une journée ')
  
# function to show the plot
plt.show()
