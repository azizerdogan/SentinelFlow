# SentinelFlow: Healthcare RCM Data Pipeline

Hey, I'm Aziz. I built this ELT pipeline to automate the reconciliation process for Healthcare Revenue Cycle Management (RCM). 

In healthcare billing, providers submit claims, and insurance companies send back remittances (payments, denials, or adjustments). The problem is that these two datasets are usually completely separate, making it really hard to figure out what was paid, what was denied, and what's still outstanding. 

I built this pipeline to take those two raw datasets, clean them up, and automatically join them together into dimensional models so the business can actually track outstanding balances and provider denial rates.

### The Tech Stack
* **dbt Core:** For all the SQL transformations and testing.
* **DuckDB:** Used as a fast, local database so this project can run entirely on a local machine without needing cloud warehouse credentials.
* **Python (Pandas):** Used to generate the mock clinical/financial datasets.

### Why I Built It This Way
Coming from a Quality Assurance background, I care a lot about data integrity. Anyone can write a SQL JOIN, but real-world data is messy. I specifically built this pipeline with a heavy emphasis on automated dbt testing. 

There are 25 tests baked into this project that run every time the pipeline builds. They check for things like:
* Ensuring primary keys are actually unique.
* Enforcing referential integrity (remittances have to match a valid claim).
* Validating business logic (e.g., catching errors if a payment amount or outstanding balance accidentally drops below zero).

### How to Run It Locally
If you want to pull this down and run it yourself, you just need Python installed. It takes about a minute to spin up.

```bash
# 1. Clone the repo and get into the directory
git clone https://github.com/azizerdogan/SentinelFlow.git
cd SentinelFlow

# 2. Install dependencies and generate the mock data
pip install -r requirements.txt
python generate_data.py

# 3. Run the dbt pipeline
# Point dbt to the local directory
$env:DBT_PROFILES_DIR = "."

# Install packages (like dbt_utils)
dbt deps

# Load the CSVs into DuckDB
dbt seed

# Run the transformation models
dbt run

# Run the 25 data quality tests
dbt test
 