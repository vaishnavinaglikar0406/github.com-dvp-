import matplotlib.pyplot as plt  
x = [1, 2, 3, 4, 5] 
y = [2, 4, 6, 8, 10]  
plt.plot(x, y, marker='o', color='blue', linestyle='--', linewidth=2, 
markersize=8, label='Data Points') 
plt.xlabel('X-Axis') 
plt.ylabel('Y-Axis') 
plt.title('Linear Plot with Line Formatting')  
plt.legend() 
plt.grid() 
