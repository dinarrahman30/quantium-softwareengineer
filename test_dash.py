from pink_morsels import header, update_graph, data, region_picker
from dash import html, dcc
from selenium import webdriver
import pytest
import plotly.graph_objects as go

driver = webdriver.Chrome()
# driver.get("http://www.google.com/")

# Define color scheme
colors = {
    "primary": "#E6AAE8",
    "secondary": "#E60CBE",
    "tertiary": "#FA9FE8",
    "font": "#522A61"
}


def test_header_component():
    assert isinstance(header, html.H1)
    assert header.id == "header"
    assert header.children == "Sales Data Pink Morsels Visualizer"
    assert header.style == {
        "background-color": colors["secondary"],
        "color": colors["font"],
        "border-radius": "20px",
        "text-align": "center",
        "padding": "30px",
        "margin-bottom": "25px"
    }


def test_update_graph_all_regions():
    actual_fig = update_graph('all')
    assert actual_fig.layout.title.text == "Sales Data Pink Morsels"
    assert actual_fig.layout.xaxis.title.text == "Date"
    assert actual_fig.layout.yaxis.title.text == "Sales"
    assert actual_fig.layout.xaxis.tickformat == "%Y-%m-%d"
    assert actual_fig.layout.plot_bgcolor == colors["tertiary"]
    assert actual_fig.layout.paper_bgcolor == colors["primary"]
    assert actual_fig.layout.font.color == colors["font"]

    filtered_data = data.copy()
    expected_x = filtered_data['date']
    expected_y = filtered_data['sales']

    assert actual_fig.data[0].x.tolist() == expected_x.tolist()
    assert actual_fig.data[0].y.tolist() == expected_y.tolist()


def test_region_picker():
    assert isinstance(region_picker, dcc.RadioItems)
    assert region_picker.id == "region-pick"
    expected_options = [
        {"label": "North", "value": "north"},
        {"label": "East", "value": "east"},
        {"label": "South", "value": "south"},
        {"label": "West", "value": "west"},
        {"label": "All", "value": "all"}
    ]
    assert region_picker.options == expected_options

    # Check if the default value is 'north'
    assert region_picker.value == "north"
    assert region_picker.inline is True
    assert region_picker.style == {"font-size": "100%"}


# Run the tests
if __name__ == "__main__":
    pytest.main()
