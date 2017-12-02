from forex_python.converter import CurrencyRates

c = CurrencyRates()


def USD_converter(ccy2):
    fx_rate = c.get_rate('USD', ccy2)
    return fx_rate

def EUR_converter(ccy2):
    fx_rate = c.get_rate('EUR', ccy2)
    return fx_rate


if __name__ == '__main__':
    ccy2 = input('укажите валюту: ')
    print(USD_converter(ccy2))
    print(EUR_converter(ccy2))
