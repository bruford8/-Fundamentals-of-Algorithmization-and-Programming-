--
-- ���� ������������ � ������� SQLiteStudio v3.4.17 � �� ��� 22 11:10:45 2025
--
-- �������������� ��������� ������: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- �������: Categories
CREATE TABLE IF NOT EXISTS Categories (
    category_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
INSERT INTO Categories (category_ID, name) VALUES (1, '"�������� ��������"');
INSERT INTO Categories (category_ID, name) VALUES (2, '"���� � �����"');
INSERT INTO Categories (category_ID, name) VALUES (3, '"���� � ������������"');
INSERT INTO Categories (category_ID, name) VALUES (4, '"����� � ������"');
INSERT INTO Categories (category_ID, name) VALUES (5, '"����� � ��������"');
INSERT INTO Categories (category_ID, name) VALUES (6, '"���� � �������"');
INSERT INTO Categories (category_ID, name) VALUES (7, '"�������� � �������"');
INSERT INTO Categories (category_ID, name) VALUES (8, '"�������"');
INSERT INTO Categories (category_ID, name) VALUES (9, '"����������� � �����"');
INSERT INTO Categories (category_ID, name) VALUES (10, '"������������ ��������"');
INSERT INTO Categories (category_ID, name) VALUES (11, '"�������"');
INSERT INTO Categories (category_ID, name) VALUES (12, '"������� �������"');
INSERT INTO Categories (category_ID, name) VALUES (13, '"����������� � �������� �������"');
INSERT INTO Categories (category_ID, name) VALUES (14, '"������� ����� � ��� ������"');
INSERT INTO Categories (category_ID, name) VALUES (15, '"���� ��� ��������"');

-- �������: Deliveries
CREATE TABLE IF NOT EXISTS Deliveries (
    delivery_ID INTEGER PRIMARY KEY,
    supplier_ID INTEGER NOT NULL,
    delivery_date DATE NOT NULL,
    FOREIGN KEY (supplier_ID) REFERENCES Suppliers(supplier_ID)
);

-- �������: Delivery_product
CREATE TABLE IF NOT EXISTS Delivery_product (
    delivery_product_ID INTEGER PRIMARY KEY,
    delivery_ID INTEGER NOT NULL,
    product_ID INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    FOREIGN KEY (delivery_ID) REFERENCES Deliveries(delivery_ID),
    FOREIGN KEY (product_ID) REFERENCES Products(product_ID)
);

-- �������: Employees
CREATE TABLE IF NOT EXISTS Employees (
    employee_ID INTEGER PRIMARY KEY,
    lastname TEXT NOT NULL,
    firstname TEXT NOT NULL,
    position TEXT,
    hiredate DATE
);

-- �������: Products
CREATE TABLE IF NOT EXISTS Products (
    product_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category_ID INTEGER NOT NULL,
    price REAL NOT NULL,
    quantity_in_stock INTEGER NOT NULL,
    expiration_date DATE,
    FOREIGN KEY (category_ID) REFERENCES Categories(category_ID)
);

-- �������: Sales
CREATE TABLE IF NOT EXISTS Sales (
    sale_ID INTEGER PRIMARY KEY,
    employee_ID INTEGER NOT NULL,
    sale_date DATE NOT NULL,
    product_ID INTEGER NOT NULL,
    FOREIGN KEY (employee_ID) REFERENCES Employees(employee_ID),
    FOREIGN KEY (product_ID) REFERENCES Products(product_ID)
);

-- �������: Suppliers
CREATE TABLE IF NOT EXISTS Suppliers (
    supplier_ID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
