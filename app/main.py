# Main Function: Dash Application

# imports
from util import co_occuring_topics
from util import create_map
from util import publications_per_year
from util import plot_symptoms_histogram
from util import pie_plot
from util import plot_histogram
from util import pie_plot_symptoms
from util import publications_per_year_schizophrenia
from util import clinical_trials_per_year
from util import depression_publications_per_year
from util import depression_co_occuring_topics
from util import clinical_trials_per_year_bulimia

from dash import dcc
from dash import html
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
            {'label': 'Migraine', 'value': 'Q133823'},
            {'label': 'Schizophrenia', 'value': 'Q41112'},
            {'label': 'Mental Depression', 'value': 'Q4340209'},
            {'label': 'Bulimia Nervosa', 'value' : 'Q64513386'}
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
    elif disease == 'Q41112':
        return [
            dcc.Graph(id='publications-per-year-schizophrenia', figure=publications_per_year_schizophrenia()),
            dcc.Graph(id='clinical-trials-per-year-schizophrenia', figure=clinical_trials_per_year())
        ]
    elif disease == 'Q64513386':
        return [
            dcc.Graph(id='clinical-trials-per-year-bulimia', figure=clinical_trials_per_year_bulimia())
        ]
    elif disease == 'Q4340209':
        return [
            dcc.Graph(id='publications-per-year-mental-depression', figure=depression_publications_per_year()),
            dcc.Graph(id='co-occuring-topics', figure=depression_co_occuring_topics())
        ]
    else:
        return html.Div('Select disease')


