#ifndef IMAGE_INCLUDED
#define IMAGE_INCLUDED

#include <iostream>
#include "pixel.h"

class Image
{
private :
    Pixel * im;
    unsigned int width, height;
public :
    Image() : im(nullptr), width(0), height(0) {}
    Image(int w, int h) : width(w), height(h)
    {
        try{im=new Pixel[w*h];}
            catch(std::bad_alloc& ba){std::cout << "bad_alloc caught: " << ba.what() << '\n';}
    }
    const Pixel & get(unsigned int row, unsigned int col) const {return im[row*width+col];}
    Pixel & get(unsigned int row, unsigned int col){return im[row*width+col];}
    ~Image() {delete im;}
};

class Image2
{
private :
    Pixel ** im;
    unsigned int width, height;
public :
    Image2() : im(nullptr), width(0), height(0) {}
    Image2(unsigned int w,unsigned int h) : width(w), height(h)
    {
        try {im=new Pixel*[w*h]; for(unsigned int i=0; i<w*h ; i++) im[i]= new Pixel();}
        catch(std::bad_alloc& ba){std::cout << "bad_alloc caught: " << ba.what() << '\n';}
    }
    const Pixel & get(unsigned int row, unsigned int col) const {return *im[row*width+col];}
    Pixel & get(unsigned int row, unsigned int col){return *im[row*width+col];}
    ~Image2()
    {
        if(im!=nullptr)
        {
            for(unsigned int i=0; i<width*height ; i++) delete im[i];
            delete [] im;
        }
        else{std::cout << "Bip" << std::endl;}
    }
};

#endif // IMAGE_INCLUDED
