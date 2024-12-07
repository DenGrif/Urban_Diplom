from visualizations.matplotlib_visualizations import create_matplotlib_charts
from visualizations.seaborn_visualizations import create_seaborn_charts
from visualizations.plotly_visualizations import create_plotly_charts

if __name__ == "__main__":
    print("Создаем визуализации с Matplotlib...")
    create_matplotlib_charts()

    print("Создаем визуализации с Seaborn...")
    create_seaborn_charts()
    
    print("Создаем визуализации с Plotly...")
    create_plotly_charts()
