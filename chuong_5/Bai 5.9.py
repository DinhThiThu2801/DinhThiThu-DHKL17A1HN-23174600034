import pandas as pd
from io import StringIO

csv_data = """region_id,region_name
1,europe
2,americas
3,asia
4,middle east and africa
"""

with open('region.csv', 'w') as file:
    file.write(csv_data)

df = pd.read_csv('region.csv')
print(df)
