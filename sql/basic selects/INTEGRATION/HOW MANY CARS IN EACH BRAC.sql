select BRANCH.LOCATION, YEARSTART, amount
from 
    (select BARKALIF.BRANCH.ID AS BID ,count(*) as amount
     from
           cars_stock
     LEFT join BARKALIF.BRANCH
          on cars_stock.BRANCH_ID = BARKALIF.BRANCH.ID
     group by BARKALIF.BRANCH.ID) counter
inner join BARKALIF.BRANCH
on BARKALIF.BRANCH.ID = counter.BID
order by amount desc
