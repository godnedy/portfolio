package com.godnedy;

import sun.awt.image.ImageWatched;

import java.util.*;

public abstract class Player {

	/**
	 * No of row which must be reached by player's man so that it becomes a dame
	 */
	private int playersKingsrow;
	private Game game;
	/**
	 * list of pieces belonging to player
	 * piece is a linked list
	 */
	private LinkedList<Piece> pieces;


	public Player(Game game){
		this.pieces = new LinkedList<Piece>();
		this.playersKingsrow = 0;
		this.game = game;
	}
	public abstract void play();

	/**
	 * ends turn when the after the Timer event
	 */
	public void endTurnAfterTimeIsUp() {
		// TODO - implement Player.endTurnAfterTimeIsUp
		throw new UnsupportedOperationException();
	}

	/**
	 * 
	 * @param piece
	 * @param destination
	 */

}