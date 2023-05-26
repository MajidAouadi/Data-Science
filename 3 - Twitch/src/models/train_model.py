# Load linear regression model library
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression

# Check data types, names etc.
data.info()

# Build linear regression model
model = smf.ols("Average_viewers ~ Peak_viewers", data=data)
model = model.fit()
model.params
