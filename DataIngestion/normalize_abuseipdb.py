import json
from datetime import datetime, timezone

def normalize(raw_abuseipdbdata):
    normalized =[]

    fetched_at = datetime.now(timezone.utc).isoformat()

    for entry in raw_abuseipdbdata.get("data",[]):
        normalized_entry = {
            "indicator": entry["ipAddress"],
            "type": "ip",
            "confidence": entry["abuseConfidenceScore"],
            "country": entry.get("countryCode"),
            "threat_types":["reported_abuse"],
            "sources": [
                {
                    "name": "AbuseIPDB",
                    "score": entry["abuseConfidenceScore"],
                    "last_seen": entry["lastReportedAt"]
                }
            ],
            "first_seen": entry["lastReportedAt"],
            "last_updated": fetched_at
        }

        normalized.append(normalized_entry)

    return normalized
    

if __name__ == "__main__":
    with open("raw_abuseipdbdata.json", "r") as f:
        raw_data=json.load(f)

normalized_data = normalize(raw_data)


with open("normalized_indicators.json", "w") as f:
    json.dump(normalized_data,f,indent = 2)

print("Worked!")