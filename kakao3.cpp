#include <vector>

using namespace std;

int MOD = 20170805;
vector<vector<int> >a;
vector<vector<int> >DP;
int getAns(int i,int j){
    if (i == 0 && j == 0){
        return 1;
    }
    if (i<0 || j< 0){
        return 0;
    }
    if(DP[i][j] != -1){
        return DP[i][j];
    }

    if (a[i][j] == 1){
        DP[i][j] = 0;
        return DP[i][j];
    }
    DP[i][j] = 0;
    if (i-1>=0 && a[i-1][j] == 0){
        DP[i][j] += getAns(i-1,j);
    }else if(i-1 >= 0 && a[i-1][j] == 1){
        DP[i][j] += 0;
    }else{
        DP[i][j] += getAns(i-2,j);
        if (i-1 == 0)
            DP[i][j] = getAns(i-1,j);
    }
    if (j-1 >= 0 && a[i][j-1] == 0){
        DP[i][j] = (DP[i][j]+getAns(i,j-1))%MOD;
    }else if(j-1 >= 0 && a[i][j-1] == 1){
        DP[i][j] += 0;
    }else{
        DP[i][j] =(DP[i][j]+getAns(i,j-2))%MOD;
        if (j-1 == 0)
            DP[i][j] = getAns(i,j-1);

    }
    return DP[i][j];

}
int solution(int m, int n, vector<vector<int>> city_map) {
    a = city_map;
    DP.assign(m,vector<int>(n,-1));
    int answer = 0;
    answer = getAns(m-1,n-1);
     
    return answer;
}
