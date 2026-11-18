% Q32. Prolog program to implement pattern matching.
% A pattern matches a term when the structures unify.

match_pattern(pattern(Name, Age), person(Name, Age)) :-
    atom(Name),
    integer(Age).

% More general recursive matching example:
matches(X, X).

% Queries:
% ?- match_pattern(pattern(alice, 20), person(alice, 20)).
% ?- matches(node(a, node(b, nil)), node(a, node(b, nil))).
