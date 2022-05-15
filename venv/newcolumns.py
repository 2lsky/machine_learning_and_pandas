import numpy as np
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', converters={'medv': lambda x: 'High' if float(x) > 25 else 'Low'})
