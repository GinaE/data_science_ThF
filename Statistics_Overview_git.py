# Statistics_Overview.py
import pandas as pd 
import scipy
import statistics as stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()  
data = [i.split(',') for i in data] # it became a list of lists...

column_names = data[0] # getting the names
data_rows = data[1::] # getting the data

df = pd.DataFrame(data_rows,columns=column_names) 

df.Alcohol = df.Alcohol.astype(float)  # works as well as df['Alcohol'] = ...
df.Tobacco = df.Tobacco.astype(float)

#Alcohol statistics: mean, median, mode, range, variance, and standard deviation
def range1(x):
	return(max(x)-min(x))

a_mean = df['Alcohol'].mean()
a_median = df['Alcohol'].median()
# a_mode = stats.mode(df['Alcohol'])
a_range = range1(df['Alcohol'])
a_var = df['Alcohol'].var()
a_std = df['Alcohol'].std()

t_mean = df['Tobacco'].mean()
t_median = df['Tobacco'].median()
t_range = range1(df['Tobacco'])
t_var = df['Tobacco'].var()
t_std = df['Tobacco'].std()

print('The means for the Alcohol and Tobacco datasets are {0:.3f} and {1:.3f}, respectively'.format(a_mean, t_mean))
print('The medians for the Alcohol and Tobacco datasets are {0:.3f} and {1:.3f}, respectively'.format(a_median, t_median))
print('The ranges for the Alcohol and Tobacco datasets are {0:.3f} and {1:.3f}, respectively'.format(a_range, t_range))
print('The variances for the Alcohol and Tobacco datasets are {0:.3f} and {1:.3f}, respectively'.format(a_var, t_var))
print('The standard deviations for the Alcohol and Tobacco datasets are {0:.3f} and {1:.3f}, respectively'.format(a_std, t_std))
