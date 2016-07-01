#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/io.hpp>

#include <iostream>

using namespace boost::numeric;

int main(){
  ublas::vector<double> vec_d(3);
  ublas::matrix<double> mat_d(3,3);
  vec_d[1] = 10;
  mat_d(0,0) = 1;
  mat_d(1,1) = 2;
  mat_d(2,2) = 3;
  std::cout << ublas::inner_prod(vec_d, ublas::prod(vec_d, mat_d)) << std::endl;

  return 0;
}
