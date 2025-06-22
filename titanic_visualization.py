import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("titanic.csv")

# Visualization 1 - Survival Count
sns.countplot(data=df, x='Survived')
plt.title("Survival Count")
plt.show()

# Visualization 2 - Age vs Class
sns.boxplot(data=df, x='Pclass', y='Age')
plt.title("Passenger Class vs Age")
plt.show()
