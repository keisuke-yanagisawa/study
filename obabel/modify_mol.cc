#include <iostream>
#include <string>
#include <sstream>

#include <openbabel/mol.h>
#include <openbabel/obconversion.h>

int main(int argc, char** argv){

  // smilesからOBMolを生成
  std::string smiles = "c1ccc2ccccc2c1";
  std::stringstream ss(smiles);
  OpenBabel::OBConversion conv(&ss);
  conv.SetInFormat("smi");
  OpenBabel::OBMol mol;
  conv.Read(&mol);

  // OBMolのAtomsを出力
  std::cout << "Atom information" << std::endl;
  std::cout << "AtomId AtomIdx" << std::endl;
  for(OpenBabel::OBAtomIterator ait = mol.BeginAtoms(); ait!=mol.EndAtoms(); ++ait){
    std::cout << (*ait)->GetId()
              << " "
              << (*ait)->GetIdx()
              << std::endl;
  }
  std::cout << std::endl;


  // OBMolのBondsを出力
  std::cout << "Bond information" << std::endl;
  std::cout << "BeginAtomIdx EndAtomIdx" << std::endl;
  for(OpenBabel::OBBondIterator bit = mol.BeginBonds(); bit!=mol.EndBonds(); ++bit){
    std::cout << (*bit)->GetBeginAtomIdx()
              << " "
              <<(*bit)->GetEndAtomIdx()
              << std::endl;
  }
  return 0;
}
