import pandas as pd
from django.shortcuts import render
from .dashboard import frequency_table
from .dashboard import min_price
from .dashboard import min_price_with_groupby_manufacturer_and_transmission

def dashboard_view(request):
    queryset = pd.read_csv("dummy_data/vehicles_ml_dataset.csv")
    df = pd.DataFrame(queryset)
    return render(request, "vehicles/index.html", {
    "frequency_table": frequency_table(df),
    "minimum_price": min_price(df),
    "grouped_price": min_price_with_groupby_manufacturer_and_transmission(df)
    })

