USE company;
CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    department VARCHAR(30),
    salary DECIMAL(10,2),
    joining_date DATE
);
INSERT INTO employee
VALUES
(101, 'Kamal', 'IT', 50000.00, '2025-01-15'),
(102, 'John', 'HR', 45000.00, '2025-02-10'),
(103, 'Mary', 'Finance', 60000.00, '2025-03-20');