#include <stdio.h>
#include <vector>
using namespace std;
int getAns(int,int);
int T[1000001];
vector<vector<int> > DP;
int main(){
    int n;
    scanf("%d",&n);
    DP.assign(n+1,vector<int>(n+1,-1));
    for (int i = 1;i<=n;i++)
        scanf("%d",&T[i]);
    int testCase;
    scanf("%d",&testCase);
    int i,j;
    int ans;
    for(int k = 0;k<testCase;k++){
        scanf("%d %d",&i,&j);
        ans = getAns(i,j);
        printf("%d\n",ans);
    }

}

int getAns(int i,int j){
    if(i==j)
        return 1;
    if(j-i == 1 && T[i] == T[j])
        return 1;
    else if (j-i == 1 && T[i] != T[j])
        return 0;
        
    if(DP[i][j] != -1)
        return DP[i][j];
    if (T[i] != T[j]){
        DP[i][j] = 0;
    }else{
        if(getAns(i+1,j-1) == 1)
            DP[i][j] = 1;
        else
            DP[i][j] = 0;
    }
    return DP[i][j];

}

