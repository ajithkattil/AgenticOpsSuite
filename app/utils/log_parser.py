def analyze_log(log_text):
    # Placeholder logic
    if "amdgpu" in log_text.lower():
        return {"issue": "Detected AMD GPU driver issue", "confidence": 0.85}
    elif "error" in log_text.lower():
        return {"issue": "Generic error detected", "confidence": 0.60}
    else:
        return {"issue": "No known issue found", "confidence": 0.20}
