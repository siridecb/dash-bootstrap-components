import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, sidebar
from app.faithful import layout as faithful_layout
from app.histogram import layout as histogram_layout
from app.iris import layout as iris_layout
from app.scatter import layout as scatter_layout


def serve_layout():
    content = html.Div(dbc.Container(id="page-content"), id="content")
    return html.Div(
        [dcc.Location(id="url"), sidebar, content], className="wrapper"
    )


app.layout = serve_layout


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def navigate(pathname):
    if pathname == "/histogram":
        return histogram_layout
    if pathname == "/scatter":
        return scatter_layout
    if pathname == "/data/faithful":
        return faithful_layout
    if pathname == "/data/iris":
        return iris_layout
    return dbc.Jumbotron(
        [
            html.H3("404 - Not found", className="text-danger"),
            html.P("The url you have tried to reach could not be found..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
