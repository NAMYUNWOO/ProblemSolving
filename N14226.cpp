#include <stdio.h>
#include <iostream>
#include <queue>
using namespace std;

int main(){
    int n;scanf("%d",&n);
    int i,j;
    pair<int, int> node;
    vector<vector<int>> T(1001,vector<int>(1001,1001));
    queue<pair<int,int>> q;
    q.push(make_pair(1, 0));
    T[1][0] = 0;
    while (!q.empty()) {
        node = q.front();
        i = node.first;
        j = node.second;
        q.pop();
        if(T[i][i] == 1001){
            T[i][i] = T[i][j] +1;
            q.push(make_pair(i, i));
        }
        if(i+j<=n && T[i+j][j] == 1001){
            T[i+j][j] = T[i][j] +1;
            q.push(make_pair(i+j, j));
        }
        if(i-1>=0 && T[i-1][j] == 1001){
            T[i-1][j] = T[i][j] +1;
            q.push(make_pair(i-1, j));
        }
    }
    int ans = 1001;
    for(j = 0;j<1001;j++){
        ans = min(ans,T[n][j]);
    }
    printf("%d",ans);
    
}
