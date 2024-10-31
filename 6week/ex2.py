import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.font_manager as font_manager

   
hat = pd.read_csv('ch4-2.csv') # hat 변수에 데이터셋 입력
print(hat.describe(), end='\n\n')

font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

plt.subplot(1,1,1)


# 히스토그램 그리기
plt.figure(figsize=(10, 17))

plt.hist(hat.weight, bins=7)
plt.title('B 부화장 병아리 무게 분포 현황', fontsize = 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')

# sns.distplot(hat.weight) # 라인 히스토그램으로 보기
plt.show()