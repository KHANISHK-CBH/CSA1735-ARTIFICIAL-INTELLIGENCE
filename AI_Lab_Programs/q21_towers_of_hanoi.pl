% Q21. Prolog program to implement Towers of Hanoi.
hanoi(1, From, To, _) :-
    format('Move disk from ~w to ~w~n', [From, To]).
hanoi(N, From, To, Aux) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, From, Aux, To),
    hanoi(1, From, To, Aux),
    hanoi(N1, Aux, To, From).

% Query: ?- hanoi(3, left, right, middle).
