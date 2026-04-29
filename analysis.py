import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("\n--- NETFLIX DATA ANALYSIS ---\n")

# Dataset overview
print("Total Rows & Columns:", df.shape)
print("\nColumns:\n", df.columns)

# Data cleaning
df = df.dropna(subset=['country', 'rating'])

# Movies vs TV Shows
type_counts = df['type'].value_counts()
print("\nContent Type Distribution:\n", type_counts)

# Plot 1
plt.figure()
type_counts.plot(kind='bar')
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Top 10 countries
top_countries = df['country'].value_counts().head(10)
print("\nTop 10 Countries:\n", top_countries)

# Plot 2
plt.figure()
top_countries.plot(kind='bar')
plt.title("Top 10 Countries Producing Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.show()

# Content added over years
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

year_counts = df['year_added'].value_counts().sort_index()

print("\nContent Added Over Years:\n", year_counts.tail())

# Plot 3
plt.figure()
year_counts.plot()
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

print("\n--- ANALYSIS COMPLETE ---\n")
