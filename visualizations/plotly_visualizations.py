import plotly.express as px
import pandas as pd

def create_plotly_charts():
    data = pd.read_csv('data/example_data.csv')

    # Interactive Bar Chart
    fig = px.bar(data, x='Category', y='Value', title='Interactive Bar Chart (Интерактивная столбчатая диаграмма)', color='Category')
    fig.write_html('outputs/plotly_Столбчатая_интерактивная.html')
    fig.show()

    # Interactive Line Plot
    fig = px.line(data, x='Category', y='Value', title='Interactive Line Plot (Интерактивный линейный график)', markers=True)
    fig.write_html('outputs/plotly_Интерактивный_линейный.html')
    fig.show()

    # График рассеяния
    # Создание DataFrame
    df = pd.DataFrame({
        "x": [1, 2, 3, 4],
        "y": [10, 20, 14, 23]
    })

    fig = px.scatter(df, x='x', y='y', title='График рассеяния')
    fig.write_html('outputs/plotly_График_рассеяния.html')
    fig.show()
