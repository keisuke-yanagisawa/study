#include <boost/numeric/ublas/io.hpp>

#include <fstream>
#include <sstream>

#include "dimacs_read.hpp"

using namespace boost::numeric;

std::vector<std::string> split(const std::string &s, char delim) {
  std::vector<std::string> elems;
  std::stringstream ss(s);
  std::string item;
  while (getline(ss, item, delim)) {
    if (!item.empty()) {
      elems.push_back(item);
    }
  }
  return elems;
}


const ublas::symmetric_matrix<bool> read_data(std::string filename){
  ublas::symmetric_matrix<bool> adj;
  
  std::ifstream ifs(filename.c_str());
  if(ifs.fail()){
    std::cout << "Failed opening file." << std::endl;
  }

  std::string str;
  while(std::getline(ifs, str)){
    if(str[0]=='p'){
      std::vector<std::string> temp = split(str, ' ');
      int num_vertex = std::atoi(temp[2].c_str());
      adj = *(new ublas::symmetric_matrix<bool>(num_vertex, num_vertex));
    }else if(str[0]=='e'){
      std::vector<std::string> temp = split(str, ' ');
      int v1 = std::atoi(temp[1].c_str());
      int v2 = std::atoi(temp[2].c_str());
      adj(v2-1,v1-1) = true;
    }
  }

  return adj;
}

int main(){
  std::cout << read_data("data/C125.9.clq") << std::endl;

  return 0;
}
/*
int solve(const ublas::symmetric_matrix<bool> &adj){
  int num_vertex = adj.size1();
  std::stack<job*> st;
  
  //initialize
  for(int i=0; i<num_vertex; i++){//making initial state
    st.push(new job(i));
  }

  // searching mcs based on DFS
  while(!st.empty()){
*/
