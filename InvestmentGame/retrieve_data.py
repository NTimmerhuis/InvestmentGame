import requests
import pandas as pd

def get_price(symbol,date):

    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + symbol + "&outputsize=full&apikey=0I1LVMCSQ4CF9GSR")

    # Since we are retrieving stuff from a web service, it's a good idea to check for the return status code
    # See: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    if response.status_code != 200:
        raise ValueError("Could not retrieve data, code:", response.status_code)
    # The service sends JSON data, we parse that into a Python datastructure
    raw_data = response.json()

    # The actual time series is huge, let's just look at the first few items
    #Let's use itertools to do this in a lazy way
    import itertools
    list(itertools.islice(raw_data['Time Series (Daily)'].items(), 0,5))

    # Let's be smart and retrieve the name of the column with our actual data
    colname = list(raw_data.keys())[-1]
    # We want to extract the corresponding column only
    data = raw_data[colname]

    df = pd.DataFrame(data).T.apply(pd.to_numeric)

    # Next we parse the index to create a datetimeindex
    df.index = pd.DatetimeIndex(df.index)

    # Let's fix the column names
    df.rename(columns=lambda s: s[3:], inplace=True)

    a = df.loc[date,'close']
    return a

x = get_price('KO','2019-09-24')
print(x)