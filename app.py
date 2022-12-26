# 1. Import Dash
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import statistics as st
from statistics import mode
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64

print('BERHASIL')

# 2. Create a Dash app instance
app = dash.Dash(
    external_stylesheets=[dbc.themes.MATERIA],
    name = 'Mining Eyes Analytics'
)

## --- Title
app.title = 'Mining Eyes Analytics'

## --- Navbar

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),

    ],
    brand="Mining Eyes Analytics",
    brand_href="#",
    color="success",
    dark=True,
)

## Import Dataset gpp
nov = pd.read_csv('data_input/nov.csv')
nov2 = pd.read_csv('data_input/nov2.csv')
nov3 = pd.read_csv('data_input/nov3.csv')
nov4 = pd.read_csv('data_input/nov4.csv')

## VISUALIZATION

## CARD
x = nov['Num_dev'].sum()
y = f'{x:,}'
total_deviasi = [
    dbc.CardHeader('Number of Data Deviation'),
    dbc.CardBody([
        html.H1(y)
    ]),
]

a = nov['Num_Val'].sum()
b = f'{a:,}'
total_validasi = [
    dbc.CardHeader('Number of Data Validation'),
    dbc.CardBody([
        html.H1(b)
    ]),
]
## PIE CHART 1
data  = ['Dev','Val']
count = [nov['Num_dev'].sum(), nov['Num_Val'].sum()]
data_nov = {
    'data': data,
    'count':count
        }

data_nov = pd.DataFrame(data_nov)
pie1 = px.pie(
    data_nov,
    values='count',
    names='data',
    color_discrete_sequence=['lightgreen','darkgreen'],
    template='ggplot2',
    hole=0.3,
    title = 'Percentage Data Deviation vs Validation',
    height=490
)

#nov['Date'] = nov['Date'].astype('datetime64')
## LINE
dev = px.line(nov, 
              x="Date", 
              y="Num_dev",
              color_discrete_sequence=['red'],
              title = 'Trend Number of Data Deviation',
              labels = {
                'Num_dev':'Number of Deviation'},
             )

val = px.line(nov, 
              x="Date", 
              y="Num_Val",
              color_discrete_sequence=['green'],
              title = 'Trend Number of Data Validation',
              labels = {
                'Num_Val':'Number of Validation'},
             )
val2 = px.line(nov, 
              x="Date", 
              y="%val",
              color_discrete_sequence=['yellowgreen'],
              title = 'Percentage Number of Data Validation',
              labels = {
                '%val':'Percentage (%)'},
             )

### PIE 2
pie2 = px.pie(
    nov2,
    values='Jumlah Deviasi',
    names='Type Validation',
    color = 'Type Validation',
    color_discrete_sequence=['red','mediumseagreen'],
    template='ggplot2',
    #hole=0.3,
    title = 'Percentage True and False Warning'
)

### BAR 
nov2_2 = pd.crosstab(index=[nov2['type_object'],nov2['Type Validation']],
            columns='num_dev',
            values=nov2['Jumlah Deviasi'],
            aggfunc='sum')

nov2_2.reset_index(inplace = True)

bar1 = px.bar(
    nov2_2.sort_values('num_dev', ascending = False),
    x = 'type_object',
    y = 'num_dev',
    color = 'Type Validation',
    color_discrete_sequence=['mediumseagreen','red'],
    title='Number of Type Validation Each Object',
    labels = {
        'num_dev':'Number of Deviation',
        'type_object':'Type Object'},
   barmode='group'
)

nov4_1 = pd.crosstab(index=[nov4['type_object'],nov4['report_from']],
            columns='Num of Deviation',
            values=nov4['Num of Deviation'],
            aggfunc='sum')

nov4_1.reset_index(inplace = True)

bar2 = px.bar(
    nov4_1.sort_values('Num of Deviation', ascending = False),
    x = 'type_object',
    y = 'Num of Deviation',
    color = 'report_from',
    color_discrete_sequence=['darkblue','orange'],
    title='Comparison of Deviation from MEA and BEATS',
    labels = {
        'type_object':'Type of Object',
        'report_from':'Report From'},
   barmode='group'
)

# image
path_img = 'gambar.jpg'
encode = base64.b64encode(open(path_img, 'rb').read()).decode('ascii')
## PIE 3
# nov3_1 = pd.crosstab(index=nov3['Type_False_Deviation'],
#             columns='Total_deviation',
#             values=nov3['Total_deviation'],
#             aggfunc='sum')

# nov3_1.reset_index(inplace = True)


# pie3 = go.Figure(data=[go.Pie(labels=nov3_1['Type_False_Deviation'], 
#                              values=nov3_1['Total_deviation'], 
#                              pull=[0.2,0],
#                             title = 'Percentage Reason of False Warning')])

### LOLYPOP
# nov3_3 = pd.crosstab(index=nov3['Caused'],
#             columns='Total_deviation',
#             values=nov3['Total_deviation'],
#             aggfunc='sum')

# nov3_3.reset_index(inplace = True)

# lolypop = px.bar(
#     nov3_3.sort_values('Total_deviation', ascending = False),
#     x = 'Total_deviation',
#     y = 'Caused',
#     color = 'Caused',
#     color_discrete_sequence=['red','blue','green','purple','brown'],
#     title='Number of Caused False Warning Each Object'
# )

## --- LAYOUT
app.layout = html.Div(children=[
    navbar,

    html.Br(),

    ## -- Component Main Page --
    html.Div([
        #html.H1('Analysis Mining Eyes Analytics'),

        
        ### BREAK
        dbc.Row([
            
            dbc.Card(
                html.H3('Evaluation Mining Eyes Analytics Model', className="card-title", style={'textAlign': 'center'}),
            ),
            
        ]),
        html.Br(),

        
        ## ROW 1
        dbc.Row([
            ##--COLUMN 1
            dbc.Col([
                ## ROW 1.1
                dbc.Row([
                    html.Br(),
                    dbc.Card([
                        html.Br(),
                        #dbc.CardHeader('Mining Eyes Analytics'),

                        dbc.CardBody([
                            html.P('Mining Eyes Analytics merupakan salah satu inovasi Mining Eyes di operasional PT Berau Coal dengan penggunaan kamera CCTV dan penambahan AI dalam mendukung pemantauan operasi. Inovasi ini bertujuan untuk meningkatkan aspek keselamatan pekerja serta meningkatkan produktivitas')                            
                        ]),
                    ]),
                ]), 
                ## ROW 1.2
                dbc.Row([
                    dbc.Col([
                        html.Br(),
                        dbc.Card(total_deviasi, color = 'lightgreen')
                        ]
                    ),
                    dbc.Col([
                        html.Br(),
                        dbc.Card(total_validasi, color = 'yellowgreen')
                    ]),
                    
            
                ]), 

            ], 
            width = 5),
            ## -- COLUMN 2
            dbc.Col([ 
                dbc.Card(
                    dbc.CardBody([
                        html.Div(html.Img(src='data:image/png;base64,{}'.format(encode))),
                        
                    ])
            
                ),

            ], 
            width = 7),
        ]),

        html.Br(),

        
        

        ## ROW 2
        dbc.Row([
            ##--COLUMN 1
            dbc.Col([ 
                dbc.Card(
                    dcc.Graph(
                        id='plot_pie1',
                        figure = pie1,

                    ),
                ),

            ], 
            width = 5),
            ## -- COLUMN 2
            dbc.Col([ 
                dbc.Card([
                    dbc.Tabs([
                        ### tab 2
                        dbc.Tab([
                            dcc.Graph(
                                id='plot_line3',
                                figure = val2,

                                    ),

                        ],
                        label = 'Trend Val/Dev'),
                        ### tab 2
                        dbc.Tab([
                                dcc.Graph(
                                    id='plot_line2',
                                    figure = val,

                                        ),

                            ],
                            label = 'Validation'),
                        ### tab 3
                        dbc.Tab([
                                dcc.Graph(
                                    id='plot_line1',
                                    figure = dev,

                                        ),

                            ],
                            label = 'Deviation'),

                    
                    ],),
                ]),
            ], 
            width = 7),

        
        ]),
        html.Br(),

        # ### BREAK
        # dbc.Row([
            
        #     dbc.Card(
        #         html.H3('Comparation Data Validation',className="card-title", style={'textAlign': 'center'})
        #     ),
            
        # ]),
        # html.Br(),

        ## ROW 3
        dbc.Row([
            ##--COLUMN 1
            dbc.Col([ 
                dbc.Card([
                    dcc.Graph(
                    id='plot_pie2',
                    figure = pie2,

                    ),
                ]),

            ], 
            width = 5),
            ## -- COLUMN 2
            
            dbc.Col([ 
                dbc.Card([
                    #dbc.Tabs([
                        ### TAB 1
                    # dbc.Tab([
                    dcc.Graph(
                        id='plot_bar1',
                        figure = bar1,

                            ),

                    # ], 
                    # label = 'MEA'

                    # ),
                        ## TAB 2
                        # dbc.Tab([
                        #     dcc.Graph(
                        #         id='plot_bar2',
                        #         figure = bar2,

                        #             ),

                        # ], 
                        # label = 'MEA VS BEATS'

                        # ),
                   # ]),
                ]), 

            ], 
            width = 7),
        ]),
        html.Br(),

        # ### BREAK
        # dbc.Row([
            
        #     dbc.Card(
        #         html.H3('Analysis False Warning Mining Eyes Analytics', className="card-title", style={'textAlign': 'center'})
        #     ),
            
        # ]),
        # html.Br(),
        ## ROW 4
        dbc.Row([
            ##--COLUMN 1
            dbc.Col([ 
                dbc.Card([
                dbc.CardHeader('Select Object'),
                dbc.CardBody(
                    dcc.Dropdown(
                        id='Choose_Object',
                        options = nov3['Object'].unique(),
                        value = 'HD',
                    ),
                ),
                  

                    dcc.Graph(
                        id = 'plot_pie3',
                        #figure = pie3
                    ),

                ]), 

            ],
            width = 5),
            ## -- COLUMN 2
            dbc.Col([ 
                dbc.Card([
                    dcc.Graph(
                        id = 'plot_lolypop',
                        #figure = lolypop
                    ),

                ]), 

            ],
            width = 7),


        
        ]),

        
        

    


        
    
    ],style={
        'paddingLeft':'30px',
        'paddingRight':'30px'
    } 
    
    )
    #html.H1(children='Dashboard Overview'), #judul dashboard

])

### CALLBACK PIE
@app.callback(
    Output(component_id='plot_pie3', component_property='figure'),
    Input(component_id='Choose_Object',component_property='value')
)

def update_plot3(Object_name):
    nov3_1 = nov3[nov3['Object']==Object_name]
    
    #Visualization
## BAR ACCURACY
    nov3_2 = pd.crosstab(index=[nov3_1['Object'],nov3_1['Type_False_Deviation']],
            columns='Total_deviation',
            values=nov3_1['Total_deviation'],
            aggfunc='sum')

    nov3_2.reset_index(inplace = True)


    pie3 = go.Figure(data=[go.Pie(labels=nov3_2['Type_False_Deviation'], 
                                values=nov3_2['Total_deviation'], 
                                pull=[0.2,0],
                                title = 'Percentage Reason of False Warning')]
                                ).update_traces(marker=dict(colors=['forestgreen','orange']))


    return pie3

### CALLBACK PIE
@app.callback(
    Output(component_id='plot_lolypop', component_property='figure'),
    Input(component_id='Choose_Object',component_property='value')
)

def update_plot3(Object_name):
    nov3_1 = nov3[nov3['Object']==Object_name]
    
    #Visualization
## BAR ACCURACY
    #nov3_2_1 = nov3_1_1[nov3_1_1['Type_False_Deviation'] == 'Algorithm error']
    nov3_3 = pd.crosstab(index=nov3_1['Caused'],
            columns='Total_deviation',
            values=nov3_1['Total_deviation'],
            aggfunc='sum')

    nov3_3.reset_index(inplace = True)

    lolypop = px.bar(
        nov3_3.sort_values('Total_deviation', ascending = False),
        x = 'Total_deviation',
        y = 'Caused',
        color = 'Caused',
        color_discrete_sequence=['darkgreen','green','lime','limegreen','lightgreen'],
        labels = {
        'Total_deviation':'Total of Deviaton'},
        title='Number of Caused False Warning Each Object',
        height=555
    )

    return lolypop
## 3. Start the Dash server
if __name__ == "__main__":
    app.run_server()