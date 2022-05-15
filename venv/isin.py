import numpy as np
import pandas as pd
from parsedate import datetime
import numpy as np
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
print(ser1[~ser1.isin(ser2)])