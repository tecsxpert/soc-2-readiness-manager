package com.campuspe.soc2_readiness_manager.dto;

import com.campuspe.soc2_readiness_manager.entity.ControlCategory;
import com.campuspe.soc2_readiness_manager.entity.PriorityLevel;
import com.campuspe.soc2_readiness_manager.entity.ReadinessStatus;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;
import java.time.LocalDate;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ReadinessItemRequest {

    @NotBlank(message = "Title is required")
    @Size(max = 150, message = "Title must not exceed 150 characters")
    private String title;

    @NotBlank(message = "Control reference is required")
    @Size(max = 50, message = "Control reference must not exceed 50 characters")
    private String controlReference;

    @NotBlank(message = "Description is required")
    @Size(max = 2000, message = "Description must not exceed 2000 characters")
    private String description;

    @NotNull(message = "Category is required")
    private ControlCategory category;

    @NotNull(message = "Status is required")
    private ReadinessStatus status;

    @NotNull(message = "Priority is required")
    private PriorityLevel priority;

    @NotBlank(message = "Owner name is required")
    @Size(max = 100, message = "Owner name must not exceed 100 characters")
    private String ownerName;

    @NotBlank(message = "Owner email is required")
    @Email(message = "Owner email must be a valid email address")
    @Size(max = 150, message = "Owner email must not exceed 150 characters")
    private String ownerEmail;

    @NotNull(message = "Readiness score is required")
    @Min(value = 0, message = "Readiness score must be at least 0")
    @Max(value = 100, message = "Readiness score must not exceed 100")
    private Integer readinessScore;

    @NotNull(message = "Due date is required")
    private LocalDate dueDate;

    @Size(max = 2000, message = "Evidence details must not exceed 2000 characters")
    private String evidenceDetails;

    @Size(max = 2000, message = "Risk summary must not exceed 2000 characters")
    private String riskSummary;

    @Size(max = 4000, message = "AI summary must not exceed 4000 characters")
    private String aiSummary;
}
