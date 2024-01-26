import java.util.Scanner;

class basics {
    public static void main(String[] args) {
        String[] names = { "Rose", "Red", "Zero", "Lily", "Eclipse", "Candi", "Sno", "Violet" };
        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i]);
        }

        Scanner myObj = new Scanner(System.in);
        rps RockPaperScissors = new rps();

        System.out.println("Hello World!\n");
        System.out.print("Please enter your name: ");
        String userName = myObj.nextLine();
        System.out.println("Your name is: " + userName);
        System.out.println("Please enter an rock, paper, or scissors");
        String userInput = myObj.nextLine();

        while (rps.checkInput(userInput) == false) {
            System.out.println("Please enter a valid input");
            userInput = myObj.nextLine();
        }

        System.out.println("You chose" + userInput);

    }
}