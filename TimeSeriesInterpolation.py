#NatWest
def calcMissing(readings):
    # Write your code here
    time_series = pd.DataFrame(readings,columns=['DateTime'])
    time_series[['DateTime','Mercury']] = time_series['DateTime'].str.split('\t',expand = True)
	
    missing_mercury = time_series['Mercury'].loc[time_series['Mercury'].str.index('Missing').dropna().index]
	time_series.iloc[missing_mercury.index] = 'NaN'
	time_series['Mercury'] = time_series['Mercury'].astype(float).interpolate()
	
	for interpolation in time_series.iloc[missing_mercury.index]:
	  print(interpolation)