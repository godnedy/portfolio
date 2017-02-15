package com.company;

/*
 * Created by Edyta on 28.01.2017.
 */

import java.io.FileReader;
import java.util.Scanner;

public class Game {
    private int numberOfQuestions;
    private int questionCounter;
    private int correctAnswersCounter;


    public Game(int numberOfQuestions){//constructor
        this.numberOfQuestions = numberOfQuestions;
        this.questionCounter=0;

    }

    public void play(Scanner listOfQuestions ){
        // Asks all questions of the game and displays information about the score of single game

        while(this.questionCounter < this.numberOfQuestions){

            this.answerQuestion(listOfQuestions.nextLine (),listOfQuestions.nextLine());
    }

        System.out.println("End of questions in this game.\n Number of questions asked: %i\nNumber of questions answered correctly: %i\n Your" +
                "score:" + System.out.format("%.2f%n",this.correctAnswersCounter/this.questionCounter));
    }


    private void answerQuestion(String question, String correctAnswer){
        // Asks single question
        System.out.println(question);
        System.out.println("Select answer");
        String userAnswer = Quiz.userInput.nextLine();

        if(userAnswer.equalsIgnoreCase(correctAnswer)){
            this.correctAnswersCounter++;
            System.out.println("Correct answer");
        }
        else{
            System.out.println("Incorrect answer");
        }
        this.questionCounter++;
    }
}



