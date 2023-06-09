# 0.1) Import data from the load data file

import sys

sys.path.append("\\data")
from LibrariesAndData import *

# Rewrite variables without spaces
data.columns = data.columns.str.replace(" ", "_")
data.info()

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
data["StartFollowers"] = data["Followers"] - data["Followers_gained"]
# Then divide the column followers from the column start followers divided by the column start followers and then multiply by 100 procent
data["ProcentualGrowthFollowers"] = (
    (data["Followers"] - data["StartFollowers"]) / data["StartFollowers"] * 100
)
# 1.2.2) Average watch time per viewer
# Divide the column watch time with the column stream time
data["AverageWatchTimePerViewer"] = (
    data["Watch_time(Minutes)"] / data["Stream_time(minutes)"]
)
# 1.2.3) Follower gain/viewer gain ratio
# Divide the column followers gained with the column viewers gained
data["FollowerGainViewerGainRatio"] = data["Followers_gained"] / data["Views_gained"]

# 1.3) Interaction variables


################################## EXTRA FOR THE FUTURE #################################


######### FOR EXAMPLE #########

# 1) Changing the variables from categorical to numerical values.
## le = LabelEncoder()
## df["sex_idx"] = le.fit_transform(df["sex"])
## df["smoker_idx"] = le.fit_transform(df["smoker"])
## df["region_idx"] = le.fit_transform(df["region"])
