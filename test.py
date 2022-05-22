import pandas as pd
import requests
import io

with requests.Session() as s:
    # s.keep_alive = False
    s.headers['Connection'] = 'close'
    prox = {
        'https': 'socks5://nordvpn@u1.se:U1oregon@amsterdam.nl.socks.nordhold.net:1080'}
    r = s.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=U2QRUXVWDVWTRFHW&datatype=csv', proxies=prox)
    df = pd.read_csv(io.StringIO(r.text))
    print(df.head(5))
    s.close()
