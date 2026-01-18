import matplotlib.pyplot as plt 
import numpy as np 
data = np.random.randn(1000)  
plt.hist(data, bins=20, edgecolor='black', alpha=0.7) 
plt.xlabel('Values') 
plt.ylabel('Frequency') 
plt.title('Histogram Plot Example') 
plt.show()
