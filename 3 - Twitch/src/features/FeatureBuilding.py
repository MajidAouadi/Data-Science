# 0.1) Import data from the load data file

import sys

sys.path.append("\\data")
from LibrariesAndData import *

# 1.0) Rewrite the variables types
# Channel variable is a category variable
data["Channel"] = data["Channel"].astype("category")
# Language variable is a category variable
data["Language"] = data["Language"].astype("category")
