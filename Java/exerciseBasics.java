public class exerciseBasics {
    static void exer_1() {
        System.out.println("Hello World");
        System.out.println("Jake Inthavongsa");
    }

    static void exer_2() {
        System.out.println(74 + 36);
    }

    static void exer_3(int x, int y) {
        int z = x / y;
        System.out.println(Integer.toString(z));
    }

    public static void main(String[] args) {
        exer_1();
        exer_2();
        exer_3(50, 3);
    }
}
