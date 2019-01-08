import pandas as pd
from sklearn import datasets

_iris_raw = datasets.load_iris()
IRIS = pd.DataFrame(_iris_raw["data"], columns=_iris_raw["feature_names"])


FAITHFUL = pd.read_csv(
    "https://cdn.opensource.faculty.ai/old-faithful/data.csv"
)
