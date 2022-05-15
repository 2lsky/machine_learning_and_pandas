import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
print(pd.Series(np.random.randint(0,10,10),index=[datetime(year=2010,month=1,day=1)+timedelta(days=7*i) for i in range(0,10)]))
#pd.date_range('2000-01-01', periods=10, freq='W-SAT'))