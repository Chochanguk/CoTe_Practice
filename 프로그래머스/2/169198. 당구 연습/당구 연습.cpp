#include <iostream>
#include <string>
#include <vector>
#include <cmath>

typedef long long ll;
const ll INF= 987654321;

using namespace std;

ll calDist(int x1,int y1,int x2,int y2){
    int dx=x1-x2;  int dy=y1-y2;
    ll dist=pow(dx,2)+pow(dy,2);
    return dist;
}

vector<int> solution(int m, int n, int startX, int startY, vector<vector<int>> balls) {
    vector<int> answer;

    
    for (int i=0;i<balls.size();i++){
        int cx=balls[i][0]; int cy=balls[i][1];
         ll minDist=INF; // 최솟값
        
        // 위
        if (!(cx==startX and cy>startY)){ //=> 바로 위는 원쿠션이 안됨
            minDist=min(minDist,calDist(startX,startY,cx,2*n-cy));   
        }
        // 아래
        if (!(cx==startX and cy<startY)){
            minDist=min(minDist,calDist(startX,startY,cx,-cy));   
        }
        // 오른쪽
        if (!(cx>startX and cy==startY)){
             minDist=min(minDist,calDist(startX,startY,2*m-cx,cy));     
        }
        // 왼쪽
        if (!(cx<startX and cy==startY)){
            minDist=min(minDist,calDist(startX,startY,-cx,cy));
        }
        
        // 값 삽입
        answer.push_back(minDist);
        
    }
    
    return answer;
}