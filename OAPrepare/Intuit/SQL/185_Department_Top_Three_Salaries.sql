-- "WITH" 就像是定义一个临时变量（一个临时表）
WITH RankedEmployees AS (
    -- 这是第 1 步：给所有人打排名
    SELECT 
        e.name AS Employee,
        e.salary AS Salary,
        d.name AS Department,
        DENSE_RANK() OVER (
            PARTITION BY e.departmentId
            ORDER BY e.salary DESC
        ) AS salary_rank
    FROM 
        Employee e
    JOIN 
        Department d ON e.departmentId = d.id
)
-- 这是第 2 步：从上面的临时表里筛选
SELECT 
    Department,
    Employee,
    Salary
FROM 
    RankedEmployees
WHERE 
    salary_rank <= 3;