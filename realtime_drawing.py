import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import yfinance as yf

data = yf.download(tickers='BTC-USD', period='max', interval='1d')

x = []
y = []

print(data)
def draw_graph(i):
    global count
    x.append(i)
    y.append(data['Close'].iloc[i])

    plt.cla()
    plt.plot(x,y)

anima = animation.FuncAnimation(plt.gcf(), draw_graph,frames=len(data) ,interval=1500)
plt.show()