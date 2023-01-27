-- Creates four tables in the raw. schema to contain the 100 Patients data
-- Imports the data from the csv files
-- Prior to running the script make sure that the four files are copied into a suitable folder in the Docker container
-- In the original script they got stored in a folder called /imports/
-- Author: Kris Beicher
-- Date 25th Jan 2023

CREATE SCHEMA IF NOT EXISTS raw;

CREATE TABLE IF NOT EXISTS raw.patient_core_populated (
    Patient_id VARCHAR(100),
    Patient_gender VARCHAR(100) NULL,
    Patient_dob VARCHAR(100) NULL,
    Patient_race VARCHAR(500) NULL,
    Patient_marital_status VARCHAR(500) NULL,
    Patient_language VARCHAR(100) NULL,
    Patient_percentage_below_poverty VARCHAR(100) NULL
);
TRUNCATE TABLE raw.patient_core_populated;
-- don't forget to alter the file name unless the csv files were imported into a folder called /imports/
COPY raw.patient_core_populated FROM '/imports/PatientCorePopulatedTable.csv' (FORMAT csv, HEADER, DELIMITER ';');


CREATE TABLE IF NOT EXISTS raw.lab_core_populated (
    Patient_id VARCHAR(100),
    Admission_id VARCHAR(100),
    Lab_name VARCHAR(100) NULL,
    Lab_value VARCHAR(100) NULL,
    Lab_units VARCHAR(100) NULL,
    Lab_Date_time VARCHAR(100) NULL
);
TRUNCATE TABLE raw.lab_core_populated;
-- don't forget to alter the file name unless the csv files were imported into a folder called /imports/
COPY raw.lab_core_populated FROM '/imports/LabsCorePopulatedTable.csv' (FORMAT csv, HEADER, DELIMITER ';');


CREATE TABLE IF NOT EXISTS raw.admissions_core_populated (
    Patient_id VARCHAR(100),
    Admission_id VARCHAR(100),
    Admission_start_date VARCHAR(100) NULL,
    Admission_end_date VARCHAR(100) NULL
);
TRUNCATE TABLE raw.admissions_core_populated;
-- don't forget to alter the file name unless the csv files were imported into a folder called /imports/
COPY raw.admissions_core_populated FROM '/imports/AdmissionsCorePopulatedTable.csv' (FORMAT csv, HEADER, DELIMITER ';');


CREATE TABLE IF NOT EXISTS raw.admissions_diagnoses_core_populated (
    Patient_id VARCHAR(100),
    Admission_id VARCHAR(100),
    Primary_diagnoses_code VARCHAR(100) NULL,
    Primary_diagnoses_description VARCHAR(1000) NULL
);
TRUNCATE TABLE raw.admissions_diagnoses_core_populated;
-- don't forget to alter the file name unless the csv files were imported into a folder called /imports/
SET CLIENT_ENCODING TO LATIN1; -- there is a special char somewhere in the dataset which stops it from importing, this is a crude but effective solution
COPY raw.admissions_diagnoses_core_populated FROM '/imports/AdmissionsDiagnosesCorePopulatedTable.csv' (FORMAT csv, HEADER, DELIMITER ';');

/*
--check that the data has gone into the tables
SELECT * 
FROM "raw"."admissions_core_populated"
LIMIT 2;

SELECT * 
FROM "raw"."admissions_diagnoses_core_populated"
LIMIT 2;

SELECT * 
FROM "raw"."lab_core_populated"
LIMIT 2;

SELECT * 
FROM "raw"."patient_core_populated"
LIMIT 2;
*/