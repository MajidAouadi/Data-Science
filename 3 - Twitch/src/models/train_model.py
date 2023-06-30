# 0.0 Import previous created scripts

# 1) libraries and data script
import sys

sys.path.append("\\data")
from LibrariesAndData import *


# 2) Featurebuilding script
import sys

sys.path.append("\\features")
from FeatureBuilding import *

###################### START MODEL BUILDING ######################
# 1.0 - 5 STEPS TO BUILD A MODEL FROM SPLITTING THE DATA TO EVALUATING THE MODEL

# 1) Split data into X and Y Variable
x = data[
    [
        "Peak_viewers",
        "Followers",
        "Followers_gained",
        "Views_gained",
        "Partnered",
        "StartFollowers",
    ]
]
y = data["Average_viewers"]

# 2) Build training and testing set

x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=104, test_size=0.25, shuffle=True
)

# 3) Build linear regression and check coefficients

mlr = LinearRegression()
mlr.fit(x_train, y_train)
print("Intercept:", mlr.intercept_)
print("Coefficients:")
list(zip(x, mlr.coef_))

# 4) Evaluate the linear regression with RMSE

y_pred_mlr = mlr.predict(x_test)
print("Prediction for test set: {}".format(y_pred_mlr))
mlr_diff = pd.DataFrame({"Actual value": y_test, "Predicted value": y_pred_mlr})
mlr_diff.head()

# 5) Model Evaluation
from sklearn import metrics

meanAbErr = metrics.mean_absolute_error(y_test, y_pred_mlr)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_mlr)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_mlr))
print("R squared: {:.2f}".format(mlr.score(x, y) * 100))  # R-Squared of 47.02 %
print("Mean Absolute Error:", meanAbErr)
print("Mean Square Error:", meanSqErr)
print(
    "Root Mean Square Error:", rootMeanSqErr
)  # RMSE of 7327.84 meaning that the model is off by 7327.84 viewers on average.
