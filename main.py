import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv('pink_morsels_sales.csv')

df = df.sort_values(by='date')

fig = px.line(df, x='date', y='sales', title='Sales Data Pink Morsels')
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales',
    xaxis=dict(
        tickformat='%Y-%m-%d',  # Format date on x-axis
        title_text='Date'
    ),
    yaxis=dict(
        title_text='Sales'
    )
)

# Initialize the Dash app
app = Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Sales Data Pink Morsels Visualizer"),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)