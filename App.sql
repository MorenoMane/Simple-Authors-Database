CREATE TABLE PATIENT_INFO (
Patient_ID INTEGER PRIMARY KEY,
F_Name TEXT,
L_Name TEXT,
Age Integer,
Gender Text
);

INSERT INTO PATIENT_INFO(Patient_ID,F_Name,L_Name,Age,Gender)
VALUES
    (3160,'Jake','Cake',60,'Male'),
    (3162,'Luke','Skywalker',21,'Male'),
    (3164,'Mary','Lopez',27,'Female'),
    (3166,'Jake','Smith',41,'Male'),
    (3168,'Peter','Parker',25,'Male');

CREATE TABLE Doctors (
    Doc_ID INT PRIMARY KEY,
    F_Name Text,
    L_Name Text,
    Department Text);

INSERT INTO Doctors(Doc_ID,F_Name,L_Name,Department)
VALUES
    (2,'Don','Julio','Radiology'),
    (4,'Sofia','Jones','Cardiology'),
    (6,'Fiona','Myers','Gynecology'),
    (8,'Alex','Karev','Radiology'),
    (10,'Lexie','Grey','Cardiology');

CREATE TABLE Nurses(
    Nurse_ID INT PRIMARY KEY,
    F_Name Text,
    L_Name Text,
    Department Text);

INSERT into Nurses( Nurse_ID,F_Name,L_Name,Department)
VALUES
    (6200,'John','Lee','Cardiology'),
    (6202,'Susan','Storm','Gynecology'),
    (6204,'Carrie','Underwood','Radiology'),
    (6206,'Katy','Perry','Radiology'),
    (6208,'Stacy','Smith','Cardiology');

CREATE TABLE Appointments(
    App_Num INT PRIMARY KEY,
    Date INT,
    Patient_ID INT,
    Doc_ID INT,
    Nurse_ID INT);

INSERT INTO Appointments
VALUES
    (1001,081023,3162,04,6208),
    (1003,081023,3166,02,6204),
    (1005,090623,3164,06,6202),
    (1007,073023,3162,10,6200),
    (1009,080823,3168,08,6206);

-----CRUD------------------------
CREATE
INSERT INTO Nurses
VALUES
    (6210,'Cindy','Lawn','Radiology');

READ
SELECT *
FROM Appointments
WHERE App_Num = 1005;

UPDATE
UPDATE Nurses
SET L_Name = 'Murphy'
WHERE Nurse_ID = 6210;

DELETE
DELETE FROM Nurses
Where Nurse_ID = 6210;
