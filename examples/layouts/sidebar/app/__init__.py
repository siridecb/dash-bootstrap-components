import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

FA = "https://use.fontawesome.com/releases/v5.6.3/css/all.css"

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, FA])
app.config.suppress_callback_exceptions = True

sidebar = dbc.Nav(
    [
        html.Div(html.H3("Menu"), className="sidebar-header"),
        html.Li(
            dbc.Row(
                [
                    dbc.Col("Graphs"),
                    dbc.Col(
                        html.I(className="fas fa-chevron-left fa-sm"),
                        width="auto",
                        align="center",
                        className="dropdown-chevron",
                    ),
                ],
                justify="between",
                align="center",
            ),
            id="graphs",
            className="toggler",
        ),
        dbc.Collapse(
            [
                dcc.Link("Scatter plot", href="/scatter"),
                dcc.Link("Histogram", href="/histogram"),
            ],
            id="graphs-collapse",
            is_open=True,
            className="sidebar-collapse",
        ),
        html.Li(
            dbc.Row(
                [
                    dbc.Col("Data"),
                    dbc.Col(
                        html.I(className="fas fa-chevron-left fa-sm"),
                        width="auto",
                        align="center",
                        className="dropdown-chevron",
                    ),
                ],
                justify="between",
                align="center",
            ),
            id="data",
            className="toggler",
        ),
        dbc.Collapse(
            [
                dcc.Link("Faithful", href="/data/faithful"),
                dcc.Link("Iris", href="/data/iris"),
            ],
            id="data-collapse",
            is_open=False,
            className="sidebar-collapse",
        ),
    ],
    id="sidebar",
    vertical=True,
    style={
        "flex-wrap": "nowrap",
        "overflow": "scroll",
        "padding-bottom": "100px",
    },
)


def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


def toggle_collapse_active_class(is_open):
    if is_open:
        return "toggler toggler-active"
    return "toggler"


app.callback(
    Output("graphs-collapse", "is_open"),
    [Input("graphs", "n_clicks")],
    [State("graphs-collapse", "is_open")],
)(toggle_collapse)

app.callback(
    Output("graphs", "className"), [Input("graphs-collapse", "is_open")]
)(toggle_collapse_active_class)

app.callback(
    Output("data-collapse", "is_open"),
    [Input("data", "n_clicks")],
    [State("data-collapse", "is_open")],
)(toggle_collapse)

app.callback(Output("data", "className"), [Input("data-collapse", "is_open")])(
    toggle_collapse_active_class
)
