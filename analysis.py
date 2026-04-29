"""
Netflix Data Analysis Project
Author: Anshuman Sikdar
Description: Exploratory Data Analysis on Netflix dataset using Python
"""

import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("❌ File not found. Please check the file path.")
        exit()


def clean_data(df):
    # Drop missing values
    df = df.dropna(subset=['country', 'rating'])

    # Convert date column
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Extract year
    df['year_added'] = df['date_added'].dt.year

    return df


def analyze_content_type(df):
    type_counts = df['type'].value_counts()

    print("\n📊 Content Type Distribution:")
    print(type_counts.to_string())

    plt.figure()
    type_counts.plot(kind='bar')
    plt.title("Movies vs TV Shows on Netflix")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


def analyze_top_countries(df):
    top_countries = df['country'].value_counts().head(10)

    print("\n🌍 Top 10 Countries Producing Content:")
    print(top_countries.to_string())

    plt.figure()
    top_countries.plot(kind='bar')
    plt.title("Top 10 Countries Producing Content")
    plt.xlabel("Country")
    plt.ylabel("Number of Titles")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def analyze_yearly_trend(df):
    year_counts = df['year_added'].value_counts().sort_index()

    print("\n📈 Content Added Over Years:")
    print(year_counts.tail().to_string())

    plt.figure()
    year_counts.plot()
    plt.title("Content Added Over Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.tight_layout()
    plt.show()


def main():
    print("\n========== NETFLIX DATA ANALYSIS ==========\n")

    # Load data
    df = load_data("netflix_titles.csv")

    # Overview
    print("📁 Dataset Shape:", df.shape)
    print("\n📌 Columns:\n", df.columns)

    # Clean data
    df = clean_data(df)

    # Analysis
    analyze_content_type(df)
    analyze_top_countries(df)
    analyze_yearly_trend(df)

    print("\n========== ANALYSIS COMPLETE ==========\n")


if __name__ == "__main__":
    main()
