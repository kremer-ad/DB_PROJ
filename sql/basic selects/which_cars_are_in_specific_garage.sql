select licence_number, model_name, company_name, buy_year
from treatments
left join garage
     on garage.garage_id = treatments.garage_id
left join cars_stock
     on cars_stock.csid = treatments.csid
left join models
     on models.model_id = cars_stock.model_id
left join companies
     on companies.company_id = models.company_id
where garage_name = 'נירים מוסך הקבוץ'
