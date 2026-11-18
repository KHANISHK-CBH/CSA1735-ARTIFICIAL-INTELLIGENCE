% Q24. Prolog program to suggest a diet based on disease.
% Educational example only; not medical advice.
disease(diabetes).
disease(hypertension).
disease(anemia).

avoid(diabetes, sugary_food).
avoid(hypertension, high_salt_food).
avoid(anemia, tea_with_meals).

include(diabetes, high_fiber_food).
include(hypertension, fruits_and_vegetables).
include(anemia, iron_rich_food).

diet_suggestion(Disease, Avoid, Include) :-
    disease(Disease),
    avoid(Disease, Avoid),
    include(Disease, Include).

% Query: ?- diet_suggestion(diabetes, Avoid, Include).
