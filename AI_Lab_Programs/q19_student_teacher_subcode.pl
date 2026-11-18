% Q19. Prolog database: student, teacher and subject code.
student(101, 'Anu', cse).
student(102, 'Bala', aids).
student(103, 'Charan', cse).

teacher(t01, 'Dr Ravi', cse).
teacher(t02, 'Dr Meena', aids).

subject(cse, 'Computer Science').
subject(aids, 'Artificial Intelligence and Data Science').

student_teacher_subject(StudentName, TeacherName, SubjectName) :-
    student(_, StudentName, Code),
    teacher(_, TeacherName, Code),
    subject(Code, SubjectName).

% Query: ?- student_teacher_subject(Student, Teacher, Subject).
