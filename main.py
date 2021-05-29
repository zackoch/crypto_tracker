import requests
from decimal import Decimal
from datetime import datetime
from models import session, Ethereum, Polygon


def ticker(pair):
    r = requests.get(
        f'https://api.kraken.com/0/public/Ticker?pair={pair}')
    r_json = r.json()
    if len(r_json['error']) == 0:
        return r_json['result'][pair.upper()]
    else:
        return r_json['error']


def insert_eth():
    response = ticker(pair='XETHZUSD')
    insert = Ethereum(ask=Decimal(response['a'][0]),
                      bid=Decimal(response['b'][0]),
                      last=Decimal(response['c'][0]),
                      open=Decimal(response['o']),
                      low=Decimal(response['l'][0]),
                      high=Decimal(response['h'][0]),
                      volume=Decimal(response['v'][0])
                      )
    session.add(insert)
    session.commit()


def insert_polygon():
    response = ticker(pair='MATICUSD')
    insert = Polygon(ask=Decimal(response['a'][0]),
                     bid=Decimal(response['b'][0]),
                     last=Decimal(response['c'][0]),
                     open=Decimal(response['o']),
                     low=Decimal(response['l'][0]),
                     high=Decimal(response['h'][0]),
                     volume=Decimal(response['v'][0])
                     )
    session.add(insert)
    session.commit()


def main():
    insert_eth()
    insert_polygon()


if __name__ == '__main__':
    main()
