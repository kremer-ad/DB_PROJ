select 
  licence_number,model_name,company_name
from 
  cars_stock
 inner join models
       on models.model_id = cars_stock.model_id
 inner join companies
       on models.company_id =companies.company_id
where company_name = 'Audi'
