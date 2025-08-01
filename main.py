import json
import pandas as pd
import time
import os
from dotenv import load_dotenv
from pyairtable import Api
import cohere

# Load environment variables
load_dotenv()


co = cohere.Client(os.getenv("COHERE_API_KEY"))

def classify_lead(message):
    prompt = f"""Classify the following lead as 'hot', 'warm', or 'cold':
Lead message: "{message}"
Respond only with the classification label."""

    response = co.generate(
        model='command-xlarge',  # Or any available Cohere model
        prompt=prompt,
        max_tokens=10,
        temperature=0
    )
    return response.generations[0].text.strip()


def extract_entities(message):
    prompt = f"""Extract the following from the message:
- Location
- Intent (buy now, research only, long-term plan, not sure)
- Budget if mentioned

Lead message: "{message}"
Respond in JSON format with keys: location, intent, budget."""

    response = co.generate(
        model='command-xlarge',
        prompt=prompt,
        max_tokens=100,
        temperature=0
    )
    try:
        return json.loads(response.generations[0].text.strip())
    except:
        return {"location": "", "intent": "", "budget": ""}


# Load leads from JSON
with open("leads.json", "r") as f:
    leads = json.load(f)

results = []

# Process leads
for lead in leads:
    classification = classify_lead(lead["message"])
    entities = extract_entities(lead["message"])

    results.append({
        "name": lead["name"],
        "budget": lead.get("budget", ""),
        "message": lead["message"],
        "classification": classification,
        "extracted_location": entities.get("location", ""),
        "extracted_intent": entities.get("intent", ""),
        "extracted_budget": entities.get("budget", "")
    })
    time.sleep(2)
    
    

# Save to CSV
df = pd.DataFrame(results)
df.to_csv("qualified_leads.csv", index=False)
print(" Leads saved to qualified_leads.csv")

# Airtable upload
AIRTABLE_PAT = os.getenv("AIRTABLE_PAT")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

api = Api(AIRTABLE_PAT)
base = api.base(AIRTABLE_BASE_ID)
table = base.table(AIRTABLE_TABLE_NAME)

for row in results:
    airtable_data = {
        "Name": row["name"],
        "Budget": row["budget"],
        "Message": row["message"],
        "Classification": row["classification"],
        "Location": row["extracted_location"],
        "Intent": row["extracted_intent"],
        "Extracted Budget": row["extracted_budget"]
    }
    table.create(airtable_data)

print(" Leads uploaded to Airtable!")
