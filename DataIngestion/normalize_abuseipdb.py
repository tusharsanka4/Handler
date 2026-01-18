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
    
