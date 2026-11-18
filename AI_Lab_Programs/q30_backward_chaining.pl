% Q30. Prolog program for backward chaining.
parent(alice, bob).
parent(bob, carol).
parent(carol, david).

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

% Queries: ?- grandparent(alice, Who).
%          ?- ancestor(alice, Who).
