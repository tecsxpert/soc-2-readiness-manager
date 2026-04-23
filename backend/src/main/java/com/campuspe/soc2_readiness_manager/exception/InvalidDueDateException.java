package com.campuspe.soc2_readiness_manager.exception;

import java.time.LocalDate;


public class InvalidDueDateException extends RuntimeException {

    private final LocalDate dueDate;

    public InvalidDueDateException(LocalDate dueDate) {
        super(String.format("Due date cannot be in the past: %s", dueDate));
        this.dueDate = dueDate;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }
}
