#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int fee[4];             // 1일, 1달, 3달, 1년 요금
int month_using[12];    // 각 달마다 이용 횟수
int answer;             // 최소 비용 저장

void dfs(int month, int cost) {
    if (month >= 12) {
        answer = min(answer, cost);
        return;
    }

    // 수영장을 사용하지 않는 달이면 넘어감
    if (month_using[month] == 0) {
        dfs(month + 1, cost);
    }
    else {
        // 1. 1일권 사용
        dfs(month + 1, cost + fee[0] * month_using[month]);

        // 2. 1달권 사용
        dfs(month + 1, cost + fee[1]);

        // 3. 3달권 사용
        dfs(month + 3, cost + fee[2]);
    }
}

int main() {
    // freopen("test_case.txt", "r", stdin);

    int TC;
    cin >> TC;

    for (int tc = 1; tc <= TC; tc++) {
        for (int i = 0; i < 4; i++) cin >> fee[i];
        for (int i = 0; i < 12; i++) cin >> month_using[i];

        answer = fee[3]; // 1년권 기준으로 초기화

        dfs(0, 0);

        cout << "#" << tc << " " << answer << endl;
    }

    return 0;
}
