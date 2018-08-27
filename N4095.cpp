# include <stdio.h>
# include <vector>
# include <algorithm>
using namespace std;

vector<vector<int> > T;
vector<vector<int> > DP;
int main(){
    int n,m,maxVal;
    while (true){
        scanf("%d %d",&n,&m);
        if (n == 0 && m == 0)
            return 0;
        T.assign(n,vector<int>(m,0));
        DP.assign(n,vector<int>(m,0));
        for(int i =0;i<n;i++){
            for(int j = 0;j<m;j++){
                scanf("%d",&T[i][j]);
            }
        }
        maxVal = 0;
        for (int i = 0; i< n;i ++){
            for(int j = 0; j<m;j++){
                if(i == 0 || j == 0){
                    if(T[i][j] == 1)
                        DP[i][j] = 1;
                    maxVal = max(DP[i][j],maxVal);
                    continue;
                }
                if(T[i-1][j] != 1 || T[i][j-1] != 1 || T[i-1][j-1] != 1){
                    if(T[i][j] == 1)
                        DP[i][j] = 1;
                    maxVal = max(DP[i][j],maxVal);
                    continue;

                }
                if (T[i][j] == 1)
                    DP[i][j] = min(DP[i-1][j],min(DP[i][j-1],DP[i-1][j-1])) + 1; 
                else
                    DP[i][j] = 0;
                maxVal = max(DP[i][j],maxVal);
            }
        }
        printf("%d\n",maxVal);
    }
    return 0;
}
