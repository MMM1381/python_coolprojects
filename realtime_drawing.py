import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import yfinance as yf

data = yf.download(tickers='BTC-USD', period='max', interval='1d')

print(data)
# data = pd.read_csv("Load06_500mN cut.csv")
# count = 0
# x = []
# y = []


# def draw_graph(i):
#     global count
#     count += 1
#     x.append(data['Displacement'][count])
#     y.append(data['Load'][count])

#     plt.cla()
#     plt.plot(x,y)

# anima = animation.FuncAnimation(plt.gcf(), draw_graph, interval=1500)
# plt.show()