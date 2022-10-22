

/**
 * The Gird class emulates an 8x8 grid filled with characters and allows you to modify the board thourgh the place method 
 */
public class Grid {
    
   /**
    * The board is a 8x8 grid where each value corresponds with a character in the alphabtet. □ is a blank space
   */
    private char [][] board = {{'□','□','□','□','□','□','□','□'},
                              {'□','□','□','□','□','□','□','□'},
                              {'□','□','□','□','□','□','□','□'},
                              {'□','□','□','□','□','□','□','□'},
                              {'□','□','□','□','□','□','□','□'},
                              {'□','□','□','□','□','□','□','□'},
                              {'□','□','□','□','□','□','□','□'},
                              {'□','□','□','□','□','□','□','□'}};
   /**
    * The place method allows you to insert a specific character at a specific location in the board
    * @param a The character to be placed
    * @param x The x location in the grid
    * @param y The y locatiion in the grid
    */
   public void place(char a,int x,int y){
            board[y][x] = a;
    }

   public void printBoard(){
    for(int i = 0; i < 8; ++i){
        for(int j =0; j< 8; ++ j){
            System.out.print(board[i][j] + " ");
        }
        System.out.println();
    }
    System.out.println("---------------------------------");
   }

    public boolean checkBoard(){
        boolean result = true;
        return result;
   }

}
