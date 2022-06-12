create or replace view cars_in_each_model as
select model_name,company_name,amount
    from 
   (select models.model_id, count(*) as amount
        from cars_stock
        left join models
             on models.model_id = cars_stock.model_id
        group by models.model_id) counter
inner join models
      on models.model_id = counter.model_id
inner join companies
      on models.company_id = companies.company_id
