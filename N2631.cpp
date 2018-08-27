# include<stdio.h>
# include<vector>
# include<algorithm>
using namespace std;

vector<int> arr;
vector<int>dp;
int getAns(int,int);
int maxVal= 0;
int main(){
    int n;
    scanf("%d",&n);
    arr.assign(n,0);
    for (int i = 0 ; i<n;i++)
        scanf("%d",&arr[i]);
    dp.assign(n,1);
    for (int i = 0; i < n; i++) {
        if (dp[i] == 0)dp[i] = 1;
        for (int j = 0; j < i; j++) {
            if (arr[i] > arr[j]) {
                if (dp[i] < dp[j] + 1) {
                    dp[i] = dp[j] + 1;
                    maxVal = max(dp[i],maxVal);
                }
            }
        }
    }
    printf("%d",n-maxVal);
}
