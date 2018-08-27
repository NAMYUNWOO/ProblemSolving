#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
void bfs(vector<vector<int> > &, int, int,int);
vector<vector<bool> >check;

int ans = 0;
int gm,gn;
vector<int> solution(int m, int n, vector<vector<int> > picture) {
    gm = m;
    gn = n;
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    check.assign(n,vector<bool>(m,false));
    for (int i = 0;i<m;i++){
        for(int j = 0; j<n;j++){
            if(picture[i][j] != 0){
                bfs(picture,i,j,picture[i][j]);
                max_size_of_one_area = max(ans,max_size_of_one_area);
                ans = 0;
                number_of_area += 1;
            }
        }
    }
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}

void bfs(vector<vector<int> > &a,int i,int j,int color) {
    queue<pair<int,int> > q;
    check[i][j] = true;
    a[i][j] = 0;
    q.push(make_pair(i,j));
    int dx[4] = {-1,0,1,0};
    int dy[4] = {0,1,0,-1};
    while (!q.empty()) {
        pair<int,int> node = q.front();
        q.pop();
        ans += 1;
        int curI = node.first;
        int curJ = node.second;
        for (int k = 0;k<4;k++){
            int nextI = curI + dx[k];
            int nextJ = curJ + dy[k];
            if(nextI >=0 && nextI < gm && nextJ >=0 && nextJ <gn && a[nextI][nextJ] == color && check[nextI][nextJ] == false){
                check[nextI][nextJ] = true;
                a[nextI][nextJ] = 0;
                q.push(make_pair(nextI,nextJ));
            }
        }
    }
}
