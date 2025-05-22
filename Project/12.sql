--
-- Файл сгенерирован с помощью SQLiteStudio v3.4.17 в Чт май 22 11:10:45 2025
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: Categories
CREATE TABLE IF NOT EXISTS Categories (
    category_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
INSERT INTO Categories (category_ID, name) VALUES (1, '"Молочные продукты"');
INSERT INTO Categories (category_ID, name) VALUES (2, '"Мясо и птица"');
INSERT INTO Categories (category_ID, name) VALUES (3, '"Рыба и морепродукты"');
INSERT INTO Categories (category_ID, name) VALUES (4, '"Овощи и фрукты"');
INSERT INTO Categories (category_ID, name) VALUES (5, '"Крупы и макароны"');
INSERT INTO Categories (category_ID, name) VALUES (6, '"Хлеб и выпечка"');
INSERT INTO Categories (category_ID, name) VALUES (7, '"Сладости и десерты"');
INSERT INTO Categories (category_ID, name) VALUES (8, '"Напитки"');
INSERT INTO Categories (category_ID, name) VALUES (9, '"Консервация и соусы"');
INSERT INTO Categories (category_ID, name) VALUES (10, '"Замороженные продукты"');
INSERT INTO Categories (category_ID, name) VALUES (11, '"Бакалея"');
INSERT INTO Categories (category_ID, name) VALUES (12, '"Детское питание"');
INSERT INTO Categories (category_ID, name) VALUES (13, '"Диетическое и здоровое питание"');
INSERT INTO Categories (category_ID, name) VALUES (14, '"Бытовая химия и хоз товары"');
INSERT INTO Categories (category_ID, name) VALUES (15, '"Корм для животных"');

-- Таблица: Deliveries
CREATE TABLE IF NOT EXISTS Deliveries (
    delivery_ID INTEGER PRIMARY KEY,
    supplier_ID INTEGER NOT NULL,
    delivery_date DATE NOT NULL,
    FOREIGN KEY (supplier_ID) REFERENCES Suppliers(supplier_ID)
);

-- Таблица: Delivery_product
CREATE TABLE IF NOT EXISTS Delivery_product (
    delivery_product_ID INTEGER PRIMARY KEY,
    delivery_ID INTEGER NOT NULL,
    product_ID INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    FOREIGN KEY (delivery_ID) REFERENCES Deliveries(delivery_ID),
    FOREIGN KEY (product_ID) REFERENCES Products(product_ID)
);

-- Таблица: Employees
CREATE TABLE IF NOT EXISTS Employees (
    employee_ID INTEGER PRIMARY KEY,
    lastname TEXT NOT NULL,
    firstname TEXT NOT NULL,
    position TEXT,
    hiredate DATE
);

-- Таблица: Products
CREATE TABLE IF NOT EXISTS Products (
    product_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category_ID INTEGER NOT NULL,
    price REAL NOT NULL,
    quantity_in_stock INTEGER NOT NULL,
    expiration_date DATE,
    FOREIGN KEY (category_ID) REFERENCES Categories(category_ID)
);

-- Таблица: Sales
CREATE TABLE IF NOT EXISTS Sales (
    sale_ID INTEGER PRIMARY KEY,
    employee_ID INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    product_ID INTEGER NOT NULL,
    FOREIGN KEY (employee_ID) REFERENCES Employees(employee_ID),
    FOREIGN KEY (product_ID) REFERENCES Products(product_ID)
);

-- Таблица: Suppliers
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
