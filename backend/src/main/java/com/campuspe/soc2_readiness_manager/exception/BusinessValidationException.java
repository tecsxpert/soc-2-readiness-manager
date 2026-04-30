package com.campuspe.soc2_readiness_manager.exception;

import java.util.Collections;
import java.util.List;


public class BusinessValidationException extends RuntimeException {

    private final List<String> violations;

    public BusinessValidationException(String violation) {
        super(violation);
        this.violations = Collections.singletonList(violation);
    }

    public BusinessValidationException(List<String> violations) {
        super("Validation failed: " + String.join("; ", violations));
        this.violations = Collections.unmodifiableList(violations);
    }

    public List<String> getViolations() {
        return violations;
    }
}
