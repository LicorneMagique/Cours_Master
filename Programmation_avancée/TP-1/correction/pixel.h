#ifndef PIXEL_INCLUDED
#define PIXEL_INCLUDED

class Pixel
{
private :
    unsigned char _r,_g,_b;
public :
    Pixel(): _r(0), _g(0), _b(0) {}
    unsigned char r() const {return _r;}
    unsigned char g() const {return _g;}
    unsigned char b() const {return _b;}
    unsigned char & r() {return _r;}
    unsigned char & g() {return _g;}
    unsigned char & b() {return _b;}
};

#endif // PIXEL_INCLUDED
