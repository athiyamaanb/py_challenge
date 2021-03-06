/*
Suppose you're given the following table showing the weights of various unique animals in a zoo:
Table: animal_weights
animal_ID	weight_lbs	zoo_ID
9992	1040	12
99929	1090	12
12993	2190	11
9821	750	11
96673	580	11
1411	690	12
1415	695	9
1410	690	9
1117	1000	9
1677	800	9
13457	600	9
389745	200	9
324589	950	9
7854320	1200	9
87345	1700	9
83248582	765	9

Using this table, write a SQL query to split the data into quartiles based animal weight (where 1 is the heaviest, 4 is the lightest). Then, within each quartile, rank the animal weights from heaviest to lightest in descending order.
Your output should be structured like this:
animal_id	weight_lbs	quartile	rank_in_quartile
X	X	1	1
X	X	1	2
X	X	1	3
X	X	1	4
X	X	2	1
X	X	2	2
etc	etc	etc	etc
*/
CREATE TABLE animal_weights (
  `animal_ID` INTEGER,
  `weight_lbs` INTEGER,
  `zoo_ID` INTEGER
);

INSERT INTO animal_weights
  (`animal_ID`, `weight_lbs`, `zoo_ID`)
VALUES
  ('09992', '1040', '012'),
  ('099929', '1090', '012'),
  ('012993', '2190', '011'),
  ('009821', '750', '011'),
  ('096673', '580', '011'),
  ('01411', '690', '012'),
  ('01415', '695', '009'),
  ('01410', '690', '009'),
  ('01117', '1000', '009'),
  ('01677', '800', '009'),
  ('13457', '600', '009'),
  ('389745', '200', '009'),
  ('324589', '950', '009'),
  ('7854320', '1200', '009'),
  ('87345', '1700', '009'),
  ('83248582', '765', '009');



-- Answer
select
    animal_id,
    weight_lbs,
    tile,
    dense_rank() over(partition by tile order by weight_lbs) rk
from (
    select
        animal_id,
        weight_lbs,
        ntile(4) over(order by animal_id) as tile
    from animal_weights) t;