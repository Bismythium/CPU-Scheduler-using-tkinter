import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("data.csv")
fig = ff.create_gantt(df)
fig.show()
