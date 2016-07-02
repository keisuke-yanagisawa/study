#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <stack>

#define NUM_VERTEX 5

struct job{
  std::vector<int> v;
  job(int vertex){v.push_back(vertex);}
  job(){}
};

void output(std::vector<int> v){
  for (std::vector<int>::iterator i = v.begin(); i != v.end(); ++i)
    std::cout << *i << ' ';
  std::cout << std::endl;
}
void output(bool a[NUM_VERTEX]){
  for(int i=0; i<NUM_VERTEX; i++){
    std::cout << a[i] << " ";
  }
  std::cout << std::endl;
}

int solve(int num_vertex, const bool adj[NUM_VERTEX][NUM_VERTEX], std::stack<job*> &st){
  while(!st.empty()){
    job* now = st.top();
    st.pop();

    bool temp[num_vertex];
    for(int i=0; i<num_vertex; i++){
      temp[i] = true;
    }
    
    for(std::vector<int>::iterator iter = now->v.begin(); iter != now->v.end(); iter++){
      for(int i=0; i<num_vertex; i++){
	temp[i] &= adj[*iter][i];
      }
    }

    output(temp);

    for(int i=0; i<now->v.back(); i++){
      if(temp[i]){
	job* newjob = new job();
	newjob->v = now->v;
	newjob->v.push_back(i);
	st.push(newjob);
      }
    }
    
    output(now->v);
  }
}

int main(){
  int num_vertex = NUM_VERTEX;
  bool adj[NUM_VERTEX][NUM_VERTEX] = {{0,0,1,0,1},
				      {0,0,1,1,0},
				      {1,1,0,1,0},
				      {0,1,1,0,0},
				      {1,0,0,0,0}};

  std::stack<job*> st;
  for(int i=0; i<num_vertex; i++){//making initial state
    st.push(new job(i));
  }

  solve(num_vertex, adj, st);
  
}
