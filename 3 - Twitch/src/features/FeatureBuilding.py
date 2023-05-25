# 0.1) Import data from the load data file

import sys

sys.path.append("\\data")
from LibrariesAndData import *

# 1.0) Rewrite the variables types
# Channel variable is a category variable
data["Channel"] = data["Channel"].astype("category")
# Language variable is a category variable
data["Language"] = data["Language"].astype("category")
# Mature variable is a category variable
data["Mature"] = data["Mature"].astype("category")
# Partnered variable is a category variable
data["Partnered"] = data["Partnered"].astype("category")
data.info()

# 1.1) Delete variables
# 1.2) Create new variables
# 1.2.1) Procentual growth of followers
# First subtract the column followers gained from the column followers
data["StartFollowers"] = data["Followers"] - data["Followers gained"]
# Then divide the column followers from the column start followers divided by the column start followers and then multiply by 100 procent
data["ProcentualGrowthFollowers"] = (
    (data["Followers"] - data["StartFollowers"]) / data["StartFollowers"] * 100
)
# 1.2.2) Average watch time per viewer
# Divide the column watch time with the column stream time
data["AverageWatchTimePerViewer"] = (
    data["Watch time(Minutes)"] / data["Stream time(minutes)"]
)
# 1.2.3) Follower gain/viewer gain ratio
# Divide the column followers gained with the column viewers gained

data["FollowerGainViewerGainRatio"] = data["Followers gained"] / data["Views gained"]

# 1.3) Interaction variables
