/* 1. Расчёт площади круга
Создайте функцию для расчета площади круга, если известен его радиус.
Используйте формулу
Где:
S — площадь шара,
r — радиус шара,
π ≈ 3.14159 */
DELIMITER $$

CREATE FUNCTION circle_area(radius DECIMAL(10,2))
RETURNS DECIMAL(20,6)
DETERMINISTIC
BEGIN
    RETURN 3.14159 * radius * radius;
END $$

DELIMITER ;

SELECT circle_area(1); -- 3.141590


/* 2. Расчёт гипотенузы треугольника
Создайте функцию для расчета гипотенузы треугольника, если известны длины его катетов.
Используйте формулу c = SQRT(a * a + b * b)
Где:
c — длина гипотенузы треугольника,
a, b — длины его катетов */
DELIMITER $$

CREATE FUNCTION hypotenuse(
    a DECIMAL(10,2),
    b DECIMAL(10,2)
)
RETURNS DECIMAL(20,6)
DETERMINISTIC
BEGIN
    RETURN SQRT(a * a + b * b);
END $$

DELIMITER ;

SELECT hypotenuse(3, 4);  -- 5