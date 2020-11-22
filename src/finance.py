import yfinance as yf
def handleCommand(arguments):
    res = ''
    for arg in arguments:
        toPrint = yf.Ticker(arg)
        res += toPrint
