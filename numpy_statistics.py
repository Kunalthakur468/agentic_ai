import numpy as np
arr = np.array([1,2,3,4,5,6,6,7])

print(sum(arr)/len(arr))

mean = np.mean(arr)
print("mean is :",mean)

std_dev = np.std(arr)
print("standard devation is :",std_dev)

median = np.median(arr)
print("median is :",median)

variance = np.var(arr)
print("Variance is:",variance)
#Logical Operation on Array 
print(arr[(arr>3) & (arr <7)])
print(type(arr))
