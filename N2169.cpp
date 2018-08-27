#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int n;
int m;
int MINLIMIT = -2000000000;
vector<vector<int>> table;
vector<vector<int>> dp[3];
vector<vector<int>> visited;
/*
action
	0:down
	1:left
	2:right
*/

int problem(int i,int j,int a){
    if (i == n-1 && j== m-1)
        return table[i][j];

	if (i<0 || j<0 || i>= n || j>= m)
		return MINLIMIT;

	/*
	if (visited[i][j])
		return MINLIMIT;
	*/

	if (dp[a][i][j] != MINLIMIT)
		return dp[a][i][j];

    int idxs[3][2] = {{i+1,j},{i,j-1},{i,j+1}}; //down,left,right
	int newi = idxs[a][0];
	int newj = idxs[a][1];

	//visited[i][j] = 1;
	if (a == 0)
		dp[a][i][j] = max(problem(newi,newj,0),max(problem(newi,newj,1),problem(newi,newj,2)))+table[i][j];
	else if (a==1)
		dp[a][i][j] = max(problem(newi,newj,0),problem(newi,newj,1))+table[i][j];
	else if (a==2)
		dp[a][i][j] = max(problem(newi,newj,0),problem(newi,newj,2))+table[i][j];
	//visited[i][j] = 0;

	return dp[a][i][j];
}

int main(int argc, char* argv[]) {
    cin>>n>>m;
    table.assign(n,vector<int>(m,-1));
	dp[0].assign(n,vector<int>(m,MINLIMIT));
	dp[1].assign(n,vector<int>(m,MINLIMIT));
	dp[2].assign(n,vector<int>(m,MINLIMIT));
	visited.assign(n,vector<int>(m,0));
    for(int i = 0; i<n;i++){
		for(int j = 0;j<m;j++){
			cin>>table[i][j];
		}

	}
	int ans1 = problem(0,0,0);
	int ans2 = problem(0,0,2);
    int ans = max(ans1,ans2);
    cout<<ans<<endl;
}
