#include <stdio.h>
#include <vector>
using namespace std;
vector<vector<int> >T;
vector<vector<int> >cache;
int getAns(int,int,int,int);
int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    T.assign(n,vector<int>(m,0));
    cache.assign(n,vector<int>(m,-1));
    for(int i = 0;i<n;i++)
        for(int j = 0;j<m;j++)
            scanf("%d",&T[i][j]);
    printf("%d\n",getAns(n-1,m-1,n,m));
    return 0;
}
int getAns(int i,int j,int n,int m){
    if(i == 0 && j == 0)
        return 1;
    if(cache[i][j] != -1)
        return cache[i][j];
    int dx[] = {-1,0,1,0};
    int dy[] = {0,1,0,-1};
    int new_i,new_j;
    int ans = 0;
    for(int d = 0;d<4;d++){
       new_i = i+dx[d];
       new_j = j+dy[d];
       if(new_i<n && new_i>=0 &&new_j<m && new_j>=0)
           if(T[new_i][new_j]>T[i][j])
               ans += getAns(new_i,new_j,n,m);
    }
    cache[i][j] = ans;
    return cache[i][j];
}
