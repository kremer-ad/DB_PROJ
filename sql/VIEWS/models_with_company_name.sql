create or replace view models_with_company_name as
select models.model_id,model_name,companies.company_name
from models
     left join companies
          on models.company_id = companies.company_id;
