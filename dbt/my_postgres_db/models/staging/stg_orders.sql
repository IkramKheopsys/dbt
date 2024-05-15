with 
 orders as (
	select * from {{ ref ('orders_snapshot') }}
),
final as (

select id,order_id,title,status,date_update,dbt_valid_to from orders where dbt_valid_to is null)



select  * from final 
