import pandas as pd

data = {'이름' : ['Kim', 'Park', 'Lee', 'Ho'],
        '국어' : [90, 58, 88, 100],
        '영어' : [100, 60, 80, 70],
        '수학' : [55, 65, 76, 88]}

# 1
df = pd.DataFrame(data)

# 2
print(df, end='\n\n')

# 3
print(df['이름'], end='\n\n')

# 4
print(df.loc[1], end='\n\n')

# 5
newHo = df.loc[df["이름"] == "Ho", "수학"] = 90
print(newHo, end='\n\n')

# 6
df.loc[3] = ['Oh', 100, 70, 80]
print(df.loc[3], end='\n\n')

# 7
df = df.drop([2], axis=0)
print(df, end='\n\n')