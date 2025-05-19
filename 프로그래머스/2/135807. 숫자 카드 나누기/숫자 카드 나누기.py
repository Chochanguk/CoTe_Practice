import math


def get_gcd_from_array(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        # 최대 공약수를 찾음.
        result = math.gcd(result, arr[i])
    return result

# 해당 수의 약수를 찾음
def get_divisors(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

# 해당 약수들 중에 문제를 만족하는지 체크
def is_valid(divisor, arr):
    for num in arr:
        if num % divisor == 0:
            return False
    return True

def solution(arrayA, arrayB):
    result = 0

    # A의 GCD로부터 후보 약수
    a_gcd = get_gcd_from_array(arrayA)
    a_divisors = get_divisors(a_gcd)
    print('a_divisors:',a_divisors)
    for d in a_divisors:
        if is_valid(d, arrayB):
            result = max(result, d)

    # B의 GCD로부터 후보 약수
    b_gcd = get_gcd_from_array(arrayB)
    b_divisors = get_divisors(b_gcd)
    print('b_divisors:',b_divisors)
    for d in b_divisors:
        if is_valid(d, arrayA):
            result = max(result, d)

    return result
