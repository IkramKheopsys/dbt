
-- update_users_table.sql
{{ config(materialized='incremental') }}


select * from source.data

