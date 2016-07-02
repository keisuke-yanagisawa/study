#include <boost/numeric/ublas/symmetric.hpp>
#include <boost/numeric/ublas/matrix_proxy.hpp>
#include <boost/numeric/ublas/io.hpp>

#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <stack>

#define NUM_VERTEX 5

using namespace boost::numeric;

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

int solve(int num_vertex, const ublas::symmetric_matrix<bool> &adj, std::stack<job*> &st){
  while(!st.empty()){
    job* now = st.top();
    st.pop();


    ublas::vector<bool> temp(num_vertex);
    std::fill(temp.begin(), temp.end(), true);
    
    for(std::vector<int>::iterator iter = now->v.begin(); iter != now->v.end(); iter++){
      temp = ublas::element_prod(temp, ublas::row(adj, *iter));
      std::cout << temp << std::endl;
    }

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
  ublas::symmetric_matrix<bool> adj_m(num_vertex, num_vertex);
  adj_m(0,2) = 1;
  adj_m(0,4) = 1;
  adj_m(1,2) = 1;
  adj_m(1,3) = 1;
  adj_m(2,3) = 1;
  
  std::stack<job*> st;
  for(int i=0; i<num_vertex; i++){//making initial state
    st.push(new job(i));
  }

  solve(num_vertex, adj_m, st);
  
}
