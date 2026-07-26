from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/triage', methods=['POST'])
def triage():
    data = request.json
    symptom = data.get('symptom', '').lower().strip()
    
    if 'vomit' in symptom or 'diarrhea' in symptom:
        risk = "Moderate Risk ⚠️"
        advice = "Withhold food for 2-4 hours, provide small sips of water. If symptoms persist beyond 24 hours, consult your veterinarian."
    elif 'scratch' in symptom or 'ear' in symptom or 'itching' in symptom:
        risk = "Low to Moderate 🟡"
        advice = "Inspect for fleas, ticks, or ear irritation. Clean gently with a vet-approved saline wipe. Avoid human medications."
    elif 'lethargy' in symptom or 'weak' in symptom or 'fever' in symptom:
        risk = "High Risk / Emergency 🚨"
        advice = "Severe lethargy or weakness indicates potential systemic infection. Schedule an immediate veterinary evaluation."
    else:
        risk = "Low Risk 🟢"
        advice = "Continue regular monitoring, hydration, and scheduled feeding routines. Consult a vet if new symptoms develop."

    return jsonify({"risk": risk, "advice": advice})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query = data.get('query', '').lower().strip()
    
    if 'vaccine' in query or 'shot' in query:
        reply = "💉 **[PawGPT Medical AI]:** Core immunizations include Rabies, DHPP, and Bordetella. Ensure booster timelines are logged in your care schedule."
    elif 'food' in query or 'diet' in query or 'nutrition' in query:
        reply = "🍲 **[PawGPT Nutrition AI]:** Maintain balanced macronutrients with lean proteins. Strictly avoid toxic compounds such as xylitol, chocolate, grapes, and alliums."
    else:
        reply = f"🤖 **[PawGPT AI Clinical Engine]:** Analyzed query regarding '{query}'; recommend standard clinical observation, balanced hydration, and scheduled veterinary follow-ups."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True, port=5000)