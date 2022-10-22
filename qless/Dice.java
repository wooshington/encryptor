import java.util.Random;
public class Dice {
    
    private char [][] cube = {{'M','M','L','L','B','Y'},
                              {'V','F','G','K','P','P'},
                              {'H','H','N','N','R','R'},
                              {'D','F','R','L','L','W'},
                              {'R','R','D','L','G','G'},
                              {'X','K','B','S','Z','N'},
                              {'W','H','H','T','T','P'},
                              {'C','C','B','T','J','D'},
                              {'C','C','M','T','T','S'},
                              {'O','I','I','N','N','Y'},
                              {'A','E','I','O','U','U'},
                              {'A','A','E','E','O','O'}};

    public char[] roll(){
        Random rand = new Random();
        char[] temp = {'□','□','□','□','□','□','□','□','□','□','□','□'};
        for(int i=0;i<12;++i){
            temp[i] = cube[i][rand.nextInt(6)];
        }
        return temp;
    }
}

