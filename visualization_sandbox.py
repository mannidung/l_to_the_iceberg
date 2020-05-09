# Just a sandbox. Jupyter isn't that good at autocompleting

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('../dataframes/data.csv')

fig = df.hist()
plt.plot()