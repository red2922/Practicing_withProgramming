public class rps {
    static String[] moves = { "rock", "paper", "scissors" };

    static boolean checkInput(String input) {
        boolean isValid = false;
        int i = 0;
        while (isValid != true && i < moves.length) {
            if (input.equals(moves[i])) {
                isValid = true;
            }

            i++;
        }

        return isValid;
    }

    static String botWin() {
        return "bot";
    }

    static String playerWin() {
        return "player";
    }
}
