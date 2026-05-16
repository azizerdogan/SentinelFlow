with source as (

    select * from {{ source('rcm', 'insurance_remittances') }}

),

renamed as (

    select
        trim(remittance_id) as remittance_id,
        trim(claim_id) as claim_id,
        cast(adjudication_date as date) as adjudication_date,
        cast(allowed_amount as double) as allowed_amount,
        cast(paid_amount as double) as paid_amount,
        nullif(trim(denial_reason_code), '') as denial_reason_code

    from source

),

cleaned as (

    select
        remittance_id,
        claim_id,
        adjudication_date,
        coalesce(allowed_amount, 0.0) as allowed_amount,
        greatest(coalesce(paid_amount, 0.0), 0.0) as paid_amount,
        denial_reason_code

    from renamed
    where remittance_id is not null
      and claim_id is not null

)

select * from cleaned
