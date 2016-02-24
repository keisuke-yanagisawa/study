#include <iostream>
#include <string>
#include <sstream>

#include <openbabel/mol.h>
#include <openbabel/obconversion.h>
#include <openbabel/generic.h>

int main(int argc, char** argv){

  // smilesからOBMolを生成
  std::ifstream ifs("./data/test.sdf");
  OpenBabel::OBConversion in_conv(&ifs);
  in_conv.SetInFormat("sdf");
  OpenBabel::OBMol mol;
  in_conv.Read(&mol);

  std::cout << mol.GetData("i_m_source_file_index")->GetValue() << std::endl;
  //これで情報の読み込みができる

  OpenBabel::OBPairData* comment = new OpenBabel::OBPairData();
  comment->SetValue("Test");     // 内容
  comment->SetAttribute("test"); // 題名
  mol.SetData(comment);

  std::ofstream ofs("hoge.sdf");
  OpenBabel::OBConversion out_conv;
  out_conv.SetOutFormat("sdf");
  out_conv.Write(&mol, &ofs);

  return 0;
}
