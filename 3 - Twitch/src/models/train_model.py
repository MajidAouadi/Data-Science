# 0.1) Import data from the load data file

import sys

sys.path.append("\\data")
from LibrariesAndData import *

import sys

sys.path.append("\\features")
from FeatureBuilding import *

# Load linear regression model library
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

# Check data types, names etc.
data.info()

# Build linear regression model - OLS
model = smf.ols("Average_viewers ~ Peak_viewers", data=data)
model = model.fit()
model.params

# Evaluate the linear regression with RMSE

from sklearn.metrics import mean_squared_error
from math import sqrt

sqrt(
    mean_squared_error(data["Average_viewers"], model.predict(data["Peak_viewers"]))
)  # 6174.5
