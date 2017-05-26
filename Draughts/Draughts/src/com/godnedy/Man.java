package com.godnedy;

import java.util.ArrayList;

/**
 * usual piece, non-crowned
 */
public class Man extends Piece {

	int range; //TODO- bez sensu, ze mam ta zmienna we wszystkich klasach dziedziczacych po piece, a zeby nie robic jej publicznej musze to tutaj ustawic
	MoveDirection[] moveDirections;//TODO- bez sensu, ze mam ta zmienna we wszystkich klasach dziedziczacych po piece, a zeby nie robic jej publicznej musze to tutaj ustawic
	public Man(Player player, Board board){
		super(player, board);
		this.range = 1;
		this.moveDirections = new MoveDirection[]{MoveDirection.NE, MoveDirection.NW};
	}

	public Dame changeToDame() {
		// TODO - implement Man.changeToDame
		throw new UnsupportedOperationException();
	}

	public ArrayList<Move> returnPossibleMoves() {
		// TODO - implement Man.returnListOfPossibleMoves
		throw new UnsupportedOperationException();
	}

}