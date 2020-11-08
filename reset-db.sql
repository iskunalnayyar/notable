DROP TABLE IF EXISTS doctors;
CREATE TABLE doctors (
  doctor_id INTEGER PRIMARY KEY,
  f_name TEXT NOT NULL,
  l_name TEXT NOT NULL
--  created_datetime TEXT NOT NULL,
--  serviced_datetime TEXT NOT NULL,
--  status TEXT NOT NULL,
--  amount REAL NOT NULL
);

INSERT INTO doctors (doctor_id, f_name, l_name)
VALUES (1, 'Kunal', 'Nayyar'),
       (2, 'Jon', 'Doe'),
       (3, 'Jill', 'Biden');

DROP TABLE IF EXISTS patients;
CREATE TABLE patients (
  patient_id INTEGER PRIMARY KEY,
  f_name TEXT NOT NULL,
  l_name TEXT NOT NULL

);

INSERT INTO patients (patient_id, f_name, l_name)
VALUES (1, "Dheeraj", "Nayyar"),
       (2, "Smith", "Todd"),
       (3, "Mila", "Todd"),
       (4, "Hu", "Kim");


DROP TABLE IF EXISTS appointments;
CREATE TABLE appointments (
  appointment_id INTEGER PRIMARY KEY,
  created_datetime DATE NOT NULL,
  visit_type INTEGER,

  patient_id INTEGER,
  doctor_id INTEGER,
  CONSTRAINT fk_patients FOREIGN KEY(patient_id) REFERENCES patients(patient_id),
  CONSTRAINT fk_doctors FOREIGN KEY(doctor_id) REFERENCES doctors(doctor_id)
);


INSERT INTO appointments (appointment_id, created_datetime, patient_id, doctor_id, visit_type)
VALUES (1, "2018-03-01T12:03:46.464116", 1, 1, 1),
       (2, "2018-03-01T16:03:46.464116", 3, 2, 0),
       (3, "2018-04-01T12:03:46.464116", 2, 3, 0),
       (4, "2018-05-01T12:03:46.464116", 4, 1, 1);
