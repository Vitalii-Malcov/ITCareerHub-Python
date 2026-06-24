USE employees;
DELIMITER //

CREATE PROCEDURE get_employee_department(
    IN emp_id INT
)
BEGIN
    SELECT department_id
    FROM employees
    WHERE employee_id = emp_id;
END //

DELIMITER ;

CALL get_employee_department(100);


DELIMITER //

CREATE PROCEDURE get_employee_age(
    IN emp_id INT,
    OUT emp_age INT
)
BEGIN
    SELECT TIMESTAMPDIFF(YEAR, birth_date, CURDATE())
    INTO emp_age
    FROM employees
    WHERE employee_id = emp_id;
END //

DELIMITER ;

CALL get_employee_age(100, @age);

SELECT @age AS employee_age;

DELIMITER //

CREATE PROCEDURE decrease_salary(
    INOUT emp_salary DECIMAL(10,2)
)
BEGIN
    SET emp_salary = emp_salary * 0.9;
END //

DELIMITER ;

SET @salary = 5000;

CALL decrease_salary(@salary);

SELECT @salary AS decreased_salary;