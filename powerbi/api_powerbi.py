from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_PATH = "/home/pi/detecciones.db" 

def get_all_detections():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM detecciones ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()

    detections = [
        {"id": row[0], "timestamp": row[1], "clase": row[2], "probabilidad": row[3]}
        for row in rows
    ]
    return detections

@app.route("/api/detecciones", methods=["GET"])
def api_detecciones():
    detections = get_all_detections()
    return jsonify(detections)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  