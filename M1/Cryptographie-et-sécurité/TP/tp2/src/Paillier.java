import java.math.BigInteger;

import static java.math.BigInteger.ONE;

public class Paillier extends CryptoSystem {

    private BigInteger rho;

    public Paillier() {
        super();
    }

    /**
     * KeyGen() permet de générer aléatoirement deux nombres premiers p, q de 1024 bits
     *
     * Soit n = pq et φ = (p − 1)(q − 1) et ρ = n^-1 mod φ
     * pk = n; sk = ρ
     */
    @Override
    public void keyGen() {
        super.keyGen();
        rho = n.modInverse(phi);
        pk[0] = n;
        sk[0] = n;
        sk[1] = rho;
        maxBitLength = rho.bitLength() - 1;
    }

    private BigInteger randomZStarN(BigInteger n) {
        BigInteger r;
        do {
            r = new BigInteger(bitLength, random);
        } while (r.compareTo(n) >= 0 || r.gcd(n).intValue() != 1);

        return r;
    }

    /**
     * @param pk public key
     * @param m message tel que m ∈ Zn*
     * Choisir aléatoirement r ∈ Z/Zn
     * @return c = (1 + m * n) * (r^n) mod n^2
     */
    @Override
    public BigInteger encrypt(BigInteger[] pk, BigInteger m) {
        BigInteger n = pk[0];
        BigInteger r = randomZStarN(n);
        BigInteger nsquare = n.multiply(n);
        BigInteger c = ONE.add(m.multiply(n))
                .multiply(r.modPow(n, nsquare));
        return c;
    }

    /**
     * Calcule r = c^ρ mod n.
     * @param sk secret key
     * @param c message encrypté
     * r = c^ρ mod n
     * @return m = (c * r^-n mod n^2 - 1) / n
     */
    @Override
    public BigInteger decrypt(BigInteger[] sk, BigInteger c) {
        BigInteger n = sk[0];
        BigInteger rho = sk[1];
        BigInteger r = c.modPow(rho, n);
        BigInteger nsquare = n.multiply(n);
        BigInteger m = c.multiply(r.modPow(n.negate(), nsquare))
                .mod(nsquare).subtract(ONE)
                .divide(n);
        return m;
    }

}
