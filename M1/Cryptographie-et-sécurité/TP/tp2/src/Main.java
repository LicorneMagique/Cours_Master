public class Main {

    public static void main(String[] args) {
        CryptoSystem rsa = new RSA();
        CryptoSystem paillier = new Paillier();
        rsa.test();
        paillier.test();
    }

}
