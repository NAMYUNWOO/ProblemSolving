#include <iostream>
#include<stdio.h>
#include<vector>
using namespace std;

vector<vector<int>>DP;
vector<int>V;
int N,S,M;
int getAns(int,int);

int main(){
    
    
    DP.assign(101,vector<int>(1001,-2));
    scanf("%d",&N);
    scanf("%d",&S);
    scanf("%d",&M);
    int P;
    for (long i = 0 ; i < N; i++){
        scanf("%d",&P);
        V.push_back(P);
    }
    cout<<getAns(0,S)<<endl;
    
    return 0;
}
int getAns(int idx,int p){
    if ((p < 0)||(p > M)){
        return -1;
    }
    if (idx == N){
        return p;
    }
    if(DP[idx][p] != -2){
        return DP[idx][p];
    }
    int cand1 = getAns(idx+1,p+V[idx]);
    int cand2 = getAns(idx+1,p-V[idx]);
    if (cand1 > cand2){
        DP[idx][p] = cand1;
        return DP[idx][p];
    }
    DP[idx][p] = cand2;
    return DP[idx][p];
}
