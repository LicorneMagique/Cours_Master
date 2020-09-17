#include <iostream>
#include "String.h"

int main()
{
  String s1;
  String s2('r');
  String s3("NOEL");
  std::cout <<"1 "<< s1 <<" 2 "<< s2 <<" 3 "<< s3 << std::endl;
  s3+=s2;
  std::cout<<"3+=2 "<< s3 << std::endl;
  std::cout<<"3+3 "<<s3+s3 << std::endl;
  return 0;
}
