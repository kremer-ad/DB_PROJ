select licence_number,model_name,company_name,counter.amount
from (select cars_stock.csid,count(*) as amount from cars_stock
      left join treatments
           on cars_stock.csid = treatments.csid
      group by cars_stock.csid) counter
left join cars_with_model_and_company
     on cars_with_model_and_company.csid = counter.csid
order by counter.amount desc
