# CREATE 

INSERT INTO Nurses

VALUES
    (6210,'Cindy','Lawn','Radiology');

# Read

SELECT *

FROM Appointments

WHERE App_Num = 1005;

# UPDATE

UPDATE Nurses

SET L_Name = 'Murphy'

WHERE Nurse_ID = 6210;

# DELETE
DELETE FROM Nurses

Where Nurse_ID = 6210;
