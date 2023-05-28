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

# 1.0) Build linear regression model - OLS
model = smf.ols("Average_viewers ~ Peak_viewers", data=data)
model = model.fit()
model.params

# 1.1) Evaluate the linear regression with RMSE

from sklearn.metrics import mean_squared_error
from math import sqrt

sqrt(
    mean_squared_error(data["Average_viewers"], model.predict(data["Peak_viewers"]))
)  # 6174.5

# 2.0) Build a continuous decision tree
# Create a seperate dataframe called 'X' which contains all explanatory variables from the 'data' dataframe
# Except the variable 'Average_viewers' which is the variable we want to predict
X = pd.DataFrame(data, columns=data.columns)
X = X.drop(["Average_viewers"], axis=1)
# Create a seperate dataframe called 'Y' which contains the variable 'Average_viewers' which is the variable we want to predict
Y = pd.DataFrame(data, columns=["Average_viewers"])
