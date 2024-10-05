import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import yfinance as yf

data = yf.download(tickers='BTC-USD', period='max', interval='1d')

count = 0
x = []
y = []


def draw_graph(i):
    global count
    count += 1
    x.append(count)
    y.append(data['Close'].iloc[count])

    plt.cla()
    plt.plot(x,y)

anima = animation.FuncAnimation(plt.gcf(), draw_graph, interval=1500)
plt.show()