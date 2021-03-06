select model_name,company_name,counter.amount
from (select /*+ INDEX (CARS_STOCK CARS_STOCK_MODEL_ID) */ models.model_id,count(*) as amount from models
      left join cars_stock
           on models.model_id = cars_stock.model_id
      left join treatments
           on cars_stock.csid = treatments.csid
      group by models.model_id) counter
left join models_with_company_name
     on models_with_company_name.model_id = counter.model_id
order by counter.amount desc
