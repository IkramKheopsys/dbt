{% snapshot orders_snapshot %}

{{

	config(
		target_schema = 'snapshots',
		unique_key = 'id',
		strategy = 'timestamp',
		updated_at = 'date_update'	

		
	)
}}


select * from {{ source ('source','orders') }}


{% endsnapshot %}
