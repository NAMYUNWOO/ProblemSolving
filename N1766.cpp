# include <stdio.h>
# include<vector>
# include<queue>
using namespace std;
vector<vector<int> >T;
vector<int>ind;
int main(){
    int n,m;
    scanf("%d %d",&n,&m);
    T.resize(n+1);
    ind.assign(n+1,0);
    int x,y;
    for(int i = 0;i<m;i++){
       scanf("%d %d",&x,&y);
       T[x].push_back(y);
       ind[y] += 1;
    }
    priority_queue<int> myQ;
    for(int i = 1;i<=n;i++){
        if(ind[i] == 0){
            myQ.push(-i);
        }
    }
    while(!myQ.empty()){
        int x = - myQ.top();
        myQ.pop();
        printf("%d ",x);
        for(int i = 0;i<T[x].size();i++){
            int y = T[x][i];
            ind[y] -= 1;
            if(ind[y] == 0){
                myQ.push(-y);
            }
        }
    }
    return 0;
}
