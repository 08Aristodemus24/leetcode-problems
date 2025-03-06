# This repository will contain all of my solved leetcode problems ranging from arrays, dynamic programming, backtracking, stacks, queues, trees, graphs, strings, greedy algorithms

# Articles, Videos, Papers:
* shortest path in a binary maze (close to interview questions): https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
* dijkstras algorithm: https://www.geeksforgeeks.org/print-all-shortest-paths-between-given-source-and-destination-in-an-undirected-graph/
* search the maze usiing depth first search: https://www.youtube.com/watch?v=W9F8fDQj7Ok&list=PLCBT00GZN_SAzwTS-SuLRM547_4MUHPuM&index=2&pp=gAQBiAQB
* find shortest path in grid using breadth first search (close to interview questions): https://www.youtube.com/watch?v=KiCBXu4P-2Y&list=PLCBT00GZN_SAzwTS-SuLRM547_4MUHPuM&index=3&pp=gAQBiAQB

# Data Structures & algorithms


# SQL
## Exchange Seats
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The result format is in the following example.

Input: 
Seat table:
```
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
```
Output: 
```
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
```
Explanation: 
Note that if the number of students is odd, there is no need to change the last one's seat.

```
WITH base AS (SELECT * FROM "Seat")
SELECT * FROM BASE; 
```

now I know I can't just use `with` without using the alias I assigned to the table in a select 
statement, because if I `WITH base AS (SELECT * FROM "Seat");` then it gives a 
`ERROR:  syntax error at or near ";" LINE 1: WITH base AS (SELECT * FROM "Seat");` error

MySql Solution:
```
select if(id < (select max(id) from Seat), if(id % 2 = 0, id - 1, id + 1), if(id % 2 = 0, id - 1, id)) as id, student
from Seat
order by id;
```

## Reformat Department table
In SQL,(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
 

Reformat the table such that there is a department id column and a revenue column for each month.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Department table:
```
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
```
Output: 
```
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+
```
Explanation: The revenue from Apr to Dec is null.
Note that the result table has 13 columns (1 for the department id + 12 for the months). 

MySQL and PGSql Solution:
```
-- Write your PostgreSQL query statement below
select id, 
	sum(case when month = 'Jan' then revenue else null end) as Jan_Revenue,
	sum(case when month = 'Feb' then revenue else null end) as Feb_Revenue,
	sum(case when month = 'Mar' then revenue else null end) as Mar_Revenue,
	sum(case when month = 'Apr' then revenue else null end) as Apr_Revenue,
	sum(case when month = 'May' then revenue else null end) as May_Revenue,
	sum(case when month = 'Jun' then revenue else null end) as Jun_Revenue,
	sum(case when month = 'Jul' then revenue else null end) as Jul_Revenue,
	sum(case when month = 'Aug' then revenue else null end) as Aug_Revenue,
	sum(case when month = 'Sep' then revenue else null end) as Sep_Revenue,
	sum(case when month = 'Oct' then revenue else null end) as Oct_Revenue,
	sum(case when month = 'Nov' then revenue else null end) as Nov_Revenue,
	sum(case when month = 'Dec' then revenue else null end) as Dec_Revenue
from department
group by id
order by id;
```

now I know
```
CASE
      WHEN condition_1 (that uses a column) THEN result_1 (that uses a column or just a single value)
      WHEN condition_2 (that uses a column) THEN result_2 (that uses a column or just a single value)
      [WHEN ...]
      [ELSE else_result]
END
```

is the same as a ternary like operator in mysql called the `IF()` function where 
`if(<the condition i.e. id < (select max(id) from Seat)>, <this value is returned if statement is true>, <this value is returned if statement is false>)`
instead in postgresql  its

The explanation of the solution is that we group the Department table according to the id column obviously when we 
group them by default the first occurence or row of the id column will be kept and automatically discarde