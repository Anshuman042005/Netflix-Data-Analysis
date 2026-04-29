import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    return pd.read_csv(file_path)


def clean_data(df):
    df = df.dropna(subset=['country', 'rating'])
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    return df


def analyze_content_type(df):
    type_counts = df['type'].value_counts()
    print("\nContent Type Distribution:\n", type_counts)

    plt.figure()
    type_counts.plot(kind='bar')
    plt.title("Movies vs TV Shows on Netflix")
    plt.xlabel("Type")
    plt.ylabel("Count")
    plt.show()


def analyze_top_countries(df):
    top_countries = df['country'].value_counts().head(10)
    print("\nTop 10 Countries:\n", top_countries)

    plt.figure()
    top_countries.plot(kind='bar')
    plt.title("Top 10 Countries Producing Content")
    plt.xlabel("Country")
    plt.ylabel("Number of Titles")
    plt.show()


def analyze_yearly_trend(df):
    year_counts = df['year_added'].value_counts().sort_index()
    print("\nContent Added Over Years:\n", year_counts.tail())

    plt.figure()
    year_counts.plot()
    plt.title("Content Added Over Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.show()


def main():
    print("\n--- NETFLIX DATA ANALYSIS ---\n")

    df = load_data("netflix_titles.csv")

    print("Dataset Shape:", df.shape)
    print("\nColumns:\n", df.columns)

    df = clean_data(df)

    analyze_content_type(df)
    analyze_top_countries(df)
    analyze_yearly_trend(df)

    print("\n--- ANALYSIS COMPLETE ---\n")


if __name__ == "__main__":
    main()
