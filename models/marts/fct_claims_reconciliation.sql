with claims as (

    select * from {{ ref('stg_claims') }}

),

remittances as (

    select * from {{ ref('stg_remittances') }}

),

joined as (

    select
        c.claim_id,
        c.patient_id,
        c.provider_id,
        c.submission_date,
        c.procedure_code,
        c.billed_amount,
        r.remittance_id,
        r.adjudication_date,
        r.allowed_amount,
        coalesce(r.paid_amount, 0.0) as paid_amount,
        r.denial_reason_code

    from claims as c
    left join remittances as r
        on c.claim_id = r.claim_id

),

enriched as (

    select
        *,
        case
            when adjudication_date is not null
                then date_diff('day', submission_date, adjudication_date)
        end as claim_age_days,
        greatest(billed_amount - coalesce(paid_amount, 0.0), 0.0) as outstanding_balance,
        case
            when remittance_id is null then 'Unpaid'
            when paid_amount = 0 and denial_reason_code is not null then 'Denied'
            when paid_amount >= billed_amount then 'Fully Paid'
            when paid_amount > 0 and paid_amount < billed_amount then 'Partially Paid'
            when paid_amount = 0 then 'Denied'
            else 'Partially Paid'
        end as adjudication_status

    from joined

)

select * from enriched
