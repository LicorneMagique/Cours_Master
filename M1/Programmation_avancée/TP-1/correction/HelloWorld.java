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
public class HelloWorld {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        int nb_loop=100000;
        int L=1000, C=1000;
        if (args.length > 2)
        {
            try {
                
                nb_loop = Integer.parseInt(args[0]);
                L=Integer.parseInt(args[1]);
                C=Integer.parseInt(args[2]);
            } catch (NumberFormatException e) {
                System.err.println("Parametres a fournir : nombre de boucles hauteur largeur de l'image "+ args[0]);
                System.exit(1);
            }
        }
        else System.err.println("Parametres a fournir : nombre de boucles hauteur largeur de l'image ");
        
        long start=0;
        long end=0;
        long elapsed_milliseconds=0;
        
        Image im=new Image(C,L);
        start=System.currentTimeMillis();
        
        for (int i=0;i<nb_loop;i++)
        {
            for (int l=0;l<L;l++)
            {
                for (int c=0;c<C;c++)
                {
                    byte b=im.get(l,c).b();
                    im.get(l,c).setg(b);
                    im.get(l,c).setr(b);
                    //System.out.println(b);
                }
            }
        }
        end=System.currentTimeMillis();
        elapsed_milliseconds=end-start;
        System.out.println("Bonjour, suis-je aussi performant? Java " + nb_loop + " "
                           + L + " " + C + " "
                           + elapsed_milliseconds);
    }   
}


// Image



