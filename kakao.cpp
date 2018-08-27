#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
vector<vector<int> >a;
int ans = 0;
void DFS(int i,int j,int n,int m,int color){
    int dx[4] = {-1,0,1,0};
    int dy[4] = {0,1,0,-1};
    a[i][j] = 0;
    ans += 1;
    int newi,newj;
    for(int k = 0;k<4;k++){
        newi = dx[k]+i;
        newj = dy[k]+j;
        if(a[newi][newj] == color && newi>=0 && newi<n && newj>=0 && newj<m ){
            DFS(newi,newj,n,m,color);
        }
    }
    return;
}
vector<int> solution(int m, int n, vector<vector<int> > picture) {
    a = picture;
    int noa = 0;
    int nsa = 0;
    for (int i = 0;i<m;i++){
        for(int j = 0; j<n;j++){
            if(a[i][j] != 0){
                DFS(i,j,m,n,a[i][j]);
                nsa = max(ans,nsa);
                ans = 0;
                noa += 1;
            }
        }
    }
    vector<int> answer(2);
    answer[0] = noa;
    answer[1] = nsa;
    return answer;
}
