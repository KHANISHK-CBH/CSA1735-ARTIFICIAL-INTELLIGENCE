% Q23. Prolog program to implement a family tree.
male(ram).
male(kumar).
male(arun).
female(lakshmi).
female(meena).
female(divya).

parent(ram, kumar).
parent(lakshmi, kumar).
parent(kumar, arun).
parent(meena, arun).
parent(kumar, divya).
parent(meena, divya).

father(F, C) :- male(F), parent(F, C).
mother(M, C) :- female(M), parent(M, C).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(G, C) :- parent(G, P), parent(P, C).

% Queries: ?- father(ram, kumar).  ?- sibling(arun, divya).
