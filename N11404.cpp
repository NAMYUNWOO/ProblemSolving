# include<stdio.h>
# include<vector>
# include<queue>
# include<algorithm>
# include <limits.h>

using namespace std;
int getMinCost(int,int,int);
vector<vector<long long> > cost;
int n,m;
int main(){
    int i,j;
    long long val;
    scanf("%d",&n);
    scanf("%d",&m);
    cost.assign(n+1,vector<long long>(n+1,INT_MAX));
    for(int k = 1;k<=m;k++){
        scanf("%d %d %lld",&i,&j,&val);
        cost[i][j] = min(cost[i][j],val);
    }
    for(int i = 1; i<=n;i++)
        cost[i][i] = 0;
    for (int k = 1;k<=n;k++)
        for (int i = 1;i<=n;i++)
            for (int j = 1;j<=n;j++)
                cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j]);

    for(int i  = 1 ;i<=n;i++){
        for(int j = 1 ;j<=n;j++){
            printf("%lld ",cost[i][j]);
        }
        printf("\n"); 
    }

}

