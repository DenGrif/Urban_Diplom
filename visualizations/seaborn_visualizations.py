import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def create_seaborn_charts():
    data = pd.read_csv('data/example_data.csv')

    # Bar Plot – столбчатая диаграмма
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Category', y='Value', data=data, palette='pastel')
    plt.title('Bar Plot – столбчатая диаграмма')
    plt.savefig('outputs/seaborn_Столбчатая диаграмма.png')
    plt.show()

    # Точечный график (Scatter Plot)
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Category', y='Value', data=data, color='blue', s=100)
    plt.title('Точечный график (Scatter Plot)')
    plt.savefig('outputs/seaborn_Точечный_график.png')
    plt.show()

    # Тепловая карта
    # Создание данных
    data = np.random.randn(10, 12)

    sns.heatmap(data, annot=True)
    plt.title('Тепловая карта')
    plt.savefig('outputs/seaborn_Тепловая_карта.png')
    plt.show()