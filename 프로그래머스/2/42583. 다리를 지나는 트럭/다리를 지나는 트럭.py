from collections import deque

def solution(bridge_length, weight, truck_weights):
    '''
    truck_weights=[3,4]이고, bridge_length가 3인경우
    
    0: [0,0,0]
    1: [0,0,3]
    2: [0,3,0]
    3: [3,4,0]
    4: [4,0,0]
    5: [0,0,0]
    
    총 5초 소요
    '''
    current_weight = 0 # 현재 다리위의 무게
    bridge = deque([0]*bridge_length) # 다리위에 무게를 설정
    truck_weights = deque(truck_weights) # 큐로 설정해서 맨앞에서부터 pop
    time = 0 
    
    # 다리 위의 값이 모두 없어질때까지
    while bridge:
        # 1. 한 칸 이동 (앞에 트럭이 나감)
        left = bridge.popleft()
        current_weight -= left

        # 2. 다음 트럭이 다리에 올라갈 수 있는지 확인
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                # 다리위에 올라갈 수 있으면 올림
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)  # 올라가지 못하면 빈 공간
        time += 1
        
    return time
