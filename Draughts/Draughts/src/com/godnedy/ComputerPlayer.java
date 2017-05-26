package com.godnedy;

import java.util.Comparator;

public abstract class ComputerPlayer extends Player {



	public ComputerPlayer(Game game){
		super(game);
	}

	public abstract Path chooseBestPatch();

	public void play() {
		// TODO - implement ComputerPlayer.play
		throw new UnsupportedOperationException();
	}

	public void endTurn() {
		// TODO - implement ComputerPlayer.endTurn
		throw new UnsupportedOperationException();
	}

}