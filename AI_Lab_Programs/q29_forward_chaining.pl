% Q29. Prolog program for forward chaining.
% Facts and rules are represented as Horn-style rules.
fact(parent(alice, bob)).
fact(parent(bob, carol)).
fact(parent(carol, david)).

% Derived relation: grandparent(X,Z) if parent(X,Y) and parent(Y,Z).
derive(grandparent(X, Z)) :-
    fact(parent(X, Y)),
    fact(parent(Y, Z)).

% A simple forward-chaining pass over the available facts.
forward_chain(Conclusion) :-
    derive(Conclusion).

% Query: ?- forward_chain(grandparent(alice, Who)).
