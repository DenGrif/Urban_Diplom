import matplotlib.pyplot as plt
import pandas as pd


def create_matplotlib_charts():
    data = pd.read_csv('data/example_data.csv')

    # Bar Chart – столбчатая диаграмма
    plt.figure(figsize=(8, 5))
    plt.bar(data['Category'], data['Value'], color='skyblue')
    plt.title('Bar Chart – столбчатая диаграмма (Matplotlib)')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.savefig('outputs/matplotlib_столбчатая диаграмма.png')
    plt.show()

    # Line Plot – линейный график
    plt.figure(figsize=(8, 5))
    plt.plot(data['Category'], data['Value'], marker='o', linestyle='-', color='green')
    plt.title('Line Plot – линейный график (Matplotlib)')
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.savefig('outputs/matplotlib_линейный_график.png')
    plt.show()

    # Круговая диаграмма

    # Данные
    slices = [7, 2, 2, 13]
    activities = ['sleeping', 'eating', 'working', 'playing']
    colors = ['b', 'g', 'r', 'c']

    plt.pie(slices,
            labels=activities,
            colors=colors,
            startangle=90,
            shadow=True,
            explode=(0, 0.1, 0, 0),
            autopct='%1.1f%%')

    plt.title('Круговая диаграмма')
    plt.savefig('outputs/matplotlib_Круговая_диаграмма.png')
    plt.show()

# print(create_matplotlib_charts())
