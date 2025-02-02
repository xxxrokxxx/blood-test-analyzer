# Import the blood test analyzer implementation we created earlier
from dataclasses import dataclass
from typing import Dict, List, Optional

class BloodTestAnalyzer:
    # ... (paste the implementation we created earlier)

def handle_analyze_blood_test(params):
    content = params["content"]
    analyzer = BloodTestAnalyzer(content)
    return analyzer.get_analysis()

# Map the handler to the tool name
handlers = {
    "analyze_blood_test": handle_analyze_blood_test
}
