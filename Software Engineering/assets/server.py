from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database simulation
weather_data = {
    "New York": {"temperature": "5°C", "condition": "Cloudy"},
    "Los Angeles": {"temperature": "18°C", "condition": "Sunny"},
}

@app.route('/weather', methods=['GET'])
@app.route('/weather/<city>', methods=['GET'])
def get_weather(city=None):
    if city:
        city = city.title()
        if city in weather_data:
            return jsonify({city: weather_data[city]})
        else:
            return jsonify({"error": "City not found"}), 404
    else:
        return jsonify(weather_data)

@app.route('/weather', methods=['POST'])
def add_weather():
    if not request.json or 'city' not in request.json or 'temperature' not in request.json or 'condition' not in request.json:
        return jsonify({"error": "Invalid request"}), 400
    city = request.json['city'].title()
    weather_data[city] = {"temperature": request.json['temperature'], "condition": request.json['condition']}
    return jsonify({city: weather_data[city]}), 201


@app.route('/weather/<city>', methods=['PUT'])
def update_weather(city):
    city = city.title()
    if city not in weather_data:
        return jsonify({"error": "City not found"}), 404
    if not request.json:
        return jsonify({"error": "Invalid request"}), 400
    weather_data[city] = {"temperature": request.json.get('temperature', weather_data[city]['temperature']),
                          "condition": request.json.get('condition', weather_data[city]['condition'])}
    return jsonify({city: weather_data[city]})

@app.route('/weather/<city>', methods=['DELETE'])
def delete_weather(city):
    city = city.title()
    if city in weather_data:
        del weather_data[city]
        return jsonify({"success": f"{city}'s weather deleted"}), 200
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
