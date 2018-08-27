# include<stdio.h>
# include<stdlib.h>
# include <algorithm>  

using namespace std;
int T[2][15] = {0};
int dp[15] = {0};
int getAns(int,int);
int main(){
    int n;
    scanf("%d",&n);
    for(int i =0;i<n;i++){
        scanf("%d %d",&T[0][i],&T[1][i]);
    }
    int max_val = 0;
    for(int i = 0;i<n;i++)
        max_val = max(getAns(i,n),max_val);
    printf("%d\n",max_val);

}
int getAns(int i,int n){
    if(T[0][i]+i-1>=n){
        return 0;
    }
    if(dp[i]!= 0)
        return dp[i];
    
    int ans = 0;
    for (int j = i+T[0][i];j<n;j++)
        ans = max(getAns(j,n), ans);
    dp[i] = T[1][i] + ans;
    return dp[i];
}
