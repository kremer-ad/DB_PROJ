CREATE OR REPLACE VIEW FULL_AVAILABLE_CARS AS
SELECT FULL_CARS_DATA.CSID,
       FULL_CARS_DATA.LICENCE_NUMBER,
       FULL_CARS_DATA.MODEL_NAME,
       FULL_CARS_DATA.COMPANY_NAME,
       FULL_CARS_DATA.BUY_YEAR,
       FULL_CARS_DATA.LOCATION,
       FULL_CARS_DATA.YEARSTART,
       FULL_CARS_DATA.COLOR_NAME
FROM ((SELECT CARS_STOCK.CSID FROM CARS_STOCK

           )

           MINUS (SELECT CARS_STOCK.CSID FROM TREATMENTS
           LEFT JOIN CARS_STOCK
                ON CARS_STOCK.CSID = TREATMENTS.CSID
           WHERE TREATMENTS.END_DATE>CURRENT_DATE))FILTERED
LEFT JOIN FULL_CARS_DATA ON FULL_CARS_DATA.CSID = FILTERED.CSID
