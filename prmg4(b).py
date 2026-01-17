import matplotlib.pyplot as plt  
x = [1, 2, 3, 4, 5] 
y = [10, 12, 5, 20, 7] 
plt.scatter(x, y, label='Data Points', color='blue', marker='o') 
plt.xlabel('X-Axis') 
plt.ylabel('Y-Axis') 
plt.title('Scatter Plot Example')  
plt.legend()  
plt.show()
