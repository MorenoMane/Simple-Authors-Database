# Insert SQL 


INSERT INTO PATIENT_INFO(Patient_ID,F_Name,L_Name,Age,Gender)

    VALUES
    (3160,'Jake','Cake',60,'Male'),
    (3162,'Luke','Skywalker',21,'Male'),
    (3164,'Mary','Lopez',27,'Female'),
    (3166,'Jake','Smith',41,'Male'),
    (3168,'Peter','Parker',25,'Male');

INSERT INTO Doctors(Doc_ID,F_Name,L_Name,Department)

    VALUES
    (2,'Don','Julio','Radiology'),
    (4,'Sofia','Jones','Cardiology'),
    (6,'Fiona','Myers','Gynecology'),
    (8,'Alex','Karev','Radiology'),
    (10,'Lexie','Grey','Cardiology');


INSERT into Nurses( Nurse_ID,F_Name,L_Name,Department)

    VALUES
    (6200,'John','Lee','Cardiology'),
    (6202,'Susan','Storm','Gynecology'),
    (6204,'Carrie','Underwood','Radiology'),
    (6206,'Katy','Perry','Radiology'),
    (6208,'Stacy','Smith','Cardiology');

INSERT INTO Appointments

    VALUES
    (1001,081023,3162,04,6208),
    (1003,081023,3166,02,6204),
    (1005,090623,3164,06,6202),
    (1007,073023,3162,10,6200),
    (1009,080823,3168,08,6206);