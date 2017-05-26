package com.godnedy;

import java.util.*;

public class Game {

	private Board board;

	private int score;
	private int noOfMovesSinceLastCapturing = 0;
	/**
	 * How much time does the player have to make a move (in seconds)
	 */
	private int timeForRound;
	/**
	 * whose turn is now
	 */
	private Player nextPlayer;
	private Player[] players;

	public Game(int size, int level, int timeForRound){
		this.players = initializePlayers(level);
		this.board = initializeBoard(size);
		this.noOfMovesSinceLastCapturing = 0;
		this.timeForRound = timeForRound;
		this.nextPlayer = randomlyChooseStartingPlayer();
	}


	/**
	 *
	 * @param size
	 */
	private Board initializeBoard(int size) {
		// TODO - implement Game.initializeBoard
		throw new UnsupportedOperationException();
	}

	/**
	 *
	 * @param levelOfComputerPlayer
	 */
	private Player[] initializePlayers(int levelOfComputerPlayer) {
		// TODO - implement Game.initializePlayers
		throw new UnsupportedOperationException();
	}

	private Player randomlyChooseStartingPlayer(){
		Random random = new Random();
		return players[random.nextInt(2)];
	}

	public void increaseNoOfMovesSinceLastCapturing(){
		this.noOfMovesSinceLastCapturing ++;
	}

	public void resetNoOfMovesSinceLastCapturing(){
		this.noOfMovesSinceLastCapturing ++;
	}

	/**
	 * Yet not sure what it returns
	 */
	public Score getScore() {
		// TODO - implement Game.getScore
		throw new UnsupportedOperationException();
	}
}