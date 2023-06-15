#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    bestscore = 0
    for current_score in a_dictionary.values():
        if current_score > bestscore:
            bestscore = current_score
    return bestscore
