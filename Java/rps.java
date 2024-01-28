import java.util.concurrent.ThreadLocalRandom;

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

    public String checkMoves(String player, String bot) {
        switch (player) {
            case "rock":
                if (bot.equals("rock")) {
                    return "draw";
                } else if (bot.equals("paper")) {
                    return botWin();
                } else {
                    return playerWin();
                }
            case "paper":
                if (bot.equals("paper")) {
                    return "draw";
                } else if (bot.equals("rock")) {
                    return botWin();
                } else {
                    return playerWin();
                }
            case "scissors":
                if (bot.equals("scissors")) {
                    return "draw";
                } else if (bot.equals("rock")) {
                    return botWin();
                } else {
                    return playerWin();
                }
            default:
                return "Your inputs are wrong";
        }
    }

    public String randomChoice() {
        int randomChoice = ThreadLocalRandom.current().nextInt(0, 3);
        return moves[randomChoice];
    }

    static String botWin() {
        return "bot";
    }

    static String playerWin() {
        return "player";
    }

}
