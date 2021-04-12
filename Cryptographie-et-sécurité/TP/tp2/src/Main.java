import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {

    // https://docs.oracle.com/en/java/javase/13/docs/api/java.base/java/math/BigInteger.html

    public static void main(String[] args) {
        // rsa();
        paillier();
    }

    private static void paillier() {

        /*List<BigInteger> test = new ArrayList<>();
        while (test.size() < 4) {
            BigInteger e = rsaKeyGen()[0][1];
            if (!test.contains(e)) {
                test.add(e);
            }
        }*/

        BigInteger[] keys =  paillierKeyGen();
        BigInteger pk = keys[0];
        BigInteger sk = keys[1];
        float time;
        long debut, fin;
        Random randNum = new Random();


        // BigInteger m = new BigInteger(1048576*8, randNum); // m fait 1 Mo
        BigInteger m = new BigInteger(2048, randNum);
        debut = System.currentTimeMillis();
        BigInteger c = paillierEncrypt(pk, m);
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps encryption m : " + time + " ms");
        debut = System.currentTimeMillis();
        BigInteger m2 = paillierDecrypt(sk, pk, c);
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps décryption m : " + time + " ms");
        Boolean ok = m.equals(m2);
    }

    /**
     * KeyGen() permet de générer aléatoirement deux nombres premiers p, q de 1024 bits
     *
     * Soit n = pq et φ = (p − 1)(q − 1) et ρ = n^-1 mod φ
     * pk = n; sk = ρ
     */
    private static BigInteger[] paillierKeyGen() {
        BigInteger[] keys = new BigInteger[2]; // keys = { pk, sk }

        Random randNum = new Random();
        Integer k = 1024;
        BigInteger p = new BigInteger(k, randNum);
        while (!p.isProbablePrime(1)) {
            p = new BigInteger(k, randNum);
        }

        BigInteger q = new BigInteger(k, randNum);
        while (!q.isProbablePrime(1)) {
            q = new BigInteger(k, randNum);
        }

        BigInteger n = p.multiply(q);
        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));
        BigInteger rho = n.modPow(BigInteger.valueOf(-1), phi);

        keys[0] = n; // pk
        keys[1] = rho; // sk

        return keys;
    }

    /**
     * @param n public key
     * @param m message tel que m ∈ Zn*
     * Choisir aléatoirement r ∈ Z/Zn
     * @return c = (1 + m*n)*(r^n) mod n^2
     */
    private static BigInteger paillierEncrypt(BigInteger n, BigInteger m) {
        Random randNum = new Random();
        Integer k = 1024;
        BigInteger r = new BigInteger(k, randNum);
        return BigInteger.ONE.add(m.multiply(n))
                .multiply(r.modPow(n, n))
                .mod(n.pow(2));
    }

    /**
     * Calcule r = c^ρ mod n.
     * @param rho secret key
     * @param n public key
     * @param c message encrypté
     * r = c^ρ mod n
     * @return m = ((((c*(r^-n)) mod (n^2)) -1) / n
     */
    private static BigInteger paillierDecrypt(BigInteger rho, BigInteger n, BigInteger c) {
        BigInteger r = c.modPow(rho, n);
        return c.multiply((
                r.modPow(n, n).negate()// r^-n
        )).mod(
                n.pow(2)// n^2 // aie aie aie
        ).subtract(BigInteger.ONE).divide(n);
    }

    private static void rsa() {

        List<BigInteger> test = new ArrayList<>();
        while (test.size() < 4) {
            BigInteger e = rsaKeyGen()[0][1];
            if (!test.contains(e)) {
                test.add(e);
            }
        }

        BigInteger[][] keys =  rsaKeyGen();
        BigInteger[] pk = keys[0];
        BigInteger[] sk = keys[1];
        float time;
        long debut, fin;
        Random randNum = new Random();


        BigInteger m = new BigInteger(1048576*8, randNum); // m fait 1 Mo
        debut = System.currentTimeMillis();
        BigInteger c = rsaEncrypt(pk, m);
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps encryption m : " + time + " ms");
        debut = System.currentTimeMillis();
        BigInteger m2 = rsaDecrypt(sk, c);
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps décryption m : " + time + " ms");
        Boolean ok = m.equals(m2);
    }

    /**
     * KeyGen() permet de générer aléatoirement deux nombres premiers p, q de 1024 bits
     *
     * Soit n = pq et φ = (p − 1)(q − 1).
     * Choisir e arbitrairement tel que pgcd(e, φ) = 1
     * et soit d l’inverse de e dans Z φ.
     *
     * e sera choisi comme étant le plus petit entier premier avec φ(n) strictement supérieur à 1
     */
    private static BigInteger[][] rsaKeyGen() {
        BigInteger[][] keys = new BigInteger[2][];
        BigInteger[] pk = new BigInteger[2];
        BigInteger[] sk = new BigInteger[2];
        keys[0] = pk;
        keys[1] = sk;

        Random randNum = new Random();
        Integer k = 1024;
        BigInteger p = new BigInteger(k, randNum);
        while (!p.isProbablePrime(1)) {
            p = new BigInteger(k, randNum);
        }

        BigInteger q = new BigInteger(k, randNum);
        while (!q.isProbablePrime(1)) {
            q = new BigInteger(k, randNum);
        }

        BigInteger n = p.multiply(q);
        BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));

        BigInteger e = BigInteger.valueOf(3);
        while (!e.gcd(phi).equals(BigInteger.ONE)) {
            e = e.add(BigInteger.ONE);
        }

        BigInteger d = e.modInverse(phi);

        pk[0] = n;
        pk[1] = e;
        sk[0] = n;
        sk[1] = d;

        return keys;
    }

    /**
     * @param pk public key
     * @param m message tel que m ∈ Zn*
     * @return c = m^e mod n.
     */
    private static BigInteger rsaEncrypt(BigInteger[] pk, BigInteger m) {
        BigInteger n = pk[0];
        BigInteger e = pk[1];
        return m.modPow(e, n);
    }

    private static BigInteger rsaDecrypt(BigInteger[] sk, BigInteger c) {
        BigInteger n = sk[0];
        BigInteger d = sk[1];
        return c.modPow(d, n);
    }

}
