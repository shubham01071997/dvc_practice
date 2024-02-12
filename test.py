import pandas as pd
data=[
    {"name":"shubham","age":27,"city":"mumbai"},
    {"name":"sanchita","age":19,"city":"mumbai"},
    {"name":"shanta","age":50,"city":"mumbai"},
]

newData=pd.DataFrame(data)
newData.to_csv("data/data.csv",index=False)