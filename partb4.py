import pandas as pd
import matplotlib.pyplot as plt

data = {'Math_Score': [85, 90, 88, 78, 92],'English_Score': [80, 88, 85, 92, 89]}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 6))
plt.scatter(df['Math_Score'], df['English_Score'], color='green')
plt.xlabel('Math Score')
plt.ylabel('English Score')
plt.title('Scatter Plot of Exam Scores')
plt.grid(True)
plt.show()
