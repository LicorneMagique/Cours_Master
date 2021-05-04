import java.math.BigInteger;
import java.util.Random;

import static java.math.BigInteger.ONE;

public abstract class CryptoSystem {

    protected static Integer bitLength = 1024;
    protected static Integer certainty = 10;
    protected static Random random = new Random();

    protected BigInteger[] pk;
    protected BigInteger[] sk;
    protected BigInteger p;
    protected BigInteger q;
    protected BigInteger n;
    protected BigInteger phi;
    protected Integer maxBitLength;

    abstract public BigInteger encrypt(BigInteger[] pk, BigInteger m);
    abstract public BigInteger decrypt(BigInteger[] sk, BigInteger c);

    public CryptoSystem() {
        pk = new BigInteger[2];
        sk = new BigInteger[2];
    }

    public Integer getMaxBitLength() {
        return maxBitLength;
    }


    public void keyGen() {
        p = new BigInteger(bitLength, certainty, random);
        q = new BigInteger(bitLength, certainty, random);
        n = p.multiply(q);
        phi = (p.subtract(ONE)).multiply(q.subtract(ONE));
    }

    public String getName() {
        return this.getClass().getName();
    }

    public BigInteger[] getPk() {
        return pk;
    }

    public BigInteger[] getSk() {
        return sk;
    }

    public void test() {
        keyGen();
        float time;
        long debut, fin;

        BigInteger m = new BigInteger(getMaxBitLength(), new Random());
        debut = System.currentTimeMillis();
        BigInteger c = encrypt(getPk(), m);
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps encryption m : " + time + " ms");
        debut = System.currentTimeMillis();
        BigInteger m2 = decrypt(getSk(), c);
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps décryption m : " + time + " ms");
        Boolean ok = m.equals(m2);
        String message = String.format("%s %s",
                getName(), ok ? "fonctionne" : "ne fonctionne pas"
        );
        System.out.println(message);
    }

}
