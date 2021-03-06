create or replace function buyCar(licenceNumber in yomalka.cars_stock.licence_number%type,companyName in yomalka.full_models.company_name%type,modelName in yomalka.full_models.model_name%type,modelYear in yomalka.full_models.model_year%type,branchId in barkalif.branch.id%type,colorName in yomalka.colors.color_name%type) return yomalka.garage%rowtype is
  startDate date;
  colorId int;
  modelId int;
  firstTreatmentDuration int := 3;
  endDate date;
  buyYear int;
  results yomalka.garage%rowtype;
  newCarId int;
  garageId int;
  temp int;
  cursor cars_cursor is select csid from cars_stock where cars_stock.licence_number = licenceNumber;
begin
  select sysdate into startDate from dual;
  select (sysdate + firstTreatmentDuration) into endDate  from dual ;
  select extract(year from startDate) into buyYear from dual;
  select model_id into modelId from full_models where model_name = modelName and company_name = companyName and model_year = modelYear ;
  if sql%notfound then
     RAISE NO_DATA_FOUND;
  end if;
  select color_id into colorId from colors where colorName = colors.color_name ;
  if sql%notfound then
     raise NO_DATA_FOUND;
  end if;
  select barkalif.branch.id into temp from barkalif.branch where barkalif.branch.id = branchId;
  if sql%notfound then
    RAISE NO_DATA_FOUND;
  end if;
  --select count(*) into temp from cars_stock where cars_stock.licence_number = licenceNumber;
  open cars_cursor;
  fetch cars_cursor into temp;
  if cars_cursor%found then
    RAISE DUP_VAL_ON_INDEX;
  end if;
  select garage_id into garageId from (select garage_id from garage order by DBMS_RANDOM.RANDOM) where rownum=1 ;
  if sql%notfound then
     RAISE NO_DATA_FOUND;
  end if;
  select * into results from garage where garage_id = garageId;
  insert into cars_stock(
                         licence_number,
                         buy_year,
                         color_id,
                         model_id,
                         branch_id)
                 values (licenceNumber,
                         buyYear,
                         colorId,
                         modelId,
                         branchId) returning csid into newCarId  ;  
   insert into treatments(start_date,
                          end_date,
                          csid,
                          garage_id)
                   values(startDate,
                          endDate,
                          newCarId,
                          garageId);               

  return(results);
end buyCar;
/
