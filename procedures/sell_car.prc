create or replace procedure sell_car(licenceNumber in yomalka.cars_stock.licence_number%type) is

csidToDelete yomalka.cars_stock.csid%type;
begin
  select csid into csidToDelete from yomalka.cars_stock where licence_number = licenceNumber;
  delete from treatments where csid = csidToDelete;
  delete from yomalka.cars_stock where csid = csidToDelete;
end sell_car;
/
