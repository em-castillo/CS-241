'''Week 12 Checkpoint A - Panda Library'''

# Load a csv file in Pandas using the pandas.read_csv() method
import pandas

# file doesn't have headers
census_data = pandas.read_csv("census.csv", header=None)

# finding a median according to the column name
# census csv does not have a header row, so the columns
# don't have names. You can supply the names,
# or use the index of the column (in this case age is index 0)
mean = census_data[0].mean()
median = census_data[0].median()
max = census_data[0].max()
print(f'Mean: {mean:.2f}')
print(f'Median: {median}')
print(f'Max: {max}')

# Reading: 20 min
# Checkpoint: 10 min
