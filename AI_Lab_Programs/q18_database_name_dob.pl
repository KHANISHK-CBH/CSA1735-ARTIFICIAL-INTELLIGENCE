% Q18. Prolog database with name and date of birth.
% Facts
person('Arun', date(12, 5, 2004)).
person('Bala', date(23, 8, 2003)).
person('Divya', date(7, 1, 2005)).

% Query: ?- person(Name, DOB).
% Query: ?- person('Arun', DOB).
