import pandas as pd 
s = pd.Series(['banana', 42])
print(s)

# Series Method
# append    : 2개 이상의 시리즈 연결
# describe  : 요약 통계랑 계산
# drop_duplicates   : 중복값이 없는 시리즈 반환
# equals    : 시리즈에 해당 값을 요소가 있는지 확인
# get_values : 시리즈 값 구하기(values 속성과 동일)
# isin      : 시리즈에 포함된 값이 있는지 확인
# min
# max
# mean
# median    : 중간값 반환
# replace   : 특정 값을 가진 시리즈 값을 교체
# sample    : 시리즈에서 임의의 값을 반환
# sort_sample : 값을 정렬
# to_frame  : 시리즈를 데이터프레임으로 변환

scientists = pd.read_csv('./Doit_Pandas/data/scientists.csv')
ages = scientists['Age']
print(ages.max())
print(ages.mean())

# 불린 추출, 특정 조건 추가
print(ages > ages.mean())

# 참인 인덱스만 추출 가능 
# 브로드 캐스팅 - 모든 데이터에 대해 한 번에 연산하는 것
# 벡터 : 여러 개의 값을 가진 데어터
# 스칼라 : 단순 크기
# 벡터와 벡터의 연산은 Index가 같은 값끼리 수행
print(ages[ages > ages.mean()])

manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])

print()
print(scientists[scientists['Age'] > scientists['Age'].mean()])
print(scientists.loc[[True, True, False, True, True, True, False, True]])

# 숫자는 두배, 문자는 두배 길이
print(scientists*2)

print(scientists['Born'].dtype)

# 날짜 형식으로 바꾸기
born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')
print(born_datetime)

died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
scientists['born_dt'], scientists['died_dt']= (born_datetime, died_datetime)
print(scientists.head())

scientists['age_days_df'] = (scientists['died_dt'] - scientists['born_dt'])
print(scientists)

import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])

print(scientists.columns)

scientists_droped = scientists.drop(['Age'], axis=1)
print(scientists_droped.columns)

## 데이터 저장하고 불러오기
#  데이터를 바이너리 형태로 직렬화한 오브젝트를 저장하는 방법
names = scientists['Name']
scientists.to_pickle('./Doit_Pandas/output/scientists_df.pickle')

scientists_names_from_pickle = pd.read_pickle('./Doit_Pandas/output/scientists_df.pickle')
print('scientists_names_from_pickle')
print(scientists_names_from_pickle)