#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <stack>

struct job{
  std::vector<int> v;
  job(int vertex){v.push_back(vertex);}
  job(){}
};

void output(std::vector<int> v){
  for (auto i = v.begin(); i != v.end(); ++i)
    std::cout << *i << ' ';
  std::cout << std::endl;
}

int solve(int num_vertex, const std::multimap<int, int> &e, std::stack<job*> &st){
  while(!st.empty()){
    job* now = st.top();
    st.pop();
    
    auto range = e.equal_range(now->v.back());
    //これだと直前のvertexしか見ていないけど、すべてのvertexを見て次のvertexを得ていいか決定しなければならない。
    for(auto iter = range.first; iter!=range.second; iter++){
      job* newjob = new job();
      newjob->v = now->v;
      newjob->v.push_back(iter->second);
      st.push(newjob);
    }
    
    output(now->v);
  }
}

int main(){
  int num_vertex = 5;
  std::multimap<int, int> e;

  e.insert(std::pair<int, int>(0,2));
  e.insert(std::pair<int, int>(0,4));
  e.insert(std::pair<int, int>(1,2));
  e.insert(std::pair<int, int>(1,3));
  e.insert(std::pair<int, int>(2,3));
  
  std::stack<job*> st;
  st.push(new job(0));
  st.push(new job(1));
  st.push(new job(2));
  st.push(new job(3));
  st.push(new job(4));  

  solve(num_vertex, e, st);
  
  std::cout << "test" << std::endl;

}
