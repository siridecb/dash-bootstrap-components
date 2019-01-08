import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.figure_factory as ff

from app.data import FAITHFUL

fig = ff.create_distplot(
    [FAITHFUL.eruptions], ["Eruption duration"], bin_size=0.25
)
fig["layout"].update(
    {
        "title": "Geyser eruption duration",
        "showlegend": False,
        "xaxis": {"title": "Duration (minutes)"},
        "yaxis": {"title": "Density"},
    }
)

layout = dbc.Card(
    [
        dbc.CardHeader("A histogram"),
        dbc.CardBody(
            [
                dbc.CardTitle("Old Faithful eruption durations"),
                dcc.Graph(figure=fig),
            ]
        ),
    ]
)
