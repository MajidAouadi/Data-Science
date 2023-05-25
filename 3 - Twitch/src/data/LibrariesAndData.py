# Load libraries needed for this research

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# Load the data needed for this research

data = pd.read_csv(
    r"C:\Users\Eigenaar\Desktop\Python projects\Data\Data-Science\3 - Twitch\data\raw\twitchdata-update.csv"
)

# Check the data on missing values, variable types and names
data.info()  # Might have to change some variable types
data.isnull().sum()  # 0 missing values

# Rename the variable types if necessary
