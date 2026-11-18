% Q26. Prolog program for fruit and its color using backtracking.
fruit(apple).
fruit(banana).
fruit(grapes).
fruit(orange).

color(apple, red).
color(banana, yellow).
color(grapes, purple).
color(orange, orange).

fruit_color(Fruit, Color) :-
    fruit(Fruit),
    color(Fruit, Color).

% Query: ?- fruit_color(Fruit, Color).
