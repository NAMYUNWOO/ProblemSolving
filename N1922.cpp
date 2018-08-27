#include <stdio.h>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
struct Edge{
    int start;
    int end;
    int cost;
    Edge():start(0),end(0),cost(0){

    }
    Edge(int start,int end,int cost): start(start),end(end),cost(cost){

    }
    bool operator < (const Edge &other) const {
        return cost>other.cost;
    }
};

vector<vector<pair<int,int> > > T;
vector<bool> visited;
priority_queue<Edge> myQ;

int main(){
    int n,m;
    scanf("%d ",&n);
    scanf("%d ",&m);
    T.resize(n+1);
    visited.assign(n+1,false);
    int s,e,c;
    for (int i = 0;i<m;i++){
        scanf("%d %d %d",&s,&e,&c);
        T[s].push_back(make_pair(e,c));
        T[e].push_back(make_pair(s,c));
    }
    visited[1] = true;
    for(int i = 0;i<T[1].size();i++){
        myQ.push(Edge(1,T[1][i].first,T[1][i].second));
    }
    int ans = 0;
    for(int ec = 0;ec<n-1;ec++){
        Edge e;
        while(!myQ.empty()){
            e = myQ.top();
            myQ.pop();
            if(visited[e.end] == false){
                break;
            }
        }
        visited[e.end] = true;
        ans += e.cost;
        int x = e.end;
        for (int i = 0;i<T[x].size();i++){
            myQ.push(Edge(x,T[x][i].first,T[x][i].second));
        }
    }
    printf("%d",ans);
    return 0;

}
