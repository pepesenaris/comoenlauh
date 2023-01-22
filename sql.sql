-- employees                             projects
-- +---------------+---------+           +---------------+---------+
-- | id            | int     |<----+  +->| id            | int     |
-- | first_name    | varchar |     |  |  | title         | varchar |
-- | last_name     | varchar |     |  |  | start_date    | date    |
-- | salary        | int     |     |  |  | end_date      | date    |
-- | department_id | int     |--+  |  |  | budget        | int     |
-- +---------------+---------+  |  |  |  +---------------+---------+
--                             |  |  |
-- departments                  |  |  |  employees_projects
-- +---------------+---------+  |  |  |  +---------------+---------+
-- | id            | int     |<-+  |  +--| project_id    | int     |
-- | name          | varchar |     +-----| employee_id   | int     |
-- +---------------+---------+           +---------------+---------+

-- 1 - Sort the current employees at the company by who has the highest salary

-- select first_name, LAST_NAME, salary
-- from EMPLOYEES
-- order by salary DESC;

-- 2 - Show all of the employees that worked on the project “Build a cool site”


-- select EMPLOYEES.first_name, EMPLOYEES.last_name, PROJECTS.TITLE
-- from EMPLOYEES
-- join EMPLOYEES_PROJECTS
--   on EMPLOYEES.id = EMPLOYEES_PROJECTS.EMPLOYEE_ID
-- join PROJECTS
--   on EMPLOYEES_PROJECTS.PROJECT_ID = EMPLOYEES_PROJECTS.PROJECT_ID
-- where PROJECTS.title = 'Build a cool site';

-- 3 - For the project “Build a cool site”, if an employee was paid on the 1st and the 15th of every month, show how much each employee made for the duration of the project.

