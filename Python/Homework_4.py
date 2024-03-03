# Implement the Gale-Shaply proposal algorithm (pg 131 from text.) and use your program to complete problem 3.2.4 from the book (pg 134).
# 3.2.4 Determine the stable matching resulting from the Proposal Algo run with men proposing and with women proposing given the list below
import copy

men = {"u": ["a", "b", "d", "c", "f", "e"], "v": ["a", "b", "c", "f", "e", "d"],
       "w": ["c", "b", "d", "a", "f", "e"], "x": ["c", "a", "d", "b", "e", "f"],
       "y": ["c", "d", "a", "b", "f", "e"], "z": ["d", "e", "f", "c", "b", "a"]}

women = {"a": ["z", "x", "y", "u", "v", "w"], "b": ["y", "z", "w", "x", "v", "u"],
         "c": ["v", "x", "w", "y", "u", "z"], "d": ["w", "y", "u", "x", "z", "u"],
         "e": ["u", "v", "x", "w", "y", "z"], "f": ["u", "w", "x", "v", "z", "y"]}

# Question 1
# Lets return a list of sets to show the pairs
def gale_shap(re, propose):
    matches = []
    initial = len(propose)

    c1 = copy.deepcopy(re)
    c2 = copy.deepcopy(propose)

    # Proposer will approach their reciever index[0]. If proposer == receiver[0] (highest) append to matches and remove key from all others.
    # else go to next proposer.

    while len(matches) != initial:

        for p in c2:
            if p == c1[c2[p][0]][0]:
                matches.append((p, c2[p][0]))
                removed = c2[p][0]
                for r in c1:
                    if p in c1[r]:
                        c1[r].remove(p)

                for i in c2:
                    if removed in c2[i]:
                        c2[i].remove(removed)
            else:
                c2[p].pop(0)

    return sorted(matches)

# Question 2
print(gale_shap(men, women))
print(gale_shap(women, men))
