import pandas as pd

import Scripts.chartgpt.chartgpt_c as cg

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"
)
chart = cg.Chart(df, api_key=None, max_tokens=500)
chart.plot("pop vs state", return_fig=False, show_code=True)