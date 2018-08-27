#include <vector>

using namespace std;

int MOD = 20170805;
int solution(int m, int n, vector<vector<int> > city_map) {
    int DP[500][500] = {0};
    DP[0][0] = 1;
    for(int i = 1;i<m;i++){
        if(a[i][0] == 0){
            DP[i][0] = DP[i-1][0];
        }else if(a[i][0] == 1){
            DP[i][0] = 0;
        }else{
            DP[i][0] = DP[i-1][0];
        }  
    }
    for(int j = 1;j<m;j++){
        if(a[0][j] == 0){
            DP[0][j] = DP[0][j-1];
        }else if(a[0][j] == 1){
            DP[0][j] = 0;
        }else{
            DP[0][j] = DP[0][j-1];
        }  
    }
    for (int i = 1; i<m;i++){
        for(int j = 1; j<n;j++){
            if(city_map[i][j] == 1)
                DP[i][j] = 0;
            else{
                DP[i][j] = DP[i][j-1]+DP[i-1][j];
                if (a[i-1][j] == 2)
                    DP[i][j] -= DP[i-1][j-1];
                if(a[i][j-1] == 2)
                    DP[i][j] -= DP[i-1][j-1];
            }
        }
    } 
}
