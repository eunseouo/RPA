import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('2024_seoul_data.csv', encoding = 'utf-8')
# 위 recode의 값으로 채우기(결측치 값 처리)
df2 = df.fillna(method='ffill')
df2.info()

df2.rename(colums={'일강수량':'precipitation'}, inplace = True)
# df2.rename(colums={'평균기온':'avg_temp'}, inplace = True)
# df2.rename(colums={'최고기온':'max_temp'}, inplace = True)
df2.head(3)

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.title('서울시 2024년도 여름 강수량 변화')
plt.plot(df2['일시'], df2['precipitation'], label= '일강수량', c='r')
plt.xlabel('일')
plt.ylabel('강수량')
plt.legend()
plt.show()