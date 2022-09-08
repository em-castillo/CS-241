'''Week 12-14 Data Structure Project'''

# import libraries
import pandas as pd  # Our data manipulation library
import seaborn as sns  # Used for graphing/plotting
import matplotlib.pyplot as plt  # If we need any low level methods
import os  # Used to change the directory to the right place
os.chdir("/Users/Emily/Downloads/CS 241/nba_basketball_data/")

'''Load in the data'''
# The players data (basketball_players.csv) has the season stats
players = pd.read_csv("basketball_players.csv")

# 1 calculate mean and median of points scored
mean = players['points'].mean()
median = players['points'].median()
print(f'Mean: {mean:.2f}, Median: {median:.2f}')

# 2 highest points in a season. Who and year
print(players[['playerID', 'year', 'points']].sort_values(
    'points', ascending=True).head(1))

# 3 boxplot: total points, total assists, and total rebounds
# sns.boxplot(data=players[['points', 'assists', 'rebounds']])
# plt.show()
# plt.savefig("boxplot_rebounds.png")

# 4 plot that shows x=year, y= median of points
years_median = players[['points', 'year']].groupby('year').median()
print('median')
print(years_median)

years_median = years_median.reset_index()
# sns.regplot(data=years_median, x='year', y='points').set_title(
#     'Median of points per year')
# plt.show()
# plt.savefig("boxplot_pointYears.png")

'''Part II'''
# use graphs
# 1 fg + ft attempted , points. Players that scored more from attempts
sum_attempts = players['fgAttempted'] + players['ftAttempted']
players['totalAttempts'] = sum_attempts
# print(players)
print(players[['playerID', 'totalAttempts', 'points']].sort_values(
    'totalAttempts', ascending=False).head(10))


# 2 choose categories and see who is best in most categories
# chambwi points, rebounds, fg and ft

print(players[['playerID', 'points']].sort_values(
    'points', ascending=False).head(10))

print(players[['playerID', 'rebounds']].sort_values(
    'rebounds', ascending=False).head(10))

print(players[['playerID', 'assists']].sort_values(
    'assists', ascending=False).head(10))

print(players[['playerID', 'steals']].sort_values(
    'steals', ascending=False).head(10))

print(players[['playerID', 'blocks']].sort_values(
    'blocks', ascending=False).head(10))

print(players[['playerID', 'turnovers']].sort_values(
    'turnovers', ascending=False).head(10))

print(players[['playerID', 'fgAttempted', 'fgMade']
              ].sort_values('fgMade', ascending=False).head(10))

print(players[['playerID', 'ftAttempted', 'ftMade']
              ].sort_values('ftMade', ascending=False).head(10))
# print(players[['playerID', 'PostSteals']].sort_values(
#     'PostSteals', ascending=False).head(10))
# print(players[['playerID', 'blocks']].sort_values(
#     'blocks', ascending=False).head(10))
# print(players[['playerID', 'PostBlocks']].sort_values(
#     'PostBlocks', ascending=False).head(10))
# print(players[['playerID', 'assists']].sort_values(
#     'assists', ascending=False).head(10))
# print(players[['playerID', 'PostAssists']].sort_values(
#     'PostAssists', ascending=False).head(10))
# print(players[['playerID', 'rebounds']].sort_values(
#     'rebounds', ascending=False).head(10))
# print(players[['playerID', 'PostRebounds']].sort_values(
#     'PostRebounds', ascending=False).head(10))
# print(players[['playerID', 'turnovers']].sort_values(
#     'turnovers', ascending=False).head(10))
# print(players[['playerID', 'PostTurnovers']].sort_values(
#     'PostTurnovers', ascending=False).head(10))
# print(players[['playerID', 'points']].sort_values(
#     'points', ascending=False).head(10))
# print(players[['playerID', 'PostPoints']].sort_values(
#     'PostPoints', ascending=False).head(10))
# print(players[['playerID', 'threeAttempted', 'threeMade']].sort_values(
#     'threeMade', ascending=False).head(10))


# 3 three points per team or liga / year
print(players[['playerID', 'threeMade', 'year', 'tmID', 'lgID']].sort_values(
    'threeMade', ascending=False).head(10))


'''Part III'''
# 1 use 2 part II

# 2 compare same place with what they have done
player_bio = pd.read_csv("basketball_master.csv")
player_data = pd.merge(players, player_bio, how="left",
                       left_on="playerID", right_on="bioID")

print(player_data[['playerID', 'birthCity', 'birthState', 'birthCountry', 'steals']].sort_values(
    'steals', ascending=False).head(10))

print(player_data[['playerID', 'birthCity', 'birthState', 'birthCountry', 'turnovers']].sort_values(
    'turnovers', ascending=False).head(10))
# print(player_data[['playerID', 'bioID', 'birthCity', 'birthState',
#                    'birthCountry', 'points', 'rebounds', 'assists', 'blocks', 'steals', 'turnovers']].sort_values('rebounds', ascending=False).head(20))

# steals, turnovers IN

print(player_data[['height', 'points']].sort_values(
    'height', ascending=False).head(10))
player_data = player_data[player_data["height"] > 0]
sns.regplot(data=player_data, x='points', y='height').set_title(
    'Height vs Points')
plt.show()
plt.savefig("boxplot_height.png")

# sns.boxplot(data=player_data[['height', 'points']])

# send = code and picture
