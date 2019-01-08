import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.graph_objs as go
from sklearn.cluster import KMeans

from app.data import IRIS

km = KMeans(n_clusters=3)
df = IRIS.loc[:, ["sepal width (cm)", "sepal length (cm)"]]
km.fit(df.values)
df["cluster"] = km.labels_

centers = km.cluster_centers_

data = [
    go.Scatter(
        x=df.loc[df.cluster == c, "sepal width (cm)"],
        y=df.loc[df.cluster == c, "sepal length (cm)"],
        mode="markers",
        marker={"size": 8},
        name="Cluster {}".format(c),
    )
    for c in range(3)
]

data.append(
    go.Scatter(
        x=centers[:, 0],
        y=centers[:, 1],
        mode="markers",
        marker={"color": "#000", "size": 12, "symbol": "diamond"},
        name="Cluster centers",
    )
)

layout = {
    "xaxis": {"title": "sepal width (cm)"},
    "yaxis": {"title": "sepal length (cm)"},
}

fig = go.Figure(data=data, layout=layout)

layout = dbc.Card(
    [
        dbc.CardHeader("A scatter plot"),
        dbc.CardBody([dbc.CardTitle("Iris clusters"), dcc.Graph(figure=fig)]),
    ]
)
