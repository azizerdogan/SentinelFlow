"""Generate mock Healthcare RCM seed data for dbt."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

SEEDS_DIR = Path(__file__).resolve().parent / "seeds"
SEEDS_DIR.mkdir(parents=True, exist_ok=True)

CLAIMS = [
    ("CLM-10001", "PAT-501", "PRV-201", "2025-01-05", "99213", 250.00),
    ("CLM-10002", "PAT-502", "PRV-201", "2025-01-08", "99214", 380.00),
    ("CLM-10003", "PAT-503", "PRV-202", "2025-01-10", "93000", 175.00),
    ("CLM-10004", "PAT-504", "PRV-203", "2025-01-12", "27447", 4200.00),
    ("CLM-10005", "PAT-505", "PRV-202", "2025-01-15", "99213", 225.00),
    ("CLM-10006", "PAT-506", "PRV-204", "2025-01-18", "99215", 520.00),
    ("CLM-10007", "PAT-507", "PRV-203", "2025-01-20", "99203", 310.00),
    ("CLM-10008", "PAT-508", "PRV-201", "2025-01-22", "36415", 45.00),
    ("CLM-10009", "PAT-509", "PRV-204", "2025-01-25", "99214", 395.00),
    ("CLM-10010", "PAT-510", "PRV-205", "2025-01-28", "99213", 240.00),
    ("CLM-10011", "PAT-511", "PRV-205", "2025-02-01", "99204", 450.00),
    ("CLM-10012", "PAT-512", "PRV-202", "2025-02-03", "93000", 180.00),
    ("CLM-10013", "PAT-513", "PRV-203", "2025-02-05", "99213", 260.00),
    ("CLM-10014", "PAT-514", "PRV-204", "2025-02-08", "99214", 370.00),
    ("CLM-10015", "PAT-515", "PRV-201", "2025-02-10", "99215", 510.00),
    ("CLM-10016", "PAT-516", "PRV-205", "2025-02-12", "27447", 3950.00),
    ("CLM-10017", "PAT-517", "PRV-202", "2025-02-15", "99213", 235.00),
    ("CLM-10018", "PAT-518", "PRV-203", "2025-02-18", "36415", 50.00),
    ("CLM-10019", "PAT-519", "PRV-204", "2025-02-20", "99203", 295.00),
    ("CLM-10020", "PAT-520", "PRV-201", "2025-02-22", "99214", 365.00),
    ("CLM-10021", "PAT-521", "PRV-205", "2025-03-01", "99213", 255.00),
    ("CLM-10022", "PAT-522", "PRV-202", "2025-03-03", "99215", 535.00),
    ("CLM-10023", "PAT-523", "PRV-203", "2025-03-05", "93000", 170.00),
    ("CLM-10024", "PAT-524", "PRV-204", "2025-03-08", "99214", 400.00),
    ("CLM-10025", "PAT-525", "PRV-201", "2025-03-10", "99213", 245.00),
]

# Fully paid, partially paid, denied, and unpaid (no remittance row)
REMITTANCES = [
    ("REM-20001", "CLM-10001", "2025-01-20", 200.00, 200.00, None),
    ("REM-20002", "CLM-10002", "2025-01-25", 300.00, 300.00, None),
    ("REM-20003", "CLM-10003", "2025-01-28", 140.00, 140.00, None),
    ("REM-20004", "CLM-10004", "2025-02-05", 3200.00, 1800.00, None),
    ("REM-20005", "CLM-10005", "2025-02-01", 0.00, 0.00, "CO-11"),
    ("REM-20006", "CLM-10006", "2025-02-10", 420.00, 420.00, None),
    ("REM-20007", "CLM-10007", "2025-02-12", 250.00, 125.00, None),
    ("REM-20008", "CLM-10008", "2025-02-15", 35.00, 35.00, None),
    ("REM-20009", "CLM-10009", "2025-02-18", 0.00, 0.00, "PR-1"),
    ("REM-20010", "CLM-10010", "2025-02-22", 190.00, 190.00, None),
    ("REM-20011", "CLM-10011", "2025-03-01", 380.00, 200.00, None),
    ("REM-20012", "CLM-10012", "2025-03-03", 0.00, 0.00, "CO-11"),
    ("REM-20013", "CLM-10013", "2025-03-08", 210.00, 210.00, None),
    ("REM-20014", "CLM-10014", "2025-03-10", 290.00, 145.00, None),
    ("REM-20015", "CLM-10015", "2025-03-12", 410.00, 410.00, None),
    ("REM-20016", "CLM-10016", "2025-03-15", 0.00, 0.00, "PR-1"),
    ("REM-20017", "CLM-10017", "2025-03-18", 185.00, 185.00, None),
    ("REM-20018", "CLM-10018", "2025-03-20", 40.00, 40.00, None),
    ("REM-20019", "CLM-10019", "2025-03-22", 0.00, 0.00, "CO-11"),
    ("REM-20020", "CLM-10020", "2025-03-25", 300.00, 300.00, None),
    ("REM-20021", "CLM-10021", "2025-04-01", 200.00, 100.00, None),
    ("REM-20022", "CLM-10022", "2025-04-03", 430.00, 430.00, None),
    ("REM-20023", "CLM-10023", "2025-04-05", 0.00, 0.00, "PR-1"),
    ("REM-20024", "CLM-10024", "2025-04-08", 320.00, 320.00, None),
    # CLM-10025 intentionally has no remittance (Unpaid)
]


def main() -> None:
    claims_df = pd.DataFrame(
        CLAIMS,
        columns=[
            "claim_id",
            "patient_id",
            "provider_id",
            "submission_date",
            "procedure_code",
            "billed_amount",
        ],
    )
    claims_df["submission_date"] = pd.to_datetime(claims_df["submission_date"]).dt.date

    remittances_df = pd.DataFrame(
        REMITTANCES,
        columns=[
            "remittance_id",
            "claim_id",
            "adjudication_date",
            "allowed_amount",
            "paid_amount",
            "denial_reason_code",
        ],
    )
    remittances_df["adjudication_date"] = pd.to_datetime(
        remittances_df["adjudication_date"]
    ).dt.date

    claims_path = SEEDS_DIR / "claims_submitted.csv"
    remittances_path = SEEDS_DIR / "insurance_remittances.csv"

    claims_df.to_csv(claims_path, index=False)
    remittances_df.to_csv(remittances_path, index=False)

    print(f"Wrote {len(claims_df)} claims to {claims_path}")
    print(f"Wrote {len(remittances_df)} remittances to {remittances_path}")
    print(f"Unpaid claims (no remittance): CLM-10025")


if __name__ == "__main__":
    main()
