import dash_bootstrap_components as dbc

from app.data import FAITHFUL

layout = dbc.Card(
    dbc.CardBody(
        [
            dbc.CardTitle("A random sample of the faithful data"),
            dbc.Table.from_dataframe(
                FAITHFUL.sample(10), bordered=True, striped=True, hover=True
            ),
        ]
    )
)
