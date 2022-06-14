select model_name, company_name , model_year
from models
left join companies
     on models.company_id = companies.company_id
where model_year > 2020
order by model_year
