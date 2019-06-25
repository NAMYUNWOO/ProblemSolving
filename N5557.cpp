#include <iostream>
# include<stdio.h>
# include<vector>
using namespace std;

vector<vector<long>>DP;
vector<long>vec;
long num;
long getAns(long,long);
int main(){
    
    scanf("%d",&num);
    DP.assign(9001,vector<long>(101,-1));
    vec.assign(101,0);
    for (long i = 0 ; i < num; i++){
        scanf("%d",&vec[i]);
    }
    long ans = getAns(vec[num-1],num-2);
    printf("%ld",ans);
    return 0;
}
long getAns(long i,long j){
    
    if (j==0){
        if(i == vec[j]){
            return 1;
        }else{
            return 0;
        }
    }
    if (DP[i][j] != -1){
        return DP[i][j];
    }
    long minusLeft = i - vec[j];
    long plusLeft = i + vec[j];
    long ans = 0;
    if (plusLeft <= 20 ){
        ans += getAns(plusLeft,j-1);
    }
    
    if (minusLeft >= 0 ){
        ans += getAns(minusLeft,j-1) ;
    }
    DP[i][j] = ans;
    return ans;
}
