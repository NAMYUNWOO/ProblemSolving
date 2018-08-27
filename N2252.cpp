# include <stdio.h>
# include <vector>
# include <queue>
# include <tuple>
# include <stdlib.h>
using namespace std;
vector<vector<int> > T;
vector<bool> visited;
queue<int> myQ;
int *pointed;
void topoSort();
int main(){
    int n,m,node1,node2;
    scanf("%d %d",&n,&m);
    pointed = (int *)malloc(sizeof(int)*(n+1));
    for(int i = 0; i<=n;i++)
        pointed[i] = 0;
    T.resize(n+1);
    visited.assign(n+1,false);
    for(int i = 0;i<m;i++){
        scanf("%d %d",&node1,&node2);
        T[node1].push_back(node2);
        pointed[node2] += 1;
    }
    for(int i = 1;i<T.size();i++)
        sort(T[i].begin(),T[i].end());
    for(int i = 1;i<=n;i++){
        if(pointed[i] == 0){
            myQ.push(i);
            visited[i] = true;
        }
    }
    topoSort();
    
}

void topoSort(){
    int front,next;
    while(!myQ.empty()){
        front = myQ.front();
        myQ.pop();
        printf("%d ",front);
        for(int i = 0;i<T[front].size();i++){
            next = T[front][i];
            pointed[next] -= 1;
            if(pointed[next] == 0){
                myQ.push(next);
            }
        }
        
    }
}
