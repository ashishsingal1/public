import pandas as pd
import numpy as np
import highcharts as hc

def df_to_hc(df, chart_type='bar'):
    H = hc.Highchart(width=750, height=600)
    options = {
        'xAxis': {
            'categories': list(df.columns)
        }
    }
    H.set_dict_options(options)
    # use .tolist() instead of list() to convert numpy to native types
    for r in list(df.index): H.add_data_set(df.loc[r].tolist(), chart_type, r)
    return H