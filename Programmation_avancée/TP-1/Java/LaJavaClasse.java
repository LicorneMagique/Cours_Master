public class LaJavaClasse {

    public LaJavaClasse() {
        i = 1;
        System.out.println("LaJavaClasse() "+ i + " (constructeur par defaut) ");
    }
    // Methode finalize appelee par le ramasse-miette quand une instance n’est plus utilisee
    public void finalize() {}// facultatif
    // Attributs
    private int i; // pas d’entiers non signes en Java
}
