def study_schedule(permanence_period, target_time):
    """ Faça o código aqui. """
    counter = 0
    if target_time is None:
        return None
    for std in permanence_period:
        if std[0] is None or std[1] is None:
            return None
        if std[0] <= target_time <= std[1]:
            counter += 1
    return counter
