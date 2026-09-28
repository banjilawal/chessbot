# --- START_ATTACKER_VALIDATION_PROCESS ---#

if attacker_validation.is_failure:
    # Send the exception chain on failure.
    return ValidationResult.failure(
        CommonAttackPropertyTableGeneratorException(
            cls_mthd=method,
            cls_name=self.__class__.__name__,
            msg=CommonAttackPropertyTableGeneratorException.MSG,
            err_code=CommonAttackPropertyTableGeneratorException.ERR_CODE,
            ex=attacker_validation.exception,
        )
    )