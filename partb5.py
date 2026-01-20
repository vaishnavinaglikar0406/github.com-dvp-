import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
 'Department': ['HR', 'IT', 'Finance', 'Sales', 'Marketing'],
 'Salary': [50000, 60000, 75000, 70000, 55000],
}

df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.boxplot(x='Department', y='Salary', data=df, palette='Set2')
plt.title('Salary Distribution Across Departments')
plt.show()
