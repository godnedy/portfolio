package com.godnedy;

import java.util.*;

public class Path {

	private int capuredPieces;
	private int length;
	private LinkedList<Move> moves;


	public Path(){
		this.capuredPieces = 0;
		this.length = 0;
		this.moves = new LinkedList<Move>();
	}
	/**
	 * get List of moves
	 */
	public LinkedList<Move> getMoves() {
		return moves;
	}

	/**
	 * Adds move to the list of moves and increases length and optionally no of captured pieces
	 */
	public void addMove(Move move) {
		this.moves.add(move);
		//TODO-pomyslec nad konstrukcja ruchow, czy moga byc dluzsze? raczej tak
	}

}