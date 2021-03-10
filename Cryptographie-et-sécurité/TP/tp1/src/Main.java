import java.math.BigInteger;
import java.util.Random;

public class Main {

    // https://docs.oracle.com/en/java/javase/13/docs/api/java.base/java/math/BigInteger.html

    public static void main(String[] args) {
        // doExercice74();
        // doExercice75();
        // doExercice76();
        doExercice77();
        // doExercice78();
    }

    /**
     * 1. Générer aléatoirement 2 entiers a et b de 2048 bits. Afficher-les.
     * 2. Quelle est la taille (en nombres de bits) de a + b et a × b.
     * 3. Quels sont les temps d’exécution pour obtenir a + b, a × b, a/b et a mod b (avec
     * les méthodes sum, multiply, divide et mod).
     */
    private static void doExercice74() {
        System.out.println("Début exercice 74");

        // 1.
        Random randNum = new Random();
        Integer size = 2048;
        BigInteger a = new BigInteger(size, randNum);
        BigInteger b = new BigInteger(size, randNum);
        System.out.println("a = " + a);
        System.out.println("b = " + b);

        // 2.
        Integer taille;
        taille = a.add(b).bitLength();
        System.out.println("Taille a + b " + taille);
        taille = a.multiply(b).bitLength();
        System.out.println("Taille a * b " + taille);

        // 3.
        Integer it = 1000000;
        Integer ms = it / 1000;
        float time;
        long debut, fin;
        debut = System.currentTimeMillis();
        for (Integer i = 0; i < it; i++) {
            a.add(b);
        }
        fin = System.currentTimeMillis();
        time = fin - debut;
        time /= ms;
        System.out.println("Temps a + b : " + time + " μs");

        debut = System.currentTimeMillis();
        for (Integer i = 0; i < it; i++) {
            a.multiply(b);
        }
        fin = System.currentTimeMillis();
        time = fin - debut;
        time /= ms;
        System.out.println("Temps a * b : " + time + " μs");

        debut = System.currentTimeMillis();
        for (Integer i = 0; i < it; i++) {
            a.divide(b);
        }
        fin = System.currentTimeMillis();
        time = fin - debut;
        time /= ms;
        System.out.println("Temps a / b : " + time + " μs");

        debut = System.currentTimeMillis();
        for (Integer i = 0; i < it; i++) {
            a.mod(b);
        }
        fin = System.currentTimeMillis();
        time = fin - debut;
        time /= ms;
        System.out.println("Temps a % b : " + time + " μs");

        System.out.println("Fin exercice 74\n");
    }

    /**
     * 1. Générer aléatoirement 2 entiers a et b de 2048 bits.
     * 2. Approximer (expérimentalement) la probabilité que a soit premier.
     * 3. Approximer (expérimentalement) la probabilité que a et b soient premiers entre eux,
     *    i.e. pgcd(a, b) = 1.
     */
    private static void doExercice75() {
        System.out.println("Début exercice 75");

        // 1.
        Random randNum = new Random();
        Integer size = 2048;
        BigInteger a = new BigInteger(size, randNum);
        BigInteger b = new BigInteger(size, randNum);

        // 2.
        Integer primeFound = 0;
        long primeTest = 0;
        float proba;
        while (primeFound < 10) { // -> le test a 2^1 chances de se tromper
            if (a.isProbablePrime(1)) {
                primeFound++;
            }
            a = new BigInteger(size, randNum);
            primeTest++;
        }
        proba = (float) primeFound / (float) primeTest;
        System.out.println("Proba a premier : " + proba);

        // 3.
        primeFound = 0;
        primeTest = 0;
        while (primeFound < 1000) { // -> le test a 2^1 chances de se tromper
            if (a.gcd(b).equals(new BigInteger("1"))) {
                primeFound++;
            }
            a = new BigInteger(size, randNum);
            b = new BigInteger(size, randNum);
            primeTest++;
        }
        proba = (float) primeFound / (float) primeTest;
        System.out.println("Proba a premier avec b : " + proba);

        System.out.println("Fin exercice 75\n");
    }

    /**
     * 1. Générer aléatoirement un entier p non-premier de 2048 bits.
     * 2. Proposer et implémenter une méthode AleaInf(p) pour générer aléatoirement un
     *    entier a dans l’ensemble {1, 2, . . . , p − 1}.
     * 3. Soit a = AleaInf(p).
     *    Calculer a^(p−1) mod p de 2 manières différentes :
     *      (a) En calculant c = a^(p−1) puis c mod p
     *      (b) En utilisant la méthode modPow
     *      Quelle est la plus efficace ?
     * 4. Mesurer (expérimentalement) la probabilité que a^(p−1) mod p = 1
     *    (en échantillonnant a, p comme décrit ci-dessus).
     */
    private static void doExercice76() {
        System.out.println("Début exercice 76");

        // 1.
        Random randNum = new Random();
        Integer size = 2048;
        BigInteger p = new BigInteger(size, randNum);
        while (p.isProbablePrime(1)) {
            p = new BigInteger(size, randNum);
        }

        // 2.
        // 3.
        BigInteger a = aleaInf(p);
        BigInteger c;
        float time;
        long debut, fin;
        // a)
        /* debut = System.currentTimeMillis();
        c = a.pow(p.subtract(BigInteger.ONE).intValue()).mod(p); // -> Erreur : exposant trop grand
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps a) : " + time); */

        // b)
        debut = System.currentTimeMillis();
        c = a.modPow(p.subtract(BigInteger.ONE), p);
        fin = System.currentTimeMillis();
        time = fin - debut;
        System.out.println("Temps b) : " + time);

        // 4.
        Integer found = 0;
        long tests = 0;
        float proba;
        while (found < 10 && tests < 1000) {
            if (c.equals(BigInteger.ONE)) {
                found++;
            }
            p = new BigInteger(size, randNum);
            while (p.isProbablePrime(1)) {
                p = new BigInteger(size, randNum);
            }
            a = aleaInf(p);
            c = a.modPow(p.subtract(BigInteger.ONE), p);
            tests++;
        }
        proba = (float) found / (float) tests;
        System.out.println("Proba a premier : " + proba);

        System.out.println("Fin exercice 76\n");
    }

    /**
     * Génère aléatoirement un entier a dans l’ensemble {1, 2, . . . , p − 1}.
     * @param p
     * @return a
     */
    private static BigInteger aleaInf(BigInteger p) {
        Random randNum = new Random();
        Integer size = p.bitLength();
        BigInteger a = new BigInteger(size, randNum);
        while (a.compareTo(p) > -1) {
            a = new BigInteger(size, randNum);
        }
        return a;
    }

    /**
     * 1. Générer aléatoirement un entier premier p de 2048 bits.
     * 2. Quel est le temps (moyen) de génération de p ?
     * 3. Soit a = AleaInf(p). Vérifier (expérimentalement) que a^(p−1) mod p = 1.
     * 4. En déduire un test de primalité efficace.
     */
    private static void doExercice77() {
        System.out.println("Début exercice 77");

        // 1.
        float time;
        long debut, fin;
        Random randNum = new Random();
        Integer size = 2048;
        debut = System.currentTimeMillis();
        BigInteger p = new BigInteger(size, randNum);
        while (!p.isProbablePrime(1)) {
            p = new BigInteger(size, randNum);
        }
        fin = System.currentTimeMillis();

        // 2.
        time = fin - debut;
        System.out.println("Temps p : " + time + "ms");

        // 3.
        BigInteger a = aleaInf(p);
        Integer found = 0;
        long tests = 0;
        float proba;
        while (tests < 1000) {
            if (a.modPow(p.subtract(BigInteger.ONE), p).equals(BigInteger.ONE)) {
                found++;
            }
            p = new BigInteger(size, randNum);
            while (p.isProbablePrime(1)) {
                p = new BigInteger(size, randNum);
            }
            a = aleaInf(p);
            tests++;
        }
        proba = (float) found / (float) tests;
        System.out.println("Proba a^(p−1) mod p = 1 : " + proba);

        System.out.println("Fin exercice 77\n");
    }

    /**
     * L’inverse modulaire de a modulo n est un entier b ∈ {1, . . . , n − 1} tel
     * que a × b mod n = 1.
     * 1. Générer deux nombres premiers p et q de 1024 et les multiplier, i.e. n = pq.
     * 2. Soit a = AleaInf(p). Calculer l’inverse b de a modulo n avec la fonction
     *    modInverse.
     * 3. Vérifier que (a × b) mod n = 1.
     * 4. Quel est l’inverse de p modulo n. Justifier.
     */
    private static void doExercice78() {
        System.out.println("Début exercice 78");

        // 1.
        Random randNum = new Random();
        Integer size = 1024;
        BigInteger p = new BigInteger(size, randNum);
        while (!p.isProbablePrime(1)) {
            p = new BigInteger(size, randNum);
        }
        BigInteger q = new BigInteger(size, randNum);
        while (!q.isProbablePrime(1)) {
            q = new BigInteger(size, randNum);
        }
        BigInteger n = p.multiply(q);

        System.out.println("Fin exercice 78\n");
    }

}
