{% snapshot users_snapshot %}

{{

	config(
		target_schema = 'snapshots',
		unique_key = 'id',
		strategy = 'check',
		check_cols = ['id', 'user_name', 'email']	

		
	)
}}


select * from {{ source ('source','users') }}


{% endsnapshot %}
