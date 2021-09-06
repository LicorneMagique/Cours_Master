/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package helloworld;

/**
 *
 * @author raphaelle
 */
public class Pixel {
  private 
    byte _r,_g,_b;
  public Pixel(){_r=0; _g=0; _b=0; }
  public byte r() {return _r;}
  public byte g() {return _g;}
  public byte b() {return _b;}
  public void setr(int r) {
      int tmp = r & 0xff;
      _r=(byte) ((tmp & 0x80) == 0 ? tmp : tmp - 256);} 
  public void setg(int g) {
      int tmp = g & 0xff;
      _g=(byte) ((tmp & 0x80) == 0 ? tmp : tmp - 256);}
  public void setb(int b) {
      int tmp = b & 0xff;
      _b=(byte) ((tmp & 0x80) == 0 ? tmp : tmp - 256);}
}

//// (byte) (my_char&0x00FF); int c = 0xff & b ;
