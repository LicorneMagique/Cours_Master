//
//  main.cpp
//  GuerreDesLangages
//

#include <iostream>
#include <sstream> //std::istringstream
#include <chrono> //std::chrono::time_point
#include "image.h"
#include "pixel.h"

int main(int argc, const char * argv[])
{
    if(argc < 4)
    {
        std::cerr<<"Parametres a fournir : nombre de boucles hauteur largeur de l'image"<<std::endl;
        exit(0);
    }
    std::istringstream s1(argv[1]);
    std::istringstream s2(argv[2]);
    std::istringstream s3(argv[3]);
    
    int nb_loop=0;
    int L=0, C=0;
    
    if (!(s1 >> nb_loop))
        std::cerr << "Nombre de boucles invalide " << argv[1] << std::endl;
    if (!(s2 >> L))
        std::cerr << "Hauteur invalide " << argv[2] << std::endl;
    if (!(s3 >> C))
        std::cerr << "Largeur invalide" << argv[3] << std::endl;

    
    std::chrono::time_point<std::chrono::system_clock> start, end;
    
    Image im(C,L);
    //Image2 im(C,L);

    start = std::chrono::system_clock::now();
    for (int i=0;i<nb_loop;i++)
    {
        for (int l=0;l<L;l++)
        {
            for (int c=0;c<C;c++)
                im.get(l,c).r()=im.get(l,c).g()=im.get(l,c).b();
        }
    }
    end = std::chrono::system_clock::now();
    
    int elapsed_microseconds = std::chrono::duration_cast<std::chrono::microseconds> (end-start).count();
    std::cout << "Bonjour, suis-je performant? C++ Mode Release 1 " << nb_loop
        << " " << L << " " << C
        << " " << elapsed_microseconds << std::endl;
    return 0;
}


