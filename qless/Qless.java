import java.util.Scanner;
import java.util.Arrays;

public class Qless {
    public static void main(String[] args) {
        
        Scanner userInput = new Scanner(System.in);

        Grid board = new Grid();
        board.printBoard();
        Dice d = new Dice();
        
        char [] currentRoll = d.roll();

        System.out.println("Your Roll: " + Arrays.toString(currentRoll));


        userInput.close();
    }
}