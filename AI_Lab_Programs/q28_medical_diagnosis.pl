% Q28. Prolog program for simple medical diagnosis.
symptom(fever, flu).
symptom(cough, flu).
symptom(body_pain, flu).
symptom(sneezing, common_cold).
symptom(runny_nose, common_cold).
symptom(fever, infection).
symptom(sore_throat, infection).

diagnosis(Disease, Symptoms) :-
    setof(S, symptom(S, Disease), Symptoms).

% Query: ?- diagnosis(Disease, Symptoms).
% Educational demonstration only; not a real diagnostic tool.
