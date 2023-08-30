import pandas as pd
import plotly.graph_objects as go


color_scale = {
    'White': 'rgb(255, 255, 255)',  # White
    'Light Green': 'rgb(173, 255, 47)',  # Light green
    'One level above light green': 'rgb(0, 255, 0)',  # Light green
    'Two levels above light green': 'rgb(0, 128, 0)',  # Light green
    'Two levels below dark green': 'rgb(0, 32, 0)',  # Dark green
    'One level below dark green': 'rgb(0, 100, 0)',  # Dark green
    'Dark Green': 'rgb(0, 64, 0)'  # Darkest green
}


df = pd.read_excel(r'C:\Users\VenkataHarish B-3270\PycharmProjects\strings1.py\heatmap_data.xlsx')

df['Color'] = df['colors'].map(color_scale)


fig = go.Figure(go.Treemap(
    labels=df.apply(lambda row: f'{row["Languages"]} ({row["size"]})', axis=1),
    parents=['' for _ in df['Languages']],
    values=df['size'],
    customdata=df['Color'],
    hovertemplate='<b>Area:</b> %{label}<br><b>Team Size:</b> %{value}<br><b>Expertise:</b> %{customdata}',
    marker=dict(
        colorscale=['white', 'rgb(173, 255, 47)', 'rgb(0, 255, 0)', 'rgb(0, 128, 0)', 'rgb(0, 100, 0)', 'rgb(0, 64, 0)', 'rgb(0, 32, 0)'],
    ),
))


fig.update_layout(
    title='Team Expertise Treemap',
    template='plotly',
    treemapcolorway=['rgb(255, 255, 255)']
)


fig.show()