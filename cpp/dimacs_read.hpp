#include <boost/numeric/ublas/symmetric.hpp>
#include <vector>
#include <string>

#ifndef DIMACS_READ_H_
#define DIMACS_READ_H_

namespace myutil {
  using namespace boost::numeric;
  
  std::vector<std::string> split(const std::string &s, char delim);
  const ublas::symmetric_matrix<bool> read_data(std::string filename);
  
}

#endif
