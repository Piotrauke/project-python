import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import numpy as np
from storage import get_storage


def legs_plot():
    if "2" in get_storage():
        pd = get_storage()["2"]
        times = np.array(pd["timestamps"])
        values = np.array(pd["values"])
    else:
        times = np.array([0])
        values = np.array([[0]])

    print(times)
    print(values)

    fig = go.Figure([go.Scatter(x = times, y = values[:,0],\
                        line = dict(color = 'firebrick', width = 4), name = 'L0')
                        ])
    return fig                    

app = dash.Dash()


def create_layout():
    app.layout = html.Div(id='parent', children = [
            html.H1(id = 'H1', children = 'Hey this is our awful plot', style = {'textAlign':'center',\
                                                    'marginTop':40, 'marginBottom':40}),\
                dcc.Graph(id = 'the_plot', figure = legs_plot()), \
                dcc.Interval(id='interval', interval=1000, n_intervals=0) 
                ] )

@app.callback(Output(component_id='the_plot',component_property='figure' ),
                [Input(component_id='interval',component_property='n_intervals' )])
def graph_update(n_intervals):
    print(n_intervals)
    return legs_plot()