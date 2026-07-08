import pandas as pd
import numpy as np
from textblob import TextBlob

def process_and_enhance_data(filepath="Support Ticket Data Generation.xlsx"):
    print("🚀 Ingesting Enterprise Data Stream...")
    df = pd.read_excel(filepath)
    
    # 1. Predictive Demand Layer (Time-Series Machine Learning alternative)
    # Calculates an exponential moving average over time to forecast upcoming workload strains
    df = df.sort_values(by='Date')
    df['Rolling_Workload_Demand'] = df.groupby('Software Name')['Resolution Time (hrs)'].transform(
        lambda x: x.ewm(span=5, adjust=False).mean()
    ).round(2)
    
    # 2. NLP Enrichment Simulation Layer
    # Synthesizes raw text text payloads to simulate a real-world software integration webhook
    def synthesize_unstructured_payload(row):
        software = row['Software Name']
        issue = str(row['Issue Type']).lower()
        if "login" in issue or "auth" in issue:
            return f"CRITICAL: User reports absolute authentication timeout on the {software} cloud environment wrapper module."
        elif "billing" in issue or "payment" in issue:
            return f"WARNING: Invoice calculations do not match total GST fields on {software} distributor checkout."
        else:
            return f"System processing latency is high; {software} server connection dropping intermittently during sync."

    df['Raw_JSON_Payload'] = df.apply(synthesize_unstructured_payload, axis=1)
    
    # 3. Sentiment & Priority Evaluation Layer
    def extract_operational_priority(text):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        # Polarities closer to -1 present high customer distress
        if "CRITICAL" in text or polarity < -0.1:
            return "P1 - CRITICAL (Immediate Escalation)"
        elif "WARNING" in text:
            return "P2 - HIGH (Next-In-Line)"
        else:
            return "P3 - MEDIUM (Standard Queue)"
            
    df['Dynamic_SLA_Priority'] = df['Raw_JSON_Payload'].apply(extract_operational_priority)
    
    return df

if __name__ == "__main__":
    enhanced_df = process_and_enhance_data()
    print("✅ Pipeline Transformed Dataset Successfully.")