import numpy as np

#1 배열 만들기 (list->numpy 배열)
arr = np.array([1,2,3,4,5])
print(arr)
print(type(arr))    # 타입 확인 -> numpy.ndarray

#2 배열 연산
print(arr+10)    # 모든 원소에 +10
print(arr*2)    # 모든 원소에 *2

#3 2차원 배열(행렬)
matrix = np.array([[1,2,3],[4,5,6]])
print(matrix)

#4 배열 형태 확인
print(arr.shape)    # 배열 형태 (1차원 5개)
print(matrix.shape)    #(2행, 3열)

#5 배열 합계, 평균
print(arr.sum())    # 합계
print(arr.mean())    # 평균

#6 특정 값 조건 필터링
print(arr[arr>2])    # 2보다 큰 값만 추출

# Numpy의 핵심 배열 및 연산
# 파이썬 리스트 연산
lst = [1,2,3,4]
print([x*2 for x in lst]) # 맞긴하지만 느리다

arr = np.array([1,2,3,4])
print(arr*2)    # 매우 빠르고 간단하다

# for문, if문 등을 아예 사용할 필요 없음
#1. 1부터 100까지 숫자로 된 numpy의 배열 만들기
arr1 = np.arange(1,101)    # 1부터 100까지 숫자 생성
print(arr1)

#2. 짝수만 추출
even_arr1 = arr1[arr1%2==0]
print(even_arr1)

#3. 배열의 평균값 구하기
mean_value = arr1.mean()
print(mean_value)

#4. 배열 모양을 (10행, 10열로) 바꾸기
arr1_reshape = arr1.reshape(10,10)
print(arr1_reshape)