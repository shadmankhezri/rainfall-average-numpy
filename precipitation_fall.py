## Import the necessary libraries
import numpy as np
import codecs

## files path
PATH_2019 = "C:/Users/se7enpc.ir/Desktop/HW numpy/precipitation_fall_2019.txt"
PATH_2020 = "C:/Users/se7enpc.ir/Desktop/HW numpy/precipitation_fall_2020.txt"
PATH_2021 = "C:/Users/se7enpc.ir/Desktop/HW numpy/precipitation_fall_2021.txt"
## open files
data_2019 = codecs.open(PATH_2019, encoding = 'cp1252')
data_2020 = codecs.open(PATH_2020, encoding = 'cp1252')
data_2021 = codecs.open(PATH_2021, encoding = 'cp1252')
## load and reshape files
arr_2019 = np.loadtxt(data_2019).reshape(3,5)
arr_2020 = np.loadtxt(data_2020).reshape(3,5)
arr_2021 = np.loadtxt(data_2021).reshape(3,5)
## print arraies
print(100*'*')
print("Display information about the amount of rain in autumn 2019:")
print(arr_2019)
print(25*'*')
print("Display information about the amount of rain in autumn 2020:")
print(arr_2020)
print(25*'*')
print("Display information about the amount of rain in autumn 2021:")
print(arr_2021)
print(100*'*')

## print average of arries and add to list
lst = []
print("Showing the average rainfall for the three months of autumn 2019:")
sum_2019 = arr_2019.sum(axis=1, dtype='float')/5
lst.append(sum_2019)
print(sum_2019)
print(25*'*')
print("Showing the average rainfall for the three months of autumn 2020:")
sum_2020 = arr_2020.sum(axis=1, dtype='float')/5
lst.append(sum_2020)
print(sum_2020)
print(25*'*')
print("Showing the average rainfall for the three months of autumn 2021:")
sum_2021 = arr_2021.sum(axis=1, dtype='float')/5
lst.append(sum_2021)
print(sum_2021)

## Print array with average rainfall
print(100*'*')
print("General display of average precipitation:\nThe rows represent the year and the columns represent the month\n")
avg_rain = np.array(lst)
print(avg_rain)
print(100*'*')
print("Average maximum rainfall")
## Find the maximum amount of precipitation
print(avg_rain.max())
x = np.unravel_index(np.argmax(avg_rain , axis=None), avg_rain.shape)
print(x)
## The highest amount of precipitation is related to the third month of 2021
data_2019.close()