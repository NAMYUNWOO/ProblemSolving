# include<cstdio>
# include<vector>
# include<algorithm>
using namespace std;
vector<vector<int> >T;
int getAns(int,int);
int ans = 0;
int n,m;
int main(){
    scanf("%d %d",&n,&m);
    T.assign(n+1,vector<int>(m+1,0));
    for(int i = 1;i<=n;i++){
        for (int j = 1;j<=m;j++){
            scanf("%1d", &T[i][j]);
        }
    }
    for (int i = 1 ; i<=n;i++){
        for(int j = 1;j<=m;j++){
            if (T[i][j] != 0){
                T[i][j] = min(T[i-1][j],min(T[i-1][j-1],T[i][j-1]))+1;
                ans = max(ans,T[i][j]);
            }
        }
    }
    printf("%d\n",ans*ans);

    return 0;
}


