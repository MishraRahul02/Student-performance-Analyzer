import pandas as pd
df = pd.read_csv("student_performance.csv")

#top 5 lines are
print("top 5 lines are: ")
print(df.head(5))

#bottom 5 lines are
print("last 5 lines are: ")
print(df.tail(5))

#total of Students
print("total students are ")
print(df.shape[0])

#Average of Marks

Avg_Marks = df[["Math","English","Science"]].mean()
print("Average of Marks")
print(Avg_Marks)

#added a column name of Total_Marks
df.insert(loc=6,column="Total_Marks",value=df["Math"]+df["English"]+df["Science"])
print("Adding a New Column Total_Marks")
print(df)

#Add a column name of Percentage
df.insert(loc=7,column="Percentage",value=df["Total_Marks"]/3)
print("Adding a New Column Percentage")
print(df)

#sorted marks from highest to lowest
df.sort_values(by="Total_Marks",ascending=False,inplace=True)
print("Sorted Marks from Highest to Lowest")
print(df)

#Low Attendace from 75
Low_Attendance = df[df["Attendance"]<75]
print("Low Attendance Students from 75 are: ")
print(Low_Attendance)

#top 3 performers
top_performers = df.nlargest(3,"Percentage")
print("Top 3 performers are: ")
print(top_performers)

#grouped by the Gender on Avg Marks
grouped_by = df.groupby("Gender")["Total_Marks"].mean()
print("Grouping Marks by their Gender")
print(grouped_by)

#finding missing Values 
print("Missing values in each column:")
print(df.isnull().sum())

#Droping missing values
print("\nAfter dropping rows with any missing values:")
df = df.dropna()
print(df)

#Saving file into csv file
df.to_csv("Analysis_completed_and_saved.csv",index=False)

print("Analysis completed and saved succesfully")