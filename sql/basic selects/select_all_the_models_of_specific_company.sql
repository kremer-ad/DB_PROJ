select distinct model_name,company_name
from models
left join companies
     on models.company_id = companies.company_id
where company_name = 'Audi'
