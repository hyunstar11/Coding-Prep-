# 핵심 - array 선언, append 함수, 마이너스를 이용한 array 활용법 

n = int(input()) # n 이라는 숫자 입력받기 
array = [0,1] # 피보나치 수를 위한 array 선언하기 

for num in range(2,n+1): # array의 인덱스 2부터(array 의 원래 값인 0 1 다음의 내용) 해당되는 내용임..  
  array.append(array[-1]+array[-2]) # array 의 가장 마지막 자리 수 + 두 번째의 마지막 자리 수를 더한 뒤 그 합을 array 에 append 한다. 

print(array[n]) # array의 n 번재 수를 출력한다. 
