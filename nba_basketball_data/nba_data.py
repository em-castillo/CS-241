'''Week 12 Pandas (and seaborn) Tutorial'''
'''load libraries'''

# This line isn't necessary, but it makes it so the later commands (e.g., read_csv)
# are in a consistent place (You will obviously need to change this to the correct location on _your_ computer.)
# If you have put the data files and your Python script in the same folder, you
# don't need this line.
import pandas as pd  # Our data manipulation library
import seaborn as sns  # Used for graphing/plotting
import matplotlib.pyplot as plt  # If we need any low level methods
import os  # Used to change the directory to the right place
os.chdir("/Users/Emily/Downloads/CS 241/nba_basketball_data/")

'''Load in the data'''
# The players data (basketball_players.csv) has the season stats
players = pd.read_csv("basketball_players.csv")
print(players)

'''Explore the data'''
# see available columns
print(players.columns)

# statistics about variables or columns.
min = players["rebounds"].min()
max = players["rebounds"].max()
mean = players["rebounds"].mean()
median = players["rebounds"].median()

print("Rebounds per season: Min:{}, Max:{}, Mean:{:.2f}, Median:{}".format(
    min, max, mean, median))

'''Finding the best rebounders'''
# highest rebounding. Top 10 rows
print(players.sort_values("rebounds", ascending=False).head(10))

# show fewer columns
print(players[["playerID", "year", "tmID", "rebounds"]
              ].sort_values("rebounds", ascending=False).head(10))

''' Merging or joining separate datasets'''
# The "master" data (basketball_master.csv) has names, biographical information, etc.
master = pd.read_csv("basketball_master.csv")

# We can do a left join to "merge" these two datasets together
nba = pd.merge(players, master, how="left",
               left_on="playerID", right_on="bioID")

# summary of the dataset
print(nba.columns)

print(nba[["year", "useFirst", "lastName", "tmID", "rebounds"]
          ].sort_values("rebounds", ascending=False).head(10))

'''Creating new columns'''
# average of rebounds per game.
# rebounds column: games played column
nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]
          ].sort_values("reboundsPerGame", ascending=False).head(10))

# Let's just remove any rows with GP=0
nba = nba[nba.GP > 0]

nba["reboundsPerGame"] = nba["rebounds"] / nba["GP"]
print(nba[["year", "useFirst", "lastName", "rebounds", "GP", "reboundsPerGame"]
          ].sort_values("reboundsPerGame", ascending=False).head(10))

'''Plotting with seaborn(sns) - Seaborn Library'''
# bloxplot of rebounds
# sns.boxplot(data=nba.reboundsPerGame)
#  OR box plot of multiple columns
# sns.boxplot(data=nba[["rebounds", "oRebounds", "dRebounds"]])

# Show the current plot using matplotlib as plt
plt.show()

# Save the current plot to a file
plt.savefig("boxplot_reboundsPerGame.png")


# '''Rebounds over time - facetgrid'''
# Get a subset of the data where the year is between 1980 and 1990
eighties = nba[(nba.year >= 1980) & (nba.year < 1990)]
# bloxplot
sns.boxplot(eighties["reboundsPerGame"], orient="v")
grid = sns.FacetGrid(eighties, col="year")
grid.map(sns.boxplot, "reboundsPerGame", orient="v")
# show graph
plt.show()
plt.savefig("boxplot_reboundsPerGame.png")

'''Rebounds over time - grouping by year'''
# statistics by year
# use the median of the reboundsPerGame
nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").median()
print(nba_grouped_year)

nba_grouped_year = nba_grouped_year.reset_index()
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame")
# remove years with median 0
nba_grouped_year = nba_grouped_year[nba_grouped_year["reboundsPerGame"] > 0]
sns.regplot(data=nba_grouped_year, x="year", y="reboundsPerGame").set_title(
    "Median rebounds per Year")

# using max
nba_grouped_year = nba[["reboundsPerGame", "year"]].groupby("year").max()
nba_grouped_year = nba_grouped_year.reset_index()

# Remove the zeros
nba_grouped_year = nba_grouped_year[nba_grouped_year["reboundsPerGame"] > 0]
sns.regplot(data=nba_grouped_year, x="year",
            y="reboundsPerGame").set_title("Max rebounds per year")
plt.show()
plt.savefig("boxplot_reboundsPerGame.png")

'''Summarizing in more complicated ways'''
# Get the top 10 rebounders per year
nba_topRebounders_perYear = nba[["reboundsPerGame", "year"]].groupby("year")[
    "reboundsPerGame"].nlargest(10)

# Get the median of these 10
nba_topRebounders_median_perYear = nba_topRebounders_perYear.groupby(
    "year").median()

# Put year back in as a column
nba_topRebounders_median_perYear = nba_topRebounders_median_perYear.reset_index()

# Again no zeros...
nba_topRebounders_median_perYear_noZeros = nba_topRebounders_median_perYear[
    nba_topRebounders_median_perYear["reboundsPerGame"] > 0]

# Now plot
sns.regplot(data=nba_topRebounders_median_perYear_noZeros, x="year",
            y="reboundsPerGame").set_title("Median of Top 10 Rebounders Each Year")

plt.show()
plt.savefig("boxplot_reboundsPerGame.png")

# tutorial 1 hour
