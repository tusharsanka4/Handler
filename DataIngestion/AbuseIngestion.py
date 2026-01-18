from AbuseIPDB import fetch_data
from normalize_abuseipdb import normalize
from insert_mongo import insert_indicators

def main():
    raw = fetch_data()
    normalized = normalize(raw)
    insert_indicators(normalized)
    print(f"[✓] Ingested {len(normalized)} indicators")

if __name__ == "__main__":
    main()
