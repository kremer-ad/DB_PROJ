select garage_name, garage_location, garage_phone_number, amount
from 
    (select garage.garage_id ,count(*) as amount
     from
           treatments
     LEFT join garage
          on treatments.garage_id = garage.garage_id
     where treatments.end_date > CURRENT_DATE
     group by garage.garage_id) counter
inner join garage
on garage.garage_id = counter.garage_id
order by amount desc
