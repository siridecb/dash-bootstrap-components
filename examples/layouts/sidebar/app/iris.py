import dash_bootstrap_components as dbc

from app.data import IRIS

layout = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardTitle("A random sample of the iris data"),
            dbc.Table.from_dataframe(
                IRIS.sample(10), bordered=True, striped=True, hover=True
            ),
        ]
    )
)
