create or replace function SMALLEST_BRANCH return INT is
  FunctionResult INT ;
begin
select bid into FunctionResult from(
  select bid,amount
  from (select barkalif.branch.id as bid,count(*) as amount from cars_stock
        left join barkalif.branch
             on cars_stock.branch_id = barkalif.branch.id
        group by barkalif.branch.id) counter
  order by counter.amount
) where rownum = 1;
  return(FunctionResult);
end SMALLEST_BRANCH;
/
