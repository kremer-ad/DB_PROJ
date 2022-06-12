CREATE OR REPLACE VIEW FULL_TREATMENTS AS
SELECT LICENCE_NUMBER,MODEL_NAME,CARS_WITH_MODEL_AND_COMPANY.COMPANY_NAME,GARAGE_NAME,GARAGE.GARAGE_PHONE_NUMBER,GARAGE.GARAGE_LOCATION, START_DATE, END_DATE
FROM TREATMENTS
LEFT JOIN CARS_WITH_MODEL_AND_COMPANY
     ON CARS_WITH_MODEL_AND_COMPANY.CSID = TREATMENTS.CSID
LEFT JOIN GARAGE
     ON GARAGE.GARAGE_ID = TREATMENTS.GARAGE_ID;