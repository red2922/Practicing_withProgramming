import java.util.Scanner;

class basics {
    public static void main(String[] args) {
        String[] names = { "Rose", "Red", "Zero", "Lily", "Eclipse", "Candi", "Sno", "Violet" };
        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i]);
        }

        System.out.println("Hello World!\n");
        Scanner myObj = new Scanner(System.in);
        System.out.print("Please enter your name");
        String userName = myObj.nextLine();
        System.out.println("Your name is: " + userName);
    }
}