# include <stdio.h>
# include <vector>
# include <algorithm>
# define BIGN 1000000000
using namespace std;
vector<vector<int> > T;
vector<vector<int> >DP;
int go(int,int);
int N;
int main(){
    scanf("%d",&N);
    T.assign(N,vector<int>(N,0));
    DP.assign(1<<20,vector<int>(N,BIGN));
    for (int i = 0;i<N;i++)
        DP[1][i] = 0;
    
    for (int i = 0;i<N;i++){
        for (int j = 0;j<N;j++){
            scanf("%d",&T[i][j]);
        }
    }
    int ans= BIGN;
    for (int i = 0;i<N;i++){
        if (T[i][0] != 0){
            ans = min(ans,go((1<<N)-1,i)+T[i][0]);
        }
    }
    printf("%d\n",ans);
    return 0;
}
int go(int status,int current){
    if (status == 1){
        return DP[status][current];
    }
    if (DP[status][current] != BIGN)
        return DP[status][current];
    if (status&(1<<current)){
        for(int i = 0;i<N;i++){
            if (i != current && (status&(1<<i)) && T[i][current])
                DP[status][current] = min(DP[status][current], go(status-(1<<current),i)+T[i][current]);
        }
    }

    return DP[status][current];
}
