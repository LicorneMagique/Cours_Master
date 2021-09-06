import java.math.BigInteger;

import static java.math.BigInteger.ONE;

public class RSA extends CryptoSystem {

    public RSA() {
        super();
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
    @Override
    public void keyGen() {
        super.keyGen();
        BigInteger e = BigInteger.valueOf(3);
        while (!e.gcd(phi).equals(ONE)) {
            e = e.add(ONE);
        }
        BigInteger d = e.modInverse(phi);
        pk[0] = n;
        pk[1] = e;
        sk[0] = n;
        sk[1] = d;
        maxBitLength = n.bitLength() - 1;
    }

    /**
     * @param pk public key
     * @param m message tel que m ∈ Zn*
     * @return c = m^e mod n.
     */
    @Override
    public BigInteger encrypt(BigInteger[] pk, BigInteger m) {
        BigInteger n = pk[0];
        BigInteger e = pk[1];
        return m.modPow(e, n);
    }

    @Override
    public BigInteger decrypt(BigInteger[] sk, BigInteger c) {
        BigInteger n = sk[0];
        BigInteger d = sk[1];
        return c.modPow(d, n);
    }

}
