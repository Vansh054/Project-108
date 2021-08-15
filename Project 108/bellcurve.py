import pandas as pd
import plotly.figure_factory as pff

data = pd.read_csv('data.csv')
avgRating = data["Avg Rating"].tolist()

graph = pff.create_distplot([avgRating],["Results"],show_hist=False)
graph.show()
