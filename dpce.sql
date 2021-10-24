with estimate_cte as (
select distinct estimate_id,
dim_assets_id,
total
from estimates
where closed_at is not null)

select distinct a.vin,
sum(e.total) over (group by a.vin) as total_per_vin,
sum(e.total) over (group by e.estimate_id) as total_per_operation
from assets a
inner join estimate_cte e
on a.dim_assets_id = e.dim_assets_id