#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bestscore = 0
    bestkey = None
    for current_student, current_score in a_dictionary.items():
        if current_score > bestscore:
            bestkey = current_student
            bestscore = current_score
    return bestkey
