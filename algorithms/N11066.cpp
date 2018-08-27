# include <stdio.h>
# include <vector>
# include <algorithm>
using namespace std;
int T[503];
int getAns(int,int);
vector<vector<int> >DP;
int n;
int main(){
  int tc;
  scanf("%d",&tc);
  int ans;
  for (int i = 0; i<tc;i++){
    scanf("%d",&n);
    DP.assign(n+1,vector<int>(n+1,0));
    for(int j = 1;j<=n;j++)
      scanf("%d",&T[j]);
    ans = getAns(1,n);
    printf("%d\n",ans);
  }
}

int getAns(int i,int j){
    if (i >= j){
        return 0;
    }
    if (i+1 == j){
        return T[i]+T[j];
    }
    if (DP[i][j]!=0)
        return DP[i][j];
    for (int k = i ; k<=j ; k ++)
        DP[i][j] += T[k];
    int minVal = getAns(i,i) + getAns(i+1,j);
    for (int k = i+1;k<j;k++){
        minVal = min(getAns(i,k)+getAns(k+1,j),minVal);
    }
    DP[i][j] += minVal;
    return DP[i][j];
}
