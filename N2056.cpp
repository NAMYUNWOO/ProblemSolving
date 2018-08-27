# include <stdio.h>
# include <vector>
# include <queue>
# include <algorithm>
using namespace std;
# define MAXVAL 2000000
int cost[10000];
vector<int>T[10001];
vector<int>T2[10001];
vector<int> ind;
int DP[10001] ={0};
int main(){
    int n;
    scanf("%d",&n);
    ind.assign(n+1,0);
    int preCnt;
    int preWork;
    for(int i = 1;i<=n;i++){
        scanf("%d",&cost[i]);
        scanf("%d",&preCnt);
        for(int j = 0;j<preCnt;j++){
            scanf("%d",&preWork);
            T[preWork].push_back(i);
            ind[i] += 1;
        }
    }
    queue<int> myQ;
    for(int i = 1;i<=n;i++){
        if(ind[i] == 0){
            myQ.push(i);
            DP[i] = cost[i];
        }
    }
    while(!myQ.empty()){
        int current = myQ.front();
        myQ.pop();
        for(int i = 0;i<T[current].size();i++){ 
            int next = T[current][i];
            ind[next] -= 1;
            if (DP[next] < DP[current]+cost[next]) {
                DP[next] = DP[current]+cost[next];
            }
            if(ind[next] == 0){
                myQ.push(next);
            }
        }
    }
    int ans = 0;
    for (int i=1; i<=n; i++) {
        if (ans < DP[i]) {
            ans = DP[i];
        }
    }
    printf("%d\n",ans);
    return 0;
}
