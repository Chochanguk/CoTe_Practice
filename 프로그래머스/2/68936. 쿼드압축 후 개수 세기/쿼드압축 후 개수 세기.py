def solution(arr):
    answer = [0, 0]  # [0 개수, 1 개수]

    def compress(x, y, size):
        # 현재 정사각형에서 모든 값이 동일한지 확인
        initial = arr[x][y]
        all_same = True
        for i in range(x, x+size):
            for j in range(y, y+size):
                if arr[i][j] != initial:
                    all_same = False
                    break

        # 같으면 개수 증가
        if all_same:
            answer[initial] += 1
        else:
            # 4개로 쪼개기
            half = size // 2
            compress(x, y, half)
            compress(x, y + half, half)
            compress(x + half, y, half)
            compress(x + half, y + half, half)

    compress(0, 0, len(arr))
    return answer
