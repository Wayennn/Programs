package com.mycompany.clockproblem;

public class clockproblem {
    public static void main(String args[]) {
        int i = 0;
        int j, k;
        double[] x = new double[144];
        double[] y = new double[144];
        String zero = "";
        String zero1 = "";
        for(j=0; j<12; j++) {
            for(k=0; k<12; k++) {
                x[i] = 12.0*(12.0*j+k)/143.0;
                y[i] = 12.0*(j+12.0*k)/143.0;
                System.out.print("Hand at " + 12.0*(12.0*j+k)/143.0 + ", hand at " + 12.0*(j+12.0*k)/143.0);
                if((int)(Math.floor(5*x[i]))==60)
                    x[i] = 0;
                if((int)(Math.floor(5*y[i]))==60)
                    y[i] = 0;
                if((int)(Math.floor(5*y[i]))<10)
                    zero = "0";
                if((int)(60*(5*y[i]-(Math.floor(5*y[i]))))<10)
                    zero1 = "0";
                if((int)Math.floor(x[i])==0) {
                    System.out.print("\t Time is: " + 12 + ":" + zero + (int)(Math.floor(5*y[i])) + ":" + zero1 + (int)(60*(5*y[i]-(Math.floor(5*y[i])))));                
                } else {
                    System.out.print("\t Time is: " + (int)Math.floor(x[i]) + ":" + zero + (int)(Math.floor(5*y[i])) + ":" + zero1 + (int)(60*(5*y[i]-(Math.floor(5*y[i])))));
                }
                zero = "";
                zero1 = "";
                if((int)(Math.floor(5*x[i]))<10)
                    zero = "0";
                if((int)(60*(5*x[i]-(Math.floor(5*x[i]))))<10)
                    zero1 = "0";
                if((int)Math.floor(y[i])==0) {
                    System.out.println(" or " + 12 + ":" + zero + (int)(Math.floor(5*x[i])) + ":" + (int)(60*(5*x[i]-(Math.floor(5*x[i])))));                
                } else {
                    System.out.println(" or " + (int)Math.floor(y[i]) + ":" + zero + (int)(Math.floor(5*x[i])) + ":" + (int)(60*(5*x[i]-(Math.floor(5*x[i])))));
                }
                zero = "";
                zero1 = "";
                i++;
            }
        }
    }
}
