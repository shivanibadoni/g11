import pandas as pd
#Q1. Create a dataframe with your name, age, mail-id and phone number and add your friends’s information to the same. 
data = {'Name':['Gaurav'],'Age':[21],'mail id':['xyuhj213123@gmail.com'],'phone no':['9876764543']}
df = pd.DataFrame(data)
df.loc[1]=['Anil',21,'b83276hn@gmail.com','9987875654']       #Add detail of friend 1
df.loc[2]=['Aayush',20,'kjso9083@gmail.com','8876765445']       #Add detail of friend 2
print(df)
print("\n")

#Q2. Import the data and print:
df=pd.read_csv('weather.csv')
print(df)
#a.) First 5 rows of Dataframe
print(df.head(5))
#b.) First 10 rows of the Dataframe
print(df.head(10))
#c.) Find basic statistics on the particular dataset.
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())
#d.) Find the last 5 rows of the dataframe
print(df.tail(5))
#e.) Extract the 2nd column and find basic statistics on it.
finaldata=[df.iloc[:,2].sum(),
df.iloc[:,2].mean(),
df.iloc[:,2].median(),
df.iloc[:,2].nunique(),
df.iloc[:,2].max(),
df.iloc[:,2].min()]
print(finaldata) 
