
package com.godnedy;

import java.util.*;

/**
 * a board where the pieces are being placed
 */
public class Board {

	Game game;
	/**
	 * On the field there could be a piece of player 1, a piece of player 2 or field can be empty
	 */
	private Piece[][] fieldsOfBoard;
	/**
	 * length of side (we assume that board is an rectangle)
	 */
	private int size = 0;

	public Board(Game game, int size){
		this.game = game;
		this.size = size;

	}

	/**
	 * checks if field of table is occupied (if so by whom) or not, returns true or false
	 * @param position
	 */

	public boolean isPositionOccupied(Position position) {
		Piece field = fieldsOfBoard[position.getColumn()][position.getRow()];
		if (field == null)
			return false;
		else
			return true;
	}

	/**
	 * 
	 * @param position
	 */
	public Piece returnPiece(Position position) {
		return fieldsOfBoard[position.getColumn()][position.getRow()];
	}
	public int getSize(){
		return this.size;
	}

	/**
	 * prints board with all pieces on it 
	 */
	public void printBoard() {
		// TODO - implement Board.printBoard
		throw new UnsupportedOperationException();
	}

	/**
	 * 
	 * @param position
	 */
	public void removePiece(Position position) {
		// TODO - implement Board.removePiece
		throw new UnsupportedOperationException();
	}

	/**
	 * 
	 * @param piece
	 */
	public void changeToDame(Piece piece) {
		Position position = piece.getPosition();
		Player owner = piece.get
	}

	private void populateWithPieces(Piece[] pieces) {
		// TODO - implement Board.populateWithPieces
		throw new UnsupportedOperationException();
	}

}