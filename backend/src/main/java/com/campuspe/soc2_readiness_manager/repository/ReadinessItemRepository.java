package com.campuspe.soc2_readiness_manager.repository;

import com.campuspe.soc2_readiness_manager.entity.ReadinessItem;
import java.util.List;
import java.util.Optional;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ReadinessItemRepository extends JpaRepository<ReadinessItem, Long> {

    Optional<ReadinessItem> findByIdAndDeletedFalse(Long id);

    List<ReadinessItem> findAllByDeletedFalse();

    Optional<ReadinessItem> findByControlReferenceAndDeletedFalse(String controlReference);
}
