package com.godnedy;

import java.util.*;

public abstract class Piece {

	Board board;

	/**
	 * position on a board
	 */
	private Position position;
	/**
	 * FINAL
	 * to whom this piece belongs
	 */
	private Player owner;
	/**
	 * max range of piece (will change if piece becomes Dame)
	 */

	/**
	 * is it captured (still on the board) or not yet captured
	 */
	private boolean isCaptured;
	private MoveDirection[] moveDirections;
	private MoveDirection[] captureDirections;



	public Piece(Player player, Board board){
		this.owner = player;
		this.isCaptured = false;
		this.board = board;
		this.captureDirections = new MoveDirection[]{MoveDirection.NE, MoveDirection.NW, MoveDirection.SE, MoveDirection.SW};
	}

	public Position getPosition(){
		return this.position;
	}

	public Player getOwner(){
		return this.owner;
	}

	public MoveDirection[] getCaptureDirections(){
	    return this.captureDirections;
    }

	/**
	 * 
	 * @param position
	 */

	private void changePosition(Position position) {
		this.position = position;
	}

	public void changeToCaptured() {
		this.isCaptured = true;
	}

	/**
	 * returns collection of possible piece's moves from current position
	 */

	public abstract ArrayList<Move> returnPossibleMoves();
	public abstract int getRange();                             //TODO - bez sensu
	public abstract MoveDirection[] getMoveDirections();        //TODO - bez sensu
}