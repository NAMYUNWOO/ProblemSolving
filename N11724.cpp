#include <stdio.h>
#include <vector>
using namespace std;
vector<vector<int> >T;
vector<bool> visited;
void dfs(int);
int main(){
    int n,m;
    int sum = 0;
    scanf("%d %d",&n,&m);
    T.resize(n+1);
    visited.assign(n+1,false);
    int node1,node2;
    for(int i =0 ;i<m;i++){
       scanf("%d %d",&node1,&node2);
       T[node1].push_back(node2);
       T[node2].push_back(node1);
    }
    for(int i = 1;i<=n;i++){
        if(visited[i] == false){
            ++sum;
        }
        dfs(i);
    }
    printf("%d\n",sum);
}
void dfs(int n){
    int next;
    visited[n]= true;
    for(int i = 0;i<T[n].size();i++){
        next = T[n][i];
        if(visited[next]==false)
            dfs(next);
    }
}
