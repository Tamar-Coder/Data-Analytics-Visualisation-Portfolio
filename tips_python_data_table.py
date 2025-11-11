import pandas as pd


# reading the database
data = pd.read_csv("tips.csv")

# printing the top 10 rows
display(data.head(10))
# display is not inbuilt to python or pandas. it is part of jupiter built