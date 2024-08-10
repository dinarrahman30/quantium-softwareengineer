import pandas as pd
from dash import Dash, html, dcc, Output, Input
import plotly.express as px

# Load and prepare dataset
data = pd.read_csv('pink_morsels_sales.csv')
data = data.sort_values(by='date')

# Define color scheme
colors = {
    "primary": "#E6AAE8",
    "secondary": "#E60CBE",
    "tertiary": "#FA9FE8",
    "font": "#522A61"
}

# Initialize the Dash app
app = Dash(__name__)


# Define the callback to update the graph based on region selection
@app.callback(
    Output('graph', 'figure'),
    [Input('region-pick', 'value')]
)
def update_graph(region):
    # Filter data based on selected region
    filtered_data = data if region == "all" else data[data["region"] == region]

    # Create the line chart
    fig = px.line(filtered_data, x='date', y='sales', title='Sales Data Pink Morsels')
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales',
        xaxis=dict(tickformat='%Y-%m-%d'),
        plot_bgcolor=colors["tertiary"],
        paper_bgcolor=colors["primary"],
        font_color=colors["font"]
    )
    return fig


region_picker = dcc.RadioItems(
    id="region-pick",
    options=[{"label": region.capitalize(), "value": region} for region in ["north", "east", "south", "west", "all"]],
    value="north",
    inline=True,
    style={"font-size": "100%"}
)

graphs = dcc.Graph(
    id='graph',
    style={'width': '80%', 'margin': 'auto'}
)

header = html.H1(
    id="header",
    children="Sales Data Pink Morsels Visualizer",
    style={
        "background-color": colors["secondary"],
        "color": colors["font"],
        "border-radius": "20px",
        "text-align": "center",
        "padding": "30px",
        "margin-bottom": "25px"
    }
)

# Define the layout of the app
app.layout = html.Div(
    children=[
        header,
        region_picker,
        graphs
    ],
    style={
        "text-align": "center",
        "border-radius": "30px",
        "background-color": colors["primary"]
    }
)

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
