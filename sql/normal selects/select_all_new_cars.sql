select licence_number,buy_year , model_name, company_name
from cars_stock 
left join models
     on models.model_id = CARS_STOCK.model_id
left join companies
     on models.model_id = companies.company_id
where buy_year >2020
