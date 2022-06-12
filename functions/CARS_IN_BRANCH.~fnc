create or replace function CARS_IN_BRANCH(BID IN INT) return integer is
  FunctionResult integer;
begin
  SELECT AMOUNT INTO FunctionResult
  FROM (SELECT BRANCH_ID,COUNT(*) AS AMOUNT FROM CARS_STOCK
       GROUP BY BRANCH_ID)
       WHERE BRANCH_ID = BID;
  return(FunctionResult);
end CARS_IN_BRANCH;
/
