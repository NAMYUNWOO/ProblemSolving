#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;
vector< vector<int> > T;
vector<bool> visited;
void DFS(int);
void BFS(int);
int main(){
    int n,m,sn;
    int node1,node2;
    scanf("%d %d %d",&n,&m,&sn);
    T.resize(n+1);
    visited.assign(n+1,false);
    for(int i = 0;i<m;i++){
        scanf("%d %d",&node1,&node2);
        T[node1].push_back(node2);
        T[node2].push_back(node1);
    }
    for(int i = 1;i<T.size();i++)
        sort(T[i].begin(), T[i].end());
    DFS(sn);
    printf("\n");
    visited.clear();
    visited.assign(n+1,false);
    BFS(sn);
    printf("\n");
    return 0;
}
void BFS(int n){
    int front;
    int next;
    queue<int> myQ;
    visited[n] = true;
    myQ.push(n);
    while(!myQ.empty()){
        front = myQ.front();
        printf("%d ",front);
        myQ.pop();
        for(int i = 0;i<T[front].size();i++){
            next = T[front][i];
            if(visited[next]==false){
                visited[next]=true;
                myQ.push(next);
            }
        }
        
    }
    
}
void DFS(int n){
    printf("%d ",n);
    int next;
    visited[n] = true;
    for(int i = 0;i<T[n].size();i++){
        next = T[n][i];
        if(visited[next]== false){
            DFS(next);
        }
    }
}

