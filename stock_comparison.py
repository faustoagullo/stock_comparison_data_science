from matplotlib import pylab as plt
import pandas as pd

df1 = pd.read_csv(r"/Users/faustoagullo/PycharmProjects/stock_comparison_data_science/TM.csv")
print(df1.head())

df2 = pd.read_csv(r"/Users/faustoagullo/PycharmProjects/stock_comparison_data_science/TSLA.csv")
print(df2.head())

mean_TM = df1["Close"].mean()
mean_TSLA = df2["Close"].mean()

plt.figure("Toyota Motors vs Tesla\nStock Price")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.3, label="TM Stock price, mean="+str(mean_TM))
# or the same can be:
plt.plot("Date", "Close", 'r-', linewidth=0.3, label="Tesla Stock Price, mean="+str(mean_TSLA), data=df2)

plt.scatter(df1["Date"],
df1["Close"], color="r")

plt.scatter(df2["Date"],
df2["Close"], color="b")

plt.show

plt.show()

