package com.godnedy;

import java.util.ArrayList;
import java.util.Collection;

/**
 * crowned piece
 */
public class Dame extends Piece {


	int range; //TODO- bez sensu, ze mam ta zmienna we wszystkich klasach dziedziczacych po piece, a zeby nie robic jej publicznej musze to tutaj ustawic
	private MoveDirection[] moveDirections; //TODO- bez sensu, ze mam ta zmienna we wszystkich klasach dziedziczacych po piece, a zeby nie robic jej publicznej musze to tutaj ustawic

	public Dame(Player player, Board board){
		super(player, board);
		this.range = board.getSize();
		this.moveDirections = new MoveDirection[]{MoveDirection.NE, MoveDirection.NW, MoveDirection.SE, MoveDirection.SW};
	}

	public int getRange(){
		return this.range;
	}

	public MoveDirection[] getMoveDirections() {
		return this.getMoveDirections();
	}

	public ArrayList<Move> returnPossibleMoves() {
		Position piecePosition = this.getPosition();
		ArrayList<Move> possibleMoves = new ArrayList<Move>();
		Boolean captureMoveExists = false;
		for (MoveDirection direction:this.moveDirections) {
			int i = 0;
			while(i < this.range){
				if(checkIfEmptyFromDirection(direction))
					if(!captureMoveExists)
						possibleMoves.add(new Move(new Position(this.getPosition().getRow(), this.getPosition().getColumn(),
								this.getPosition().adjacentPositionOnDirection(direction)));

			}
		}
		// TODO - implement Dame.returnListOfPossibleMoves
		throw new UnsupportedOperationException();
	}


	private boolean checkIfEmptyFromDirection(MoveDirection direction){

	}

	private boolean returnPieceFromDirection(MoveDirection direction){

	}


}