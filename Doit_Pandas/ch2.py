import pandas as pd
import os

print(__file__)
# df = pd.read_csv("/home/carpdiem/gitHub/PythonStudy/Doit_Pandas/data/gapminder.tsv", sep='\t')
df = pd.read_csv("./Doit_Pandas/data/gapminder.tsv", sep='\t')

print('\n #1. df.head()')
print(df.head())

print('\n #2. type(df)')
print(type(df))
# shape : 데이터의 행과 열의 크기 정보
print('\n df.shape')
print(df.shape)

# 데이터의 프레임의 열 이름 확인
print('\n #3. df.columns')
print(df.columns)

print('\n #4. df.dtypes')
print(df.dtypes)

print('\n #5. df.info()')
print(df.info())

## 판다스와 파이썬 자료형     비교
# object        string      문자열
# int64         int         정수
# float64       float       소수점을 가진 숫자
# datetime64    datetime    날짜    

### 2-2. 데이터 추출하기

# 열 단위로 데이터 추출하기
country_df = df['country']
print('\n #6. type(country_df)')
print(type(country_df))

print('\n #7. country_df.head()')
print(country_df.head())

print('\n #8. country_df.tail()')
print(country_df.tail())

subset = df[['country', 'continent', 'year']]
print('\n #9. subset.head()')
print(subset.head())

print('\n #10. df.head(n=10)')
print(df.head(n=10))

print('\n #11. df.groupby("year")["lifeExp"].mean()')
print(df.groupby('year')['lifeExp'].mean())

grouped_year_df = df.groupby('year')
print('\n #12. type(grouped_year_df)')
print(type(grouped_year_df))

print('\n #13. grouped_year_df')
print(grouped_year_df.head())

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print('\n #14. type(grouped_year_df_lifeExp)')
print(type(grouped_year_df_lifeExp))
print(grouped_year_df_lifeExp.head())

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print(mean_lifeExp_by_year)

multi_group_var = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print(multi_group_var)

print(type(multi_group_var))

# 그룹화한 데이터 개수 세기
print(df.groupby('continent')['country'].nunique())

# 그래프 그리기
import matplotlib.pyplot as plt 

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)
global_yearly_life_expectancy.plot()