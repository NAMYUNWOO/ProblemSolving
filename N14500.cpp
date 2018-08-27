#include <stdio.h>
#include <vector>
using namespace std;
vector<vector<int> >visited;
vector<vector<int> >T;
int getAns(int,int);
int DFS(vector<vector<int> > &,int,int,int);
int n,m;
int main(){
    scanf("%d %d",&n,&m);
    T.assign(n,vector<int>(m,0));
    visited.assign(n,vector<int>(m,0));
    for(int i = 0;i<n;i++)
        for(int j = 0;j<m;j++)
            scanf("%d",&T[i][j]);
    int maxVal = 0;
    for(int i = 0;i<n;i++)
        for(int j = 0;j<m;j++)
            maxVal = max(getAns(i,j),maxVal);
    printf("%d\n",maxVal);
}
int getAns(int i,int j){
    int maxVal = T[i][j];
    int di[4] = {-1,0,1,0};
    int dj[4] = {0,1,0,-1};
    int minAround = 1001;
    int cnt = 0;
    for(int k =0;k<4;k++){
        int ik = i+di[k];
        int jk = j+dj[k];
        if(ik>=0 && ik<n && jk>=0 && jk<m){
            minAround = min(minAround,T[ik][jk]);
            maxVal += T[ik][jk];
            cnt += 1;
        }
    }

    int ans = DFS(visited,i,j,4);
    if (cnt==4){
        maxVal -= minAround;
        return max(ans,maxVal);
    }else if(cnt == 3){
        return max(ans,maxVal);
    }else{
        return ans;
    }
        
}

int DFS(vector<vector<int> > &visited,int i, int j,int len){
    if (len == 1)
        return T[i][j];
    visited[i][j] = 1;
    int di[4] = {-1,0,1,0};
    int dj[4] = {0,1,0,-1};
    int ans = 0;
    for(int k =0;k<4;k++){
        int ik = i+di[k];
        int jk = j+dj[k];
        if(ik>=0 && ik<n && jk>=0 && jk<m && visited[ik][jk] == 0){
            ans = max(ans,DFS(visited,ik,jk,len-1));
        }
    }
    visited[i][j] = 0;
    return ans + T[i][j];
}
