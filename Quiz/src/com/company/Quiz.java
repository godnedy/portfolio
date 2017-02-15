package com.company;
import java.io.*;
import java.util.*;

public class Quiz {
    /* An easy quiz type game to illustrate usage of switch command, working on text files and exceptions handling*/
    //static int category;
    //static int numberOfAnsweredQuestions;
    //static int numberOfCorrectAnswers;
    static FileReader listOfQuestionsFile;  // FileReader Object used to read from file
    static Scanner listOfQuestions;
    static Scanner userInput;


    public static void main (String[] args){

        System.out.println("How many questions do you want to be asked? 3, 4, 5 ?");
        userInput = new Scanner(System.in);
        try{
            Game game = new Game(userInput.nextInt());
        }
        catch(Exception e){
            e.printStackTrace();
        }
        System.out.println("Select difficulty level. \n 1 - Easy 2 - Medium 3 - Hard");
        try{
            int level = userInput.nextInt();
            switch(level){
                case 1:
                    listOfQuestionsFile = new FileReader("easy.txt");
                case 2:
                    listOfQuestionsFile = new FileReader("medium.txt");
                case 3:
                    listOfQuestionsFile = new FileReader("hard.txt");
            }
        }
        catch(Exception e){
            e.printStackTrace();
        }

        listOfQuestions = new Scanner(listOfQuestionsFile);
    }
   }




