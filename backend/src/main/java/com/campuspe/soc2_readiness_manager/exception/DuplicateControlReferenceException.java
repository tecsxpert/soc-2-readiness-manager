package com.campuspe.soc2_readiness_manager.exception;


public class DuplicateControlReferenceException extends RuntimeException {

    private final String controlReference;

    public DuplicateControlReferenceException(String controlReference) {
        super(String.format("A readiness item with control reference '%s' already exists", controlReference));
        this.controlReference = controlReference;
    }

    public String getControlReference() {
        return controlReference;
    }
}
