# DataBase

The database i chose to produce is appointments for a hospital, it contains information of patient information , doctor information , nurse information and appointment information.

|Nurse_ID|F_Name|L_Name|Department|
|--------|------|------|----------|
|6200|John|Lee|Cardiology|
|6202|Susan|Storm|Gynecology|


Table is in 3NF with NurseId is the primary key 

|Docotor_ID|F_Name|L_Name|Department|
|--------|------|------|----------|
|02|Don|Julio|Radiology|
|04|Sofia|Jones|Cardiology

Table is in 3NF with the DoctorID being primary key


|Patient_ID|F_Name|L_Name|Age|Gender|
|--------|------|------|----------|--|
|3160|Jake|Cake|60|Male|
|3162|Luke|Skywalker|21|Male|

Patient ID is the primary key with table in 3NF

|App_Name|Date|Patient_ID|Doctor_ID|Nurse_ID|
|--------|------|------|----------|----
|1001|081023|3162|04|6208|
|1003|081025|3166|02|6204|

Appointment table is 3nf with 3 forgein keys 

