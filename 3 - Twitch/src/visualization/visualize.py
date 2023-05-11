# Research question: What are the driver's of a streamers average viewership?
# Description: This file contains the code to visualize the data in the Twitch dataset


## 0.1 - Load the data and libraries needed for this research
sys.path.append("\\data")
from LibrariesAndData import *

## 0.2 - Load the features, data changes etc. needed for this research
sys.path.append("\\features")
from FeatureBuilding import *

## 1.0 - Visualize the data
# import visuals_script
# Print summary of the variable names
data.info()
data.isnull().sum()

# 2. Bivariate analysis

# 3. Multivariate analysis
