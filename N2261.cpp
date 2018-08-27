# include <stdio.h>
# include <algorithm>
# include <vector>
# include <cmath>
using namespace std;
vector<pair<int,int> >V;
int getMinDist(int,int);
int getDist(pair<int,int>,pair<int,int>);
int main(){
    int n;
    scanf("%d",&n);
    int x,y;
    for(int i = 0;i<n;i++){
       scanf("%d %d",&x,&y);
       V.push_back(pair<int,int>(x,y));
    }
    sort(V.begin(),V.end());
    int ans = getMinDist(0, n-1);
    printf("%d",ans);
}
int getMinDist(int start, int end){
    int ans;
    if (end - start == 1){

        //dp[start][end] =  pow(V[end].first - V[start].first,2)+ pow(V[end].second - V[start].second,2);
        //return dp[start][end];
        ans =  (V[end].first - V[start].first)*(V[end].first - V[start].first)+ (V[end].second - V[start].second)*(V[end].second - V[start].second);
        return ans;
    }
    if (end - start == 2){
        int candi1 = getMinDist(start,end-1);
        int candi2 = getMinDist(start+1,end);
        //int candi1 = pow(V[end].first - V[start+1].first,2)+ pow(V[end].second - V[start+1].second,2);
        //int candi2 = pow(V[end-1].first - V[start].first,2)+ pow(V[end-1].second - V[start].second,2);
        //dp[start][end] = min(candi1,candi2);
        //return dp[start][end];
        ans = min(candi1,candi2);
        return ans;
    }
    if (end - start == 3){
        int candi1 = getMinDist(start,end-2);
        int candi2 = getMinDist(start+1,end-1);
        int candi3 = getMinDist(start+2,end);
        //int candi1 = pow(V[end].first - V[start+2].first,2)+ pow(V[end].second - V[start+2].second,2);
        //int candi2 = pow(V[end-1].first - V[start+1].first,2)+ pow(V[end-1].second - V[start+1].second,2);
        //int candi3 = pow(V[end-2].first - V[start].first,2)+ pow(V[end-2].second - V[start].second,2);
        //dp[start][end] = min(min(candi1,candi2),candi3);
        //return dp[start][end];
        ans = min(min(candi1,candi2),candi3);
        return ans;
    }
    int mid = (end+start)/2;
    int candi1 = getMinDist(start,mid);
    int candi2 = getMinDist(mid+1,end);
    int minVal = min(candi1,candi2);
    vector<pair<int,int> > temp;
    for (int i = mid-1;i>= 0;i--){
        if(pow(V[mid].first - V[i].first,2) > minVal){
            temp.push_back(pair<int,int>(V[i].first,V[i].second));
            break;
        }else{
            temp.push_back(pair<int,int>(V[i].first,V[i].second));
        }
    }
    for (int i = mid+1; i<=end; i++){
        if(pow(V[i].first - V[mid].first,2) > minVal){
            temp.push_back(pair<int,int>(V[i].first,V[i].second));
            break;
        }else{
            temp.push_back(pair<int,int>(V[i].first,V[i].second));
        }
    }
    sort(temp.begin(),temp.end());
    int m = temp.size(); 
    for(int i = 0;i<m-1;i++){
        for(int j = i+1;j<m;j++){
            int y = temp[j].second - temp[i].second;
            int x = temp[j].first - temp[i].first;
            if (y*y >= minVal || x*x >= minVal){
                break;
            }else{
                minVal = min(minVal,getDist(temp[i],temp[j]));
            }
        }
    }

    return minVal;
}

int getDist(pair<int,int> i ,pair<int,int> j){
    return (j.first - i.first)*(j.first - i.first) + (j.second - i.second)*(j.second - i.second);

}
