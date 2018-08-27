#include<stdio.h>
#include<vector>
using namespace std;
vector<vector<int> >T;
void fillT(int,int);
int getAns(int,int);
void DFS(int,int,int,int);
int main(){
    T.assign(50,vector<int>(50,0));
    int n = 1;
    int m = 1;
    int ans;
    while(1){
        scanf("%d %d",&n,&m);
        if(n== 0 && m==0)
            return 0;
        fillT(m,n);
        ans = getAns(m,n);
        printf("%d\n",ans);
    }
}
void fillT(int n, int m){
    for(int i = 0;i<n;i++)
        for(int j = 0;j<m;j++)
            scanf("%d",&T[i][j]);
}
int getAns(int n,int m){
    int sum = 0;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<m;j++){
            if(T[i][j] == 1){
                DFS(i,j,n,m);
                ++sum;
            }
        }
    }
    return sum;
}

void DFS(int i,int j,int n,int m){
    int dx[8] = {-1,0,1,0,-1,1,1,-1};
    int dy[8] = {0,1,0,-1,-1,1,-1,1};
    T[i][j] = 0;
    int newi,newj;
    for(int k = 0;k<8;k++){
        newi = dx[k]+i;
        newj = dy[k]+j;
        if(newi>=0 && newi<n && newj>=0 && newj<m && T[newi][newj] == 1){
            DFS(newi,newj,n,m);
        }
    }
    return;
}
        

