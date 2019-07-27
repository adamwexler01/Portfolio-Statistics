import pandas as pd

def portfolio_setup(start_date, end_date, allocs, symbols):
	
	dates = pd.date_range(start_date, end_date)
	#	Create the empty dataframe
	
	main_dataframe = pd.DataFrame(index = dates)
	#	Index col will use the specified column as the index
	#	Parse Dates will parse the Date object
	# 	usecols will pull the columns you want
	#	na_values will label the nan values
	
	for symbol in symbols:
		dataframe = pd.read_csv(".././data/{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
		dataframe = dataframe.rename(columns={'Adj Close': symbol})
		main_dataframe = main_dataframe.join(dataframe, how='left')

	#Removing the Nan
	main_dataframe = main_dataframe.dropna()
	
	#Normalizing prices
	normalize_prices = main_dataframe / main_dataframe.iloc[0]
	
	#Multiplying the allocations and normalized
	allocs_prices = normalize_prices * allocs
	
	#Sum of each value row
	daily_portfolio_values = allocs_prices.sum(axis=1, skipna=True)
	return daily_portfolio_values
