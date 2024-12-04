import plotly.express as px
import pandas as pd

def create_plotly_charts():
    data = pd.read_csv('data/example_data.csv')

    # Interactive Bar Chart
    fig = px.bar(data, x='Category', y='Value', title='Bar Chart (Plotly)', color='Category')
    fig.write_html('outputs/plotly_bar_chart.html')
    fig.show()

    # Interactive Line Plot
    fig = px.line(data, x='Category', y='Value', title='Line Plot (Plotly)', markers=True)
    fig.write_html('outputs/plotly_line_plot.html')
    fig.show()
