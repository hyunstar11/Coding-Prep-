# 문자열 
# 구현 문제 
# 비슷한 문제들 - 

n = int(input()) # 입력 받을 워드의 수는 몇 개인지? 
group = 0 # 조건에 해당되는 단어들의 수는? 

for i in range(n):  # 0 1 2 n-1 까지 
  word = input() # 각 i에 대해 단어를 입력 받음
  error = 0 # 이게 하나라도 해당 되면 group 변수의 수는 못 올라감 
  for i in range(len(word)-1): # -1 까지로 설정해줘야 바로 밑의 if 문에서 비교할 때 에러가 발생하지 않음. 
    if word[i] != word[i+1]: # word의 i번째 원소와 바로 다음 원소가 다르면 
      new_word = word[i+1:] # 새로운 word를 생성 (그 다음 원소부터)
      if new_word.count(word[i]) > 0:  # 새로운 워드에 그 원래 워드에 있었던 특정 원소의 개수가 > 0 이라면 
        error += 1 # 에러 올라감 
  if error == 0 : # 에러가 0이면,
    group += 1 # 그룹 변수를 더해줌 
 
print(group) # 출력  
