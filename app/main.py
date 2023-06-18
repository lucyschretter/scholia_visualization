# Main Function: Dash Application

# imports
from util import co_occuring_topics
from util import create_map
from util import publications_per_year
from util import plot_symptoms_histogram
from util import pie_plot
from util import plot_histogram
from util import pie_plot_symptoms

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from jupyter_dash import JupyterDash

# Create Dash Application
app = JupyterDash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Diseases Dashboard'),
    dcc.Dropdown(
        id='disease-dropdown',
        options=[
            {'label': 'Bipolar Disorder', 'value': 'Q131755'},
            {'label': 'Migraine', 'value': 'Q133823'}
        ],
        value='Select Diasese'
    ),
    html.Div(id='graph-container')

])
@app.callback(
    Output('graph-container', 'children'),
    [Input('disease-dropdown', 'value')]
)
def update_graph(disease):
    if disease == 'Q131755':
        return [
            dcc.Graph(id='co-occurring-topics', figure=co_occuring_topics()),
            dcc.Graph(id='co-occurring-topics-map', figure=create_map()),
            dcc.Graph(id='publications-per-year', figure=publications_per_year())
        ]
    elif disease == 'Q133823':
        return [
            dcc.Graph(id='symptoms-count-histogram', figure=plot_symptoms_histogram()),
            dcc.Graph(id='pie-chart', figure=pie_plot()),
            dcc.Graph(id='histogram-treatments', figure=plot_histogram()),
            dcc.Graph(id='pie-plot-symptoms', figure=pie_plot_symptoms())
        ]
    else:
        return html.Div('Select disease')

