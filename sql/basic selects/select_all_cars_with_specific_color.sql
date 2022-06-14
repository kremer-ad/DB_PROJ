select 
  licence_number,model_name,company_name, color_name
from 
  (select * 
      from  cars_stock
      left join colors
           on colors.color_id = cars_stock.color_id
      where color_name = 'Black') filtered

 left join models
       on models.model_id = filtered.model_id
 left join companies
       on models.company_id =companies.company_id

