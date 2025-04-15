def is_prime(num):
    if num<=1:
        return False
    
    for i in range(2, int(num**(0.5))+1):
        # 나누어 떨어지는게 있으면
        if num%i==0:
            return False
    
    return True
        
def dfs(num_list,num_s,stack):
    for i in range(len(num_list)):
        stack.append(num_list[i])
        new_str=''.join(stack)
        if new_str not in num_s:
            num_s.add(new_str)
            # 중복 제거
            dfs(num_list[:i] + num_list[i+1:],num_s,stack)
        # 백트래킹을 위해 pop dfs 탐색 후
        n=stack.pop()
        
def solution(numbers):
    answer = 0
    num_list = list(numbers)
    num_s = set()
    
    dfs(num_list, num_s, [])
    
    print('num_s: ',num_s)
    new_s=set()
    for num in num_s:
        new_s.add(int(num))
    print('new_s: ',new_s)
    for num in new_s:
        if is_prime(num):
            answer+=1
    
    
    return answer