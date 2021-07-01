import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
app.title = 'Assignment-4'

app.layout = html.Div([
        html.Nav(children=[
            html.A('Home | ', href='#'),
            html.A('Code | ', href='https://www.github.com/aggarwalsiddharth'),
            html.A('Sources ', href='https://www.covid19india.org/')],className='navbar'),
    
    html.Div(
        className="app-header",
        children=[
            html.H1('COVID 19 🦠 - The Real Toll', className="app-header--title"),
       
        ]
    ),


    html.Div(
        children=html.Div([
            html.H2('Coronavirus Outbreak in India'),
            html.P('''
                Mortalities caused by Covid-19 in India from March 2020 to June 2021 allow us to observe the movement of the disease in various parts of the country.
                The hypothesis that the disease's spread began from metro cities and then towards other sub-urban parts can be corroborated using this visual.
            ''')
        ])
    ),
    html.Div(
        children = [
        html.H3('Covid-19 Mortalities in India from 2020 to 2021',style={'color':'white','text-align': 'center'}),
        html.Img(src='assets/images/img_b.gif',className="center")]),


    html.Div(
        children=html.Div([

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.P('''
                Comparing the number of Mortalities that happened before and during the Pandemic, allow us to get insight into the under-reporting that
                might have taken place. Granular Analysis of the Covid-19 Pandemic Death Toll for Karnataka is given below.  
            ''')
        ])
    ),
    html.Div(
        children = [
        html.Img(src='assets/images/a_1.jpeg',className="center")]),

    html.Div(
        children = [
        html.Img(src='assets/images/a_2.jpeg',className="center")])

])

if __name__ == '__main__':
    app.run_server(debug=True)