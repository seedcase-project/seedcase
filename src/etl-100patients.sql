-- Creates four tables in the public. schema to contain the 100 Patients data in the correct format
-- Runs a version of ETL on the data from the raw. tables to the public.

CREATE TABLE IF NOT EXISTS public.patient_core (
    Patient_id VARCHAR(100),
    Patient_gender VARCHAR(10) NULL,
    Patient_dob DATE NULL,
    Patient_race VARCHAR(50) NULL,
    Patient_marital_status VARCHAR(50) NULL,
    Patient_language VARCHAR(50) NULL,
    Patient_percentage_below_poverty NUMERIC(6,3) NULL
);

TRUNCATE TABLE public.patient_core;

INSERT INTO public.patient_core (Patient_id,
                                 Patient_gender,
                                 Patient_dob,
                                 Patient_race,
                                 Patient_marital_status,
                                 Patient_language,
                                 Patient_percentage_below_poverty)
SELECT PC.Patient_id
      ,PC.Patient_gender
      ,TO_DATE(PC.Patient_dob, 'YYYY-MM-DD')
      ,PC.Patient_race
      ,PC.patient_marital_status
      ,PC.patient_language
      ,TO_NUMBER(REPLACE(PC.Patient_percentage_below_poverty, ',','.'), '999D99')
      -- please note, the REPLACE is due to the devs version of Excel playing silly buggers with the number format (Danish organisation with UK installation of Office)
FROM raw.patient_core_populated PC;


CREATE TABLE IF NOT EXISTS public.lab_core (
    Patient_id VARCHAR(100),
    Admission_id INT,
    Lab_name VARCHAR(50) NULL,
    Lab_value NUMERIC(8,3) NULL,
    Lab_units VARCHAR(15) NULL,
    Lab_Date_time TIMESTAMP NULL
);
TRUNCATE TABLE public.lab_core;

INSERT INTO public.lab_core (Patient_id,
                             Admission_id,
                             Lab_name,
                             Lab_value,
                             Lab_units,
                             Lab_Date_time
                            )

SELECT La.Patient_id
      ,CAST(La.Admission_id AS INT)
      ,La.Lab_name
      ,TO_NUMBER(REPLACE(La.Lab_value, ',','.'), '9999D99')
      -- please note, the REPLACE is due to the devs version of Excel playing silly buggers with the number format (Danish organisation with UK installation of Office)
      ,La.Lab_units
      ,TO_TIMESTAMP(La.Lab_Date_time, 'YYYY-MM-DD HH24:MI:SS.MS')
FROM raw.lab_core_populated La;


CREATE TABLE IF NOT EXISTS public.admissions_core (
    Patient_id VARCHAR(100),
    Admission_id INT,
    Admission_start_date TIMESTAMP NULL,
    Admission_end_date TIMESTAMP NULL
);
TRUNCATE TABLE public.admissions_core;

INSERT INTO public.admissions_core (Patient_id,
                                    Admission_id,
                                    Admission_start_date,
                                    Admission_end_date
                                    )

SELECT Ad.Patient_id
      ,CAST(Ad.Admission_id AS INT)
      ,TO_TIMESTAMP(Ad.admission_start_date, 'YYYY-MM-DD HH24:MI:SS.MS')
      ,TO_TIMESTAMP(Ad.Admission_end_date, 'YYYY-MM-DD HH24:MI:SS.MS')
FROM raw.admissions_core_populated AS Ad;


CREATE TABLE IF NOT EXISTS public.admissions_diagnoses_core (
    Patient_id VARCHAR(100),
    Admission_id VARCHAR(100),
    Primary_diagnoses_code VARCHAR(10) NULL,
    Primary_diagnoses_description VARCHAR(200) NULL
);
TRUNCATE TABLE public.admissions_diagnoses_core;

INSERT INTO public.admissions_diagnoses_core (Patient_id,
                                              Admission_id,
                                              Primary_diagnoses_code,
                                              Primary_diagnoses_description
                                              )

SELECT Adc.Patient_id
      ,CAST(Adc.Admission_id AS INT)
      ,Adc.Primary_diagnoses_code
      ,Adc.Primary_diagnoses_description
FROM raw.admissions_diagnoses_core_populated Adc;
