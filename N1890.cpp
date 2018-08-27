#include <stdio.h>
#include <vector>
#include <string.h>
long long getAns(int,int);
long long T[105][105] ={0};
long long DP[105][105];
int main(){
    int n;
    scanf("%d",&n);
    for (int i =1;i<=n;i++){
        for (int j=1;j<=n;j++){
            scanf("%lld",&T[i][j]);
            DP[i][j] = -1;
        }
    }
    long long ans = getAns(n,n);
    printf("%lld\n",ans);
}
long long getAns(int i,int j){
    if(i == 1 && j == 1)
        return 1;
    if(DP[i][j]!= -1)
        return DP[i][j];
    for(int i2=0;i2<i;i2++){
        if(T[i2][j]+i2 == i)
            DP[i][j]+=getAns(i2,j);
    }
    for(int j2=0;j2<j;j2++){
        if(T[i][j2]+j2 == j)
            DP[i][j]+=getAns(i,j2);
    }
    ++DP[i][j];
    return DP[i][j];
}
