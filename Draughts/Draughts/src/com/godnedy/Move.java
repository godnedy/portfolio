package com.godnedy;

public class Move {

	Piece can_be_made;
	Patch belongs_to;
	private Position from;
	private Position to;

	public Move(Position from, Position to){
		this.from = from;
		this.to = to;
	}
	/**
	 * Possible returned values are:
	 * "NE"
	 * "NW"
	 * "SE"
	 * "SW"
	 */
	public String getDirection() {
		// TODO - implement Move.getDirection
		throw new UnsupportedOperationException();
	}

}