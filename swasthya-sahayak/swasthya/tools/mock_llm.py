import json

class MockLLM:
    """Mock LLM for offline demos. Replace with ADK/Gemini calls in production."""
    def generate(self, prompt: str, temperature: float=0.0):
        text = prompt.lower()
        if 'fever' in text and ('vomit' in text or 'vomiting' in text):
            return {'role':'assistant','content': json.dumps({'severity':'medium','recommended_action':'Visit clinic within 24 hours.','confidence':0.78,'followup_questions':['Any rash?']})}
        if 'chest' in text or 'shortness' in text:
            return {'role':'assistant','content': json.dumps({'severity':'high','recommended_action':'Seek emergency care immediately.','confidence':0.95,'followup_questions':['Onset?']})}
        if 'wound' in text or 'swollen' in text:
            return {'role':'assistant','content': json.dumps({'severity':'medium-high','recommended_action':'Clean wound and visit clinic.','confidence':0.85,'followup_questions':['How long?']})}
        if 'inventory' in text or 'stock' in text:
            return {'role':'assistant','content': json.dumps({'inventory_summary':'2 items expiring, 1 predicted stockout.','recommendations':[{'medicine':'Ibuprofen','qty_to_order':100}]})}
        return {'role':'assistant','content': json.dumps({'severity':'low','recommended_action':'Monitor; follow up if worsens.','confidence':0.6,'followup_questions':[]})}