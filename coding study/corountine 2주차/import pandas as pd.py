
import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("C:/Users/JSW/Desktop/x/통합 문서1.txt", encoding = 'utf-8')
print(df)

print(df.head())    # 상위 5개 행 출력
print(df.info())    # 데이터 타입, 결측치 확인
print(df.describe())    # 수치 데이터 요약 통계

print(df['급여'].mean())    # 전체 평균 급여
print(df.groupby('부서')['급여'].sum())    #부서별 급여 합계

df['입사일'] = pd.to_datetime(df['입사일'])    #입사일 날짜형으로 변경
print(df.info())

recent = df[df['입사일'] >= '2021-01-01']    # 2021년 이후 입사자만 보기
print(recent)

df['실수령액'] = df['급여']*(1-0.033)    # 세금 3.3% 공제후 실수령액
print(df)

df.to_csv('정리된_직원_데이터.csv', index=False)    # 결과 저장(엑셀/CSV) 