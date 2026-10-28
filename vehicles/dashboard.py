import plotly.express as px
import plotly.offline as opy
import plotly.graph_objects as go

import pandas as pd
def frequency_table(df):
 # Simple counts
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']
    
    table_html = manufacturer_counts.to_html(
    classes="table table-bordered table-striped table-sm",
    float_format='%.2f',
    justify='center'
    )
    return table_html


def min_price(df):
    manufacturer_counts = df[df['selling_price'] > 5000].reset_index()

    table_html = manufacturer_counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )

    return table_html


def min_price_with_groupby_manufacturer_and_transmission(df):
    grouped = df.groupby(['manufacturer', 'transmission'])['selling_price'].sum().to_frame('total_selling_price')

    return grouped.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format='%.2f',
        justify='center'
    )
