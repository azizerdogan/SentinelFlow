with reconciliation as (

    select * from {{ ref('fct_claims_reconciliation') }}

),

provider_metrics as (

    select
        provider_id,
        count(distinct claim_id) as total_claims,
        sum(billed_amount) as total_billed_amount,
        sum(paid_amount) as total_paid_amount,
        sum(case when adjudication_status = 'Denied' then 1 else 0 end) as denied_claims,
        round(
            100.0 * sum(case when adjudication_status = 'Denied' then 1 else 0 end)
            / nullif(count(distinct claim_id), 0),
            2
        ) as claim_denial_rate_pct

    from reconciliation
    group by provider_id

)

select * from provider_metrics
