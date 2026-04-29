import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic info
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)

# Data cleaning
df = df.dropna(subset=['country', 'rating'])

# Count Movies vs TV Shows
type_counts = df['type'].value_counts()
print("\nContent Type Count:\n", type_counts)

# Plot
type_counts.plot(kind='bar', title='Movies vs TV Shows')
plt.show()

# Top countries
top_countries = df['country'].value_counts().head(10)
print("\nTop Countries:\n", top_countries)

top_countries.plot(kind='bar', title='Top 10 Countries')
plt.show()