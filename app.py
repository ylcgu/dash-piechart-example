import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######
myheading = "What's your favorite Dunkin' Donut?"
mytitle = "Top 3 Flavors"
mylabels = ['Chocolate Frosted', 'French Cruller', 'Boston Creme']
myvalues = [45,25,7]
color1 = 'e11383'
color2 = 'f5821f'
color3 = '683817'
tabtitle = 'dunkin'
sourceurl = 'https://brandpalettes.com/dunkin-donuts-color-codes/'
githublink = 'https://github.com/austinlasseter/dunkin-donuts'

########### Set up the chart
mydata = go.Pie(
    hole=0.5,
    sort=False,
    values=myvalues,
    labels=mylabels,
    textinfo='labels',
    textposition='inside',
    marker={'colors': [color1, color2, color3],
            'line': {'color': 'white', 'width': 5}}
)
mylayout = go.Layout(
    title = mytitle
)
fig = go.Figure(data=[mydata], layout=mylayout)

########### Initiate the app
app = dash.Dash()
server = app.server
app.title=tabtitle
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
