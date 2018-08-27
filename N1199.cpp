# include<stdio.h>
# include<vector>
# include<cstdio>
using namespace std;
void getEulerCircuit(vector<int>&,int);
vector<vector<int> >T;
int main(){
    int n;
    scanf("%d",&n);
    T.assign(n+1,vector<int>(n+1,0));
    int startNode = 0;
    for (int i = 1; i<=n;i++){
        int rowSum = 0;
        for(int j = 1; j<=n;j++){
            scanf("%d",&T[i][j]);
            rowSum += T[i][j];
            if(startNode == 0 && T[i][j] == 1){
                startNode = i;
            }
        }
        if(rowSum %2 == 1){
            printf("-1\n");
            return 0;
        }

    }
    vector<int> circuit;
    getEulerCircuit(circuit,startNode);
    for(int i = (int)circuit.size()-1;i>=0;i--){
        printf("%d ",circuit[i]);
    }

}

void getEulerCircuit(vector<int>& circuit,int sNode){
    for(int eNode = 0;eNode < T.size();eNode ++){
        while(T[sNode][eNode] > 0){
            T[sNode][eNode]--;
            T[eNode][sNode]--;
            getEulerCircuit(circuit,eNode);
        }
    } 
    circuit.push_back(sNode);
}
