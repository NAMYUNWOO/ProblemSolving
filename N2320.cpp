# include <stdio.h>
# include <iostream>
# include <cstring>
# include <string>
# include <vector>
# include <queue>
# include <algorithm>
using namespace std;
priority_queue<int> graph[5][5];
int max_val = 0;
void getMax(int,int,int *);
int main(){
    int n;
    int alphabat[150] = {0};
    alphabat['A']  = 0;
    alphabat['E']  = 1;
    alphabat['I']  = 2;
    alphabat['O']  = 3;
    alphabat['U']  = 4;
    scanf("%d",&n);
    string str;
    for (int i = 0;i<n;i++){
        cin>>str;
        int idxI = alphabat[str[0]];
        int idxJ = alphabat[str[(int)str.size()-1]];
        graph[idxI][idxJ].push((int)str.size());
    }
    int ans = 0;
    for (int i = 0; i<5;i++){
        for(int j = 0; j<5;j++){
            if(!graph[i][j].empty()){
                getMax(i,j,&ans);
                ans = max(ans,max_val);
                max_val = 0;
            }
        }
    }
    printf("%d\n",ans);
    return 0;
}
void getMax(int i,int j,int *ans){
    int temp = graph[i][j].top();
    graph[i][j].pop();
    max_val += temp;
    *ans = max(*ans,max_val);
    for(int idx = 0;idx<5;idx++){
        if(!graph[j][idx].empty()){
            getMax(j,idx,ans);
        }
    }
    max_val -= temp;
    graph[i][j].push(temp);
}
