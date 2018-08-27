#include <stdio.h>
#include <vector>
using namespace std;
vector<vector<int>> T;
vector<bool> visit;
int dfs(int n,int len);
int main(){
    int n,m;
    int f1,f2;
    int result;
    scanf("%d %d",&n,&m);
    T.resize(n);
    for(int i = 0; i<m;i++){
        scanf("%d %d",&f1,&f2);
        T[f1].push_back(f2);
        T[f2].push_back(f1);
    }
    for (int i = 0 ;i<n;i++){
        visit.assign(n, false);
        result = dfs(i, 0);
        if(result >= 4){
            printf("1\n");
            return 0;
        }
    }
    printf("0\n");
    return 0;
    
        
}

int dfs(int node,int len){
    visit[node] = true;
    if (len >=4)
        return len;
    int ans = len;
    for(int i = 0;i<T[node].size();i++){
        if(visit[T[node][i]] == false){
            ans = max(ans,dfs(T[node][i],len+1));
            
        }
    }
    visit[node] = false;
    return ans;
    
}



