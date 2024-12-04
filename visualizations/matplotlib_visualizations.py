import matplotlib.pyplot as plt
import pandas as pd

def create_matplotlib_charts():
    data = pd.read_csv('data/example_data.csv')

    # Bar Chart
    plt.figure(figsize=(8, 5))
    plt.bar(data['Category'], data['Value'], color='skyblue')
    plt.title('Bar Chart (Matplotlib)')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.savefig('outputs/matplotlib_bar_chart.png')
    plt.show()

    # Line Plot
    plt.figure(figsize=(8, 5))
    plt.plot(data['Category'], data['Value'], marker='o', linestyle='-', color='green')
    plt.title('Line Plot (Matplotlib)')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.savefig('outputs/matplotlib_line_plot.png')
    plt.show()
