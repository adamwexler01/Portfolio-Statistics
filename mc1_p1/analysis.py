import pandas as pd
import datetime as dt
import math
import matplotlib.pyplot as plt
import util
import os

def portfolio_stats(daily_values, daily_returns, sample_frequency, risk_free_rate):
	return cumulative_return(daily_values), \
		   average_daily_return(daily_returns), \
		   std_daily_return(daily_returns), \
		   sharpe_ratio(daily_returns, sample_frequency, risk_free_rate)

def plot_portfolio(daily_values):
	fig = plt.figure()
	daily_values.plot()
	plt.ylabel('Normalize price')
	plt.xlabel('Date')
	plt.title('Daily portfolio value')
	# plt.show()
	fig.savefig("output/results.png")
	fig.show()

def cumulative_return(daily_portfolio_values):
	return (daily_portfolio_values[-1] / daily_portfolio_values[0])-1

def average_daily_return(daily_portfolio_values):
	return daily_portfolio_values.mean()

def std_daily_return(daily_portfolio_values):
	return daily_portfolio_values.std()

def sharpe_ratio(daily_returns, sample_frequency, risk_free_rate):
	mean = (daily_returns - risk_free_rate).mean()
	std = (daily_returns).std()
	return math.sqrt(sample_frequency) * (mean/std)

def output_results(start_date, end_date, symbols, allocations, sr, sddr, adr, cr):
	with open("output/results.txt", "w") as file:
		file.write("Start Date: {}\n".format(start_date))
		file.write("End Date: {}\n".format(end_date))
		file.write("Symbols: {}\n".format(symbols))
		file.write("Allocations: {}\n".format(allocations))
		file.write("Sharpe Ratio: {}\n".format(sr))
		file.write("Volatility (stdev of daily returns): {}\n".format(sddr))
		file.write("Average Daily Return: {}\n".format(adr))
		file.write("Cumulative Return: {}\n".format(cr))

if __name__ == "__main__":
	sample_frequency = 252.0
	risk_free_rate = 0.0
	start_date = dt.datetime(2010,1,1)
	end_date = dt.datetime(2010,12,31)
	allocations = [0.2, 0.3, 0.4, 0.1]
	symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
	# symbols_with_BTC = ['GOOG', 'AAPL', 'GLD', 'BTC']
	daily_values = util.portfolio_setup(start_date, end_date, allocations, symbols)
	# daily_values_with_BTC = util.portfolio_setup(start_date, end_date, allocations, symbols_with_BTC)
	daily_returns = daily_values / daily_values.shift(1) - 1
	# daily_returns_with_BTC = daily_values_with_BTC / daily_values_with_BTC.shift(1) - 1
	cr, adr, sddr, sr = portfolio_stats(daily_values, daily_returns, sample_frequency, risk_free_rate)
	# cr_with_BTC, adr_with_BTC, sddr_with_BTC, sr_with_BTC = portfolio_stats(daily_values_with_BTC, daily_returns_with_BTC, sample_frequency, risk_free_rate)
	plot_portfolio(daily_values)
	output_results(start_date, end_date, symbols, allocations, sr, sddr, adr, cr)
	# print_output(start_date, end_date, symbols_with_BTC, allocations, sr_with_BTC, sddr_with_BTC, adr_with_BTC, cr_with_BTC)


