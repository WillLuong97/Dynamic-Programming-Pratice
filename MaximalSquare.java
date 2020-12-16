import jdk.internal.agent.resources.agent;
import sun.font.TrueTypeFont;

//Java program to find the maxmial sqare 

class MaximalSquare{

    //function to solve the problem
    public int maximalSquare(char[][] matrix){
        //set up the variable: 
        int rows = matrix.length;
        int cols = rows > 0 ? matrix[0].length : 0;
        
        int resultAreaSquare = 0;
        //loop through the martix to find the element: 
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < cols; j++){
                //we will look for any matrix element that would contain the "1", if so we will see how it can form a square
                if(matrix[i][j] == "1"){
                    // local square area
                    int sqArea = 1;
                    boolean flag = true;
                    //if we encounter a 1, then will check its neighbor to see we can also form a square with 1: 
                    while(sqArea + i < rows && sqArea + j < cols && flag){
                        //FAILED CONDITIONS:
                        //loop through the neighbors of the current node and see if they make a square
                        for(int k = j; k <= sqArea + j; j++){
                            //if 0 or any value other than 1 is encoutered, then the function will stop
                            //horizaontally right 
                            if(matrix[sqArea + i][k] == '0'){
                                flag = false;
                                break;

                            }
                        }

                        for(int z = i; z < sqArea + i; z++){
                            //checking the vertically downward neighnor
                            if(matrix[z][sqArea + j] == '0'){
                                flag = false;
                                break;
                            }
                        }

                        //SUCCESS CONDITION: 
                        if(flag){
                            sqArea++;
                        }
                    }
                    if(resultAreaSquare < sqArea){
                        resultAreaSquare = sqArea;
                    }
                }
            }
        }
        return resultAreaSquare * resultAreaSquare;
    }
    //main function to run the test cases
    public static void main(String args[]){
        System.out.println("TESTING MAXMIMAL SQUARE...");
        // //Test cases: 
        // char[] array_01 = new char[]{'1','0','1','0','0'};
        // char[] array_02 = new char[]{'1','0','1','1','1'};
        // char[] array_03 = new char[]{'1','1','1','1','1'};
        // char[] array_04 = new char[]{'1','0','0','1','0'};
        // //test case number 1:
        // char[][] matrix_01 = new char[][]{array_01, array_02, array_03, array_04};

        // System.out.println(matrix_01);

        System.out.println("END OF TESTING...");
    }

}