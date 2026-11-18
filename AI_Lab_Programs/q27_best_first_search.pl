% Q27. Prolog program to implement Greedy Best First Search.
% The open list is ordered by the heuristic value of each path's first node.

edge(a, b).
edge(a, c).
edge(b, d).
edge(c, d).
edge(c, e).
edge(d, f).
edge(e, f).

heuristic(a, 6).
heuristic(b, 4).
heuristic(c, 3).
heuristic(d, 2).
heuristic(e, 5).
heuristic(f, 0).

best_first(Start, Goal, Path) :-
    heuristic(Start, H),
    best_first_loop([H-[Start]], Goal, [], RevPath),
    reverse(RevPath, Path).

best_first_loop([_- [Goal|Rest] | _], Goal, _, [Goal|Rest]).
best_first_loop([_- [Node|Rest] | Open], Goal, Visited, Path) :-
    ( member(Node, Visited) ->
        best_first_loop(Open, Goal, Visited, Path)
    ;
        findall(H-[Next,Node|Rest],
                (edge(Node, Next),
                 \+ member(Next, Visited),
                 \+ member_path(Next, [Node|Rest]),
                 heuristic(Next, H)),
                Children),
        append(Open, Children, Combined),
        keysort(Combined, Sorted),
        best_first_loop(Sorted, Goal, [Node|Visited], Path)
    ).

member_path(Node, [Node|_]).
member_path(Node, [_|Tail]) :- member_path(Node, Tail).

% Query: ?- best_first(a, f, Path).
