#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> DP;
int getAns(int);
int main(){
    int n,m,s,e;
    int ans =1;
    scanf("%d",&n);
    scanf("%d",&m);
    s = 0;
    for (int i = 0;i<m;i++){
        scanf("%d",&e);
        DP.assign(e-s,1);
        ans *= getAns(e-s-1);
        s = e;
    }
    e = n+1;
    DP.assign(e-s,1);
    ans *= getAns(e-s-1);
    printf("%d\n",ans);
    return 0;
}
int getAns(int len){
    
    if (len < 0)
        return 0;
    if (len  == 0 || len == 1)
        return 1;
    if (len == 2)
        return 2;
    if (DP[len] != 1)
        return DP[len];

    DP[len] = getAns(len-2)*2 + getAns(len-3);
    return DP[len];

}
