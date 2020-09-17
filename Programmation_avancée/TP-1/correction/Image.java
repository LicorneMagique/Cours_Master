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
public class Image {
    private Pixel im[];
    int width, height;// Java doesn't deal with unsigned types

    public Image() {
        im = null;
        width = 0;
        height = 0;
    }

    Image(int w, int h) {
        width = w;
        height = h;
        im = new Pixel[w * h]; // may throw OutOfMemoryError
        for (int i = 0; i < w * h; i++)
            im[i] = new Pixel();
    }

    Pixel get(int row, int col) {
        return im[row * width + col];
    }

    int getWidth() {
        return width;
    }

    int getHeigth() {
        return height;
    }
}
