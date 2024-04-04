select f.FLAVOR
from first_half f
join (select FLAVOR, sum(total_order) TOTAL_ORDER
      from july
      group by flavor) j on f.flavor = j.flavor
group by flavor
order by (f.total_order + j.total_order) desc
limit 3
