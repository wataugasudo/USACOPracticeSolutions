//Solves []

import java.io.*;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        // Setup optimized input/output file objects
        BufferedReader inFile = new BufferedReader(new FileReader("FILENAME.in"));
        PrintWriter outFile = new PrintWriter(new BufferedWriter(new FileWriter("FILENAME.out")));

        // Get next line in file & break into "tokens" at spaces
        //StringTokenizer firstLine = new StringTokenizer(inFile.readLine());

        // Get next token as String
        //String firstWord = firstLine.nextToken();
        // Get next token as Integer
        //int firstInt = Integer.parseInt(firstLine.nextToken());

        // YOUR CODE HERE
        
        // Write to & close output file
        outFile.print();
        outFile.close();
    }
}
