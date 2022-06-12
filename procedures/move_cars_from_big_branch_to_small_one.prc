--RELOCATES CARS FROM THE BRANCH WITH THE MOST CARS TO THE BRANCH WITH THE LESS CARS
create or replace procedure RELOCATE_CARS is
largest_branch_id INT :=largest_branch();
smallest_branch_id INT :=smallest_branch();
amount_in_largest int := cars_in_branch(largest_branch_id);
amount_in_smallest int := cars_in_branch(smallest_branch_id);
amount_to_move int := (amount_in_largest-amount_in_smallest)/2;
begin
    for car in (select csid from cars_stock where branch_id = largest_branch_id and rownum <amount_to_move)
      loop
        update cars_stock set branch_id = smallest_branch_id where csid = car.csid;
      end loop;
end RELOCATE_CARS;
/
