import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def create_seaborn_charts():
    data = pd.read_csv('data/example_data.csv')

    # Bar Plot
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Category', y='Value', data=data, palette='pastel')
    plt.title('Bar Chart (Seaborn)')
    plt.savefig('outputs/seaborn_bar_chart.png')
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Category', y='Value', data=data, color='blue', s=100)
    plt.title('Scatter Plot (Seaborn)')
    plt.savefig('outputs/seaborn_scatter_plot.png')
    plt.show()
