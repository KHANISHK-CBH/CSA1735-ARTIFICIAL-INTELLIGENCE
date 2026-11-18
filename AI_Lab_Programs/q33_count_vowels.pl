% Q33. Prolog program to find the number of vowels in a word/atom.
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).

count_vowels([], 0).
count_vowels([H|T], Count) :-
    ( vowel(H) -> count_vowels(T, Rest), Count is Rest + 1
    ; count_vowels(T, Count)
    ).

vowel_count(Atom, Count) :-
    atom_chars(Atom, Characters),
    count_vowels(Characters, Count).

% Query: ?- vowel_count('artificialintelligence', N).
