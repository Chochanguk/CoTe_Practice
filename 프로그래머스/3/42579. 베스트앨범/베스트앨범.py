def solution(genres, plays):
    answer = []
    
    '''
    문제 요구 사항 정리:
    1. 장르별 총 재생 수 기준으로 정렬 (내림차순)
    2. 각 장르마다 가장 많이 재생된 노래 2개씩 선택
    3. 노래 선택 기준: 
       - 재생 수 내림차순
       - 재생 수가 같으면 고유번호(idx) 오름차순
    '''

    # 1. 장르별 총 재생 수 저장
    g_dict = dict()
    for genre, play in zip(genres, plays):
        if genre not in g_dict:
            g_dict[genre] = play
        else:
            g_dict[genre] += play

    # 2. 총 재생 수 기준으로 장르 정렬 (내림차순)
    # g_dict.items()는 (장르, 총 재생 수) 형태의 튜플
    g_dict = dict(sorted(g_dict.items(), key=lambda item: item[1], reverse=True))

    '''
    예시:
    g_dict = { "pop": 3100, "classic": 1450 }
    '''

    # 3. 장르별로 (재생 수, 고유번호) 저장
    fin_dict = {}
    idx = 0
    while idx != len(plays):
        if genres[idx] not in fin_dict:
            fin_dict[genres[idx]] = [(plays[idx], idx)]
        else:
            fin_dict[genres[idx]].append((plays[idx], idx))
        idx += 1

    after = {}
    # 4. 각 장르 안에서 노래 정렬
    # 기준: 재생 수 내림차순, 인덱스 오름차순
    for k, v in fin_dict.items():
        v.sort(key=lambda x: (-x[0], x[1]))
        fin_dict[k] = v

    '''
    예시:
    fin_dict = {
        "classic": [(800, 3), (500, 0), (150, 2)],
        "pop": [(2500, 4), (600, 1)]
    }
    '''

    # 5. 장르별로 최대 2곡씩 추출
    g_list = []
    for k in g_dict:
        g_list.append(fin_dict[k][:2])  # 최대 2개씩만 선택

    # 6. 정답에 고유번호(idx)만 추가
    for result_list in g_list:
        for result in result_list:
            answer.append(result[1])

    return answer
