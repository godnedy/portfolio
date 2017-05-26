package com.godnedy;

public class Position {


	private int row;
	private int column;


	public Position(int row, int column){
		this.row = row;
		this.column = column;
	}

	public int getRow() {
		return this.row;
	}

	public int getColumn() {
		return this.row;
	}

	public Position adjacentPositionOnDirection(MoveDirection direction) {
		if (direction == MoveDirection.NE)
			return new Position(this.row + 1, this.column + 1);
		else if (direction == MoveDirection.NW)
			return new Position(this.row + 1, this.column - 1);
		else if (direction == MoveDirection.SE)
			return new Position(this.row - 1, this.column + 1);
		else
			return new Position(this.row - 1, this.column - 1);
	}
}