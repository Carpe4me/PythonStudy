import pandas
import matplotlib.pyplot as plt

# 데이터 집합 불러오기
df = pandas.read_csv('./Doit_Pandas/data/gapminder.tsv', sep='\t')
print(" >>> Dataframe head() 정보보기")
print(df.head())

# Series, DataFrame
print(type(df))
print(df.shape)

# 데이터 프레임의 열 이름을 확인
print(df.columns)

# DataFrame  속성 
print(df.dtypes)

print("\ndf.info() : ")
print(df.info()) 

# 판다스와 파이썬 자료형 비교
# pandas              Python
# object              string
# int64               int
# float64           float
# datetime64      datetime

# 02-2 데이터 추출하기
country_df  = df['country']

print("\n type(country_df)")
print(type(country_df))

print(country_df.head())

subset = df[['country', 'continent', 'year']]
print("\n type(subset)")
print(type(subset))
print(subset.head())

print("\n 인덱스가 0인 행 데이터 추출: df.loc[0] ")
print(df.loc[0])

print("\n 마지막 행 데이터 추출: tail")
print(df.tail(n=1))

print("\n 연속으로 여러 인덱스 추출")
print(df.loc[[0, 99, 999]])

print("\n df.loc[[행],[열]], df.iloc[[행],[열]], ':' 모든행 ")
subset = df.loc[:, ['year', 'pop']]

subset = df.iloc[:, [2, 4, -1]]
print(subset.head())

print("\n list(range(3)) [:3] 동일")

print(df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']])


## 02-3 기초적인 통계 계산하기
print("\n # lifeExp 열을 연도별로 그룹화하여 평균 계산하기")
print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
print(type(grouped_year_df))
print("\n grouped_year_df.head()")
print(grouped_year_df.head())

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print("\n grouped_year_df_lifeExp.head()")
print(grouped_year_df_lifeExp.head())

print("\n # lifeExp, gdpPercap 열의 평균값을 연도,지역별로 그룹화하여 한번에 계산")
multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_var)

print("\n 빈도수")
print(df.groupby('continent')['country'].nunique())
print("\n ")

## 02-4 그래프 그리기
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
global_yearly_life_expectancy.plot()
plt.show()