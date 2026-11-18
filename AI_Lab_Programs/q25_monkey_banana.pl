% Q25. Prolog program for Monkey and Banana problem.
% State: state(MonkeyPosition, MonkeyStatus, BoxPosition, HasBanana)
% MonkeyStatus is on_floor or on_box.

move(state(middle, on_box, middle, no),
     grasp,
     state(middle, on_box, middle, yes)).

move(state(P, on_floor, P, H),
     climb,
     state(P, on_box, P, H)).

move(state(P1, on_floor, B, H),
     push(P1, P2),
     state(P2, on_floor, P2, H)) :-
    P1 \= P2.

move(state(P1, on_floor, B, H),
     walk(P1, P2),
     state(P2, on_floor, B, H)) :-
    P1 \= P2.

solve_monkey(State, []) :-
    State = state(_, _, _, yes).
solve_monkey(State, [Action|Actions]) :-
    move(State, Action, NextState),
    solve_monkey(NextState, Actions).

% Example query:
% ?- solve_monkey(state(door, on_floor, window, no), Plan).
