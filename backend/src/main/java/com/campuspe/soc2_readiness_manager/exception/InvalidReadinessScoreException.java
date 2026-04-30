package com.campuspe.soc2_readiness_manager.exception;


public class InvalidReadinessScoreException extends RuntimeException {

    private final int score;

    public InvalidReadinessScoreException(int score) {
        super(String.format("Readiness score must be between 0 and 100, got: %d", score));
        this.score = score;
    }

    public int getScore() {
        return score;
    }
}
