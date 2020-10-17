# -*- coding: utf-8 -*-

# Run this app with `python dashboard_app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


def create_dashboard(server):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, server=server,
                    routes_pathname_prefix='/dashapp/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP])

    PLOTLY_LOGO = "logocatastro.svg"

    navbar = dbc.Nav(
        [
            dbc.NavItem(
                html.Img(src=app.get_asset_url(PLOTLY_LOGO), height="40px")),
            dbc.NavItem(dbc.NavLink("Home", active=True, href="#",
                                    style={'background-color': '#ea0a2a',
                                           'widht': '5px'})),
            dbc.NavItem(dbc.NavLink("About", active=True, href="#",
                                    style={'background-color': '#ea0a2a',
                                           'widht': '5px'})),
            dbc.NavItem(dbc.NavLink("Contact", active=True, href="#",
                                    style={'background-color': '#ea0a2a',
                                           'widht': '5px'})),
            dbc.Button("Registrate", color="primary", className="mr-1",
                       style={'padding': '5px', 'background-color': '#3399ff'}),
        ],
        fill=True,
        pills=True
    )

    app.layout = html.Tbody(children=[
        html.Div(children=[
            navbar,
        ]),

        html.Div([
            html.H1(
                children='Consulta el valor catastral de tu propiedad con nuestro modelo',
                style={'color': 'white', 'font-size': '30px',
                       'margin': '0 0 50px 0',
                       'position': 'relative', 'padding': '30px'}),
            dbc.Button("Comenzar", color="warning", className="mr-1",
                       style={'padding': '20px'}),

        ], style={'background-image': f"url({app.get_asset_url('Banner.JPG')})",
                  'padding': '60px'}),

        html.H2(children='Conoce el valor de tu propiedad',
                style={'textAlign': 'center'}),

        html.Div(
            [
                dbc.Row(
                    [

                        dbc.Col(html.Div(dbc.Button("Probar", color="warning",
                                                    style={
                                                        'background-color': '#ea0a2a'})),
                                width=2),

                    ],
                    justify="center",
                ),
            ]),
    ], style={'padding': '0', 'margin': '0'})

    return app.server

# if __name__ == '__main__':
#     app.run_server(debug=True)
