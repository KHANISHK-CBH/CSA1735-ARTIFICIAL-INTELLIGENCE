% Q22. Prolog facts and queries: determine whether a bird can fly.
bird(parrot).
bird(eagle).
bird(penguin).
bird(sparrow).

can_fly(Bird) :-
    bird(Bird),
    \+ cannot_fly(Bird).

cannot_fly(penguin).

% Queries:
% ?- can_fly(parrot).
% ?- can_fly(penguin).
% ?- can_fly(Bird).
