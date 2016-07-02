#include <boost/numeric/ublas/symmetric.hpp>
#include <boost/numeric/ublas/matrix_proxy.hpp>
#include <boost/numeric/ublas/io.hpp>

#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <stack>

#include "dimacs_read.hpp"

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

int solve(const ublas::symmetric_matrix<bool> &adj){
  int num_vertex = adj.size1();
  std::stack<job*> st;
  
  //initialize
  for(int i=0; i<num_vertex; i++){//making initial state
    st.push(new job(i));
  }

  // searching mcs based on DFS
  while(!st.empty()){
    job* now = st.top();
    st.pop();


    ublas::vector<bool> temp(num_vertex);
    std::fill(temp.begin(), temp.end(), true);
    
    for(std::vector<int>::iterator iter = now->v.begin(); iter != now->v.end(); iter++){
      temp = ublas::element_prod(temp, ublas::row(adj, *iter));
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

int main(int argc, char *argv[]){
  ublas::symmetric_matrix<bool> adj_m = myutil::read_data(argv[1]);
  
  solve(adj_m);
  
}
