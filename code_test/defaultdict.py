# from collections import defaultdict

# # 중첩 defaultdict 초기화: 첫 번째 레벨의 defaultdict는 두 번째 레벨의 defaultdict를 생성하고,
# # 두 번째 레벨의 defaultdict는 리스트를 기본값으로 가짐
# multi = defaultdict(lambda: defaultdict(list))

# # 예시 데이터: 종목코드 '005930'에 대해 여러 날짜의 데이터를 추가
# # '005930'은 첫 번째 레벨의 키, 날짜 '20210101'과 '20210102'는 두 번째 레벨의 키
# multi['005930']['20210101'].append(100)  # 2021년 1월 1일 데이터 추가
# multi['005930']['20210102'].append(200)  # 2021년 1월 2일 데이터 추가

# # 또 다른 종목코드 '066570'에 대해서도 동일하게 데이터 추가
# multi['066570']['20210101'].append(150)
# multi['066570']['20210102'].append(250)

# def get_data(multi, code, date):
#     """
#     multi에서 주어진 code와 date에 해당하는 데이터를 추출하는 함수

#     :param multi: 중첩 defaultdict 객체
#     :param code: 종목 코드 (예: '066570')
#     :param date: 데이터 날짜 (예: '20210101')
#     :return: 해당하는 데이터 리스트. 데이터가 없는 경우 빈 리스트 반환.
#     """
#     # 주어진 code에 해당하는 데이터가 없으면 자동으로 빈 defaultdict(list)를 생성
#     code_data = multi[code]
#     print(code_data)
#     ## 여기에 code_data의 딕셔너리 값을 출력하는 코드 추가

#     # 주어진 date에 해당하는 데이터가 없으면 자동으로 빈 리스트([])를 생성
#     return code_data[date]

# # 함수 사용 예시
# data = get_data(multi, '066570', '20210101')

# print(data)

from collections import defaultdict

l = defaultdict(list)
print(l)
""" 출력결과
defaultdict(<class 'list'>, {})
"""
d = defaultdict(dict)
print(d)
""" 출력결과
defaultdict(<class 'dict'>, {})
"""
# l['key1'] = [1,2,3]
l['key1'].append(1000)
d['key1'] = '딕셔너리'

print(l)
print(d)

print(dict(l))