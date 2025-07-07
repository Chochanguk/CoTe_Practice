from collections import deque

def solution(picks, minerals):
    answer = 0
    fatigue = {
        'diamond': [1, 1, 1],
        'iron':    [5, 1, 1],
        'stone':   [25, 5, 1]
    }

    # 1. 광물을 5개씩 block으로 자르기 (순서 유지)
    blocks = []
    for i in range(0, len(minerals), 5):
        blocks.append(minerals[i:i+5])
    
    total_pick = sum(picks)
    blocks = blocks[:total_pick]  # 곡괭이 수만큼만 처리

    # 2. 각 block의 '가중치'를 계산 (다이아 > 철 > 돌 기준)
    def get_weight(block):
        score = 0
        for m in block:
            if m == 'diamond': score += 25
            elif m == 'iron': score += 5
            else: score += 1
        return score

    weighted_blocks = [(i, get_weight(block)) for i, block in enumerate(blocks)]

    # 3. 가장 무거운 block부터 좋은 곡괭이 할당 (인덱스 기준)
    weighted_blocks.sort(key=lambda x: -x[1])  # 가중치 내림차순
    # print(weighted_blocks)
    
    tool_order = []
    for i, cnt in enumerate(picks):  # 0: 다이아, 1: 철, 2: 돌
        for _ in range(cnt):
            tool_order.append(i)  # 도구 타입 인덱스 저장
    # print(tool_order)
    
    block_tools = [None] * len(blocks)
    for idx, (block_index, _) in enumerate(weighted_blocks):
        if idx >= len(tool_order):
            break
        block_tools[block_index] = tool_order[idx]  # block 순서에 맞게 도구 할당
    # print(f'사용 가능 툴: {block_tools}')
        
    # 4. 순서대로 block을 처리하며 피로도 계산
    tool_keys = ['diamond', 'iron', 'stone']
    for i, block in enumerate(blocks):
        tool_idx = block_tools[i]
        if tool_idx is None:
            break  # 도구 부족
        tool = tool_keys[tool_idx]
        for m in block:
            if m == 'diamond':
                answer += fatigue[tool][0]
            elif m == 'iron':
                answer += fatigue[tool][1]
            else:
                answer += fatigue[tool][2]

    return answer
