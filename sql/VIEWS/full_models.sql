create or replace view full_models as
select model_id,model_name,model,company_name from models
left join companies
     on companies.company_id = models.company_idã
