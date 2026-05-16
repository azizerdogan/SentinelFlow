with source as (

    select * from {{ source('rcm', 'claims_submitted') }}

),

renamed as (

    select
        trim(claim_id) as claim_id,
        trim(patient_id) as patient_id,
        trim(provider_id) as provider_id,
        cast(submission_date as date) as submission_date,
        upper(trim(procedure_code)) as procedure_code,
        cast(billed_amount as double) as billed_amount

    from source

),

cleaned as (

    select
        claim_id,
        patient_id,
        provider_id,
        submission_date,
        procedure_code,
        coalesce(billed_amount, 0.0) as billed_amount

    from renamed
    where claim_id is not null

)

select * from cleaned
