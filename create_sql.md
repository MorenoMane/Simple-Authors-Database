# SQL TO MAKE TABLES

CREATE TABLE PATIENT_INFO
(Patient_ID INTEGER PRIMARY KEY,
    F_Name TEXT,
    L_Name TEXT,
    Age Integer,
    Gender Text);


CREATE TABLE Doctors (
    Doc_ID INT PRIMARY KEY,
    F_Name Text,
    L_Name Text,
    Department Text);

CREATE TABLE Nurses(
    Nurse_ID INT PRIMARY KEY,
    F_Name Text,
    L_Name Text,
    Department Text);

CREATE TABLE Appointments(
    App_Num INT PRIMARY KEY,
    Date INT,
    Patient_ID INT,
    Doc_ID INT,
    Nurse_ID INT);