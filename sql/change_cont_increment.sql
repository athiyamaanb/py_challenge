/*
Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?


+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | James  |
+---------+---------+
For the sample input, the output is:

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | James  |
+---------+---------+
Note:

If the number of students is odd, there is no need to change the last one's seat.
*/

CREATE TABLE students(
`id` INTEGER,
  `student` TEXT
);

INSERT INTO students
  (`id`, `student`)
VALUES
('1','Abbot'),
('2','Doris'),
('3','Emerson'),
('4','Green'),
('5','James');


-- Answer
select id, student,
	case when mod(id, 2)<>0 and id<>5  then id+1
         when mod(id, 2)<>0 and id=5 then id
    else id-1 end as new_id
from students
order by new_id

