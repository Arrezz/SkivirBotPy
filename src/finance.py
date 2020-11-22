import yfinance as yf
def handleCommand(arguments):
    res = ''
    for arg in arguments:
        toPrint = yf.Ticker(arg)
        hist = toPrint.history(period="1d")
        res = res + str(hist) + '\n'
    return res
