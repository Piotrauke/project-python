from datetime import datetime
import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import numpy as np
from storage import get_storage


patientname=''
patientbd=''
patientdis=''
patient = ''

intvals = 1000 # interval time in ms

'''
formatting + css
'''

def patient_info():
    if patient in get_storage():
        pd = get_storage()[patient]
        patientname=pd['fullname'][-1]
        patientbd=pd['birthdate'][-1]
        patientdis=pd['disabled'][-1]
        
        if patientdis == True:
            patientdis = "Yes"
        else:
            patientdis = "No"  

    else:
        patientname=[]
        patientbd=[]
        patientdis=[]
    

    fig = go.Figure(data=[
          go.Table(
              header=dict(values=['','<b><i>Patient Information</i></b>'],
              font=dict(size=16)),
                    cells=dict(values=[
                        ['<b>Name</b>', '<b>Year of Birth</b>', '<b>Disabled</b>'],
                        [patientname, patientbd, patientdis],])),
    ])

    fig.update_layout(
    title_text="<b>Patients Information</b>",
    title_x = 0.5,
    height=325,
    # width=500
    )
    return fig     







def data_table():
    if patient in get_storage():
        pd = get_storage()[patient]
        pvalues = np.array(pd["values"])

    else:
        pvalues = np.array([[0,0,0,0,0,0]])      

    lc = [pvalues[:,0]+pvalues[:,1]+pvalues[:,2]][-1]
    rc = [pvalues[:,3]+pvalues[:,4]+pvalues[:,5]][-1]
    
    fig = go.Figure(data=[
        go.Table(
            header=dict(values=['<b><i>Point</i></b>','<b><i>Pressure</i></b>'],
                        font=dict(size=16)),
                cells=dict(values= [
                    ['<b>L0</b>','<b>L1</b>','<b>L2</b>','<b>R0</b>','<b>R1</b>','<b>R2</b>','<b>Left Cumulative</b>', '<b>Right Cumulative</b>'],
                    [pvalues[-1][0], pvalues[-1][1], pvalues[-1][2], pvalues[-1][3], pvalues[-1][4], pvalues[-1][5], \
                    lc[-1],rc[-1]]]
                    )
        ),
    ],)

    fig.update_layout(
    title_text="<b>Pressure On Each Sensor</b>",
    title_x = 0.5,
    height=500,
    # width=500
    )

    return fig     







def math_table():
    if patient in get_storage():
        pd = get_storage()[patient]
        pvalues = np.array(pd["values"])
        anomalies = np.array(pd["anomalies"])
        # math_pvalues = np.append([pvalues[-1][0]])
          

    else:
        pvalues = np.array([[0,0,0,0,0,0]])      
        anomalies = np.array([0,0,0,0,0,0])


    # print(f"anomalies {anomalies}")
    # print(f"L0 anomalies : [{np.sum(anomalies[0])}]")

    fig = go.Figure(data=[
        go.Table(
            header=dict(values=[' ','<b>L0</b>','<b>L1</b>','<b>L2</b>','<b>R0</b>','<b>R1</b>','<b>R2</b>'],
                            font=dict(size=16)),
                cells=dict(values= [
                    [ '<b>Minimum</b>','<b>First Quartile</b>','<b>Median</b>','<b>Third Quartile</b>','<b>Maximum</b>','<b>Standard Deviation</b>'],
                    [np.min(pvalues[:,0]),np.percentile(pvalues[:,0],25),np.median(pvalues[:,0]), \
                        np.percentile(pvalues[:,0],75),np.max(pvalues[:,0]),np.std(pvalues[:,0],dtype=np.float32),],
                    [np.min(pvalues[:,1]),np.percentile(pvalues[:,1],25),np.median(pvalues[:,1]), \
                        np.percentile(pvalues[:,1],75),np.max(pvalues[:,1]),np.std(pvalues[:,1],dtype=np.float32),],
                    [np.min(pvalues[:,2]),np.percentile(pvalues[:,2],25),np.median(pvalues[:,2]), \
                        np.percentile(pvalues[:,2],75),np.max(pvalues[:,2]),np.std(pvalues[:,2],dtype=np.float32),],
                    [np.min(pvalues[:,3]),np.percentile(pvalues[:,3],25),np.median(pvalues[:,3]), \
                        np.percentile(pvalues[:,3],75),np.max(pvalues[:,3]),np.std(pvalues[:,3],dtype=np.float32),],
                    [np.min(pvalues[:,4]),np.percentile(pvalues[:,4],25),np.median(pvalues[:,4]), \
                        np.percentile(pvalues[:,4],75),np.max(pvalues[:,4]),np.std(pvalues[:,4],dtype=np.float32),],                         
                    [np.min(pvalues[:,5]),np.percentile(pvalues[:,5],25),np.median(pvalues[:,5]), \
                        np.percentile(pvalues[:,5],75),np.max(pvalues[:,5]),np.std(pvalues[:,5],dtype=np.float32),],   
                ]
                )
        ),
    ],)

    fig.update_layout(
    title_text="<b>Patient Analysis</b>",
    title_x = 0.5,
    height=500,
    # width=500
    )

    return fig     





def pressure_plot():
    if patient in get_storage():
        pd = get_storage()[patient]
        times = np.array(pd["timestamps"])
        pvalues = np.array(pd["values"])
    
    else:
        times = np.array([0])
        pvalues = np.array([[0,0,0,0,0,0]])



    fig = go.Figure(
        [
        go.Scatter(name="L0",x = times, y = pvalues[:,0]),
        go.Scatter(name="L1",x = times, y = pvalues[:,1]),
        go.Scatter(name="L2",x = times, y = pvalues[:,2]),
        go.Scatter(name="R0",x = times, y = pvalues[:,3]),
        go.Scatter(name="R1",x = times, y = pvalues[:,4]),
        go.Scatter(name="R2",x = times, y = pvalues[:,5]),
        ], 
    )

    fig.update_layout(
    title_text="<b>Individual Pressures</b>",
    title_x = 0.5,
    xaxis_title="<b>Time</b>",
    yaxis_title="<b>Pressure</b>",
    legend_title="<b>Point</b>",
    )

    return fig




def plot():  
    if patient in get_storage():
        pd = get_storage()[patient]
        times = np.array(pd["timestamps"])
        pvalues = np.array(pd["values"])
    
    else:
        times = np.array([0])
        pvalues = np.array([[0,0,0,0,0,0]])
    
    
    fig = go.Figure(
        [go.Scatter(name="Left Foot",x = times, y = pvalues[:,0]+pvalues[:,1]+pvalues[:,2],),
        go.Scatter(name="Right Foot",x = times, y = pvalues[:,3]+pvalues[:,4]+pvalues[:,5],)
        ], 
    )

    

    fig.update_layout(
    title_text="<b>Feet Pressures</b>",
    title_x = 0.5,
    xaxis_title="<b>Time</b>",
    yaxis_title="<b>Cumulative Pressure</b>",
    legend_title="<b>Foot</b>",
    )

    return fig     

 












app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
def create_layout():
        for patient in get_storage():
            pd = get_storage()[patient]
            times = np.array(pd["timestamps"])
            pvalues = np.array(pd["values"])
            patientname=pd['fullname'][-1]
            patientbd=pd['birthdate'][-1]
            patientdis=pd['disabled'][-1]   

    
        app.layout = html.Div(children=[
            dcc.Interval(id='interval', interval=intvals, n_intervals=0),
            html.Div(
                    children = [
                        html.H1(children = 'PPDV - Final Project',\
                            style = {'textAlign':'center'}),         
                        ],
                ),
            html.Div( 
                    children = [
                        html.H2(children = 'By Devon Power and Piotr Balcerzak',\
                            style = {'textAlign':'center'})         
                        ],
                ),
            html.Div(children=[
                html.H3("Patient ID", style={'margin-bottom':'0em'} ),
                # html.H1("Patient ID", style={'display': 'inline','position':'relative','padding-bottom':'50px','padding-top':'50px',} ),
                dcc.Dropdown(
                    id='dropdown',
                    options=[
                    {'label':i,'value':i} for i in map(str,range(1,7))
                    ],
                    placeholder='Select A Patient',
                    style={'height':'30px', 'width': '150px','bottom-margin': "-20em"},
                    clearable=False
                ),
                dcc.Graph(id="pat_info", figure = data_table(), style = {'height':'100%','width':'100%','margin-bottom' : '0em','align':'left'}), 
                html.Div(id='outputs', style = {'display': 'none'}),

            ]),
            html.Div(children=[                  
                # dcc.Graph(id="pat_info", figure = data_table(), style = {'height':'100%','width':'100%','margin-bottom' : '0em','align':'left'}), 
                dcc.Graph(id="data_table", figure = data_table(),  style = {'margin-bottom' : '0em'}),      
                dcc.Graph(id="math_table", figure = math_table(),  style = {'margin-bottom' : '0em'}),
                # html.Div(id='outputs', style = {'display': 'none'}),
                dcc.Graph(id="pressure_plot", figure = pressure_plot()),
                dcc.Graph(id="plot", figure = plot()),
                # dcc.Interval(id='interval', interval=100, n_intervals=0)
            ])
        ])
















@app.callback(
    Output(component_id='outputs', component_property='children'),
    Input(component_id='dropdown', component_property='value')
)

def update_output(value):
    global patient
    patient = value
    return patient

@app.callback(
    Output(component_id='plot',component_property='figure'),
    Input(component_id='interval',component_property='n_intervals' )
    )

def graph_update(n_intervals):
    return plot()


@app.callback(
    Output(component_id='data_table',component_property='figure'),
    Input(component_id='interval',component_property='n_intervals' )
    )

def graph_update(n_intervals):
    return data_table()

@app.callback(
    Output(component_id='pat_info',component_property='figure'),
    Input(component_id='interval',component_property='n_intervals' )
    )

def graph_update(n_intervals):
    return patient_info()

   
@app.callback(
    Output(component_id='math_table',component_property='figure'),
    Input(component_id='interval',component_property='n_intervals' )
    )

def graph_update(n_intervals):
    return math_table()

@app.callback(
    Output(component_id='pressure_plot',component_property='figure'),
    Input(component_id='interval',component_property='n_intervals' )
    )

def graph_update(n_intervals):
    return pressure_plot()
