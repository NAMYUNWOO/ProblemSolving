#include <iostream>
# include<stdio.h>
# include<vector>
using namespace std;

vector<vector<vector<long>>>cache;
vector<long>vec;
long tc;
long getAns(long,long,long);
long endidx,k;
int main(){
    
    scanf("%d",&tc);
    cache.assign(2,vector<vector<long>>(101,vector<long>(101,-1)));
    
    for (long i = 0 ; i < tc; i++){
        scanf("%d",&endidx);
        scanf("%d",&k);
        --endidx;
        long ans = getAns(0,0,k)+getAns(0,1,k);
        cout<<ans<<endl;
    }
    
    return 0;
}
long getAns(long idx,long cur, long rest){
    if ((idx == endidx )&&(rest > 0)){
        return 0;
    }
    if (endidx - idx < rest){
        return 0;
    }
    if ((idx == endidx)&&(rest == 0)){
        return 1;
    }
    int iidx = endidx - idx;
    if (cache[cur][iidx][rest] != -1){
        return cache[cur][iidx][rest];
    }
    if (cur == 0){
        cache[cur][iidx][rest] = getAns(idx+1,1,rest) + getAns(idx+1,0,rest);
    }else{
        if (rest == 0){
            cache[cur][iidx][rest] = getAns(idx+1,0,rest);
        }else{
            cache[cur][iidx][rest] = getAns(idx+1,1,rest-1) + getAns(idx+1,0,rest);
        }

    }
    return cache[cur][iidx][rest];
}
