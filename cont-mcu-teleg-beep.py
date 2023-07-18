from flask import Flask, jsonify, request
import requests
import time
import winsound
from datetime import datetime

app = Flask(__name__)

nodeMCU_ip = "192.168.1.190"  # Replace with the IP address of your NodeMCU
telegram_bot_token = "634859xxxxxxxx0"  # Replace with your Telegram bot's token
telegram_chat_id = "81xxxxx20"  # Replace with your Telegram chat ID

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {"chat_id": telegram_chat_id, "text": message}
    requests.post(url, data=data)



@app.route('/')
def hello():
    return jsonify({'name': 'Deha', 'address': 'test data'})

@app.route('/On/', methods=['GET'])
def relay_on():
    print("Gate has opened.\r\n")
    winsound.Beep(500, 700)  # Beep sound
    winsound.Beep(400, 700)  # Beep sound
    requests.get(f"http://{nodeMCU_ip}/relay/on")  # Send "on" command to NodeMCU
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    message = f"🔔🔔Gate🔔🔔 Opened 💡 at time: {current_time} {current_date} by Khanfar Systems ."
    send_telegram_message(message)

    return jsonify({'statusCode': 200, 'msg': 'Success', 'status': 'On'})

@app.route('/Off/', methods=['GET'])
def relay_off():
    print("Gate has closed.\r\n")
    winsound.Beep(400, 700)  # Beep sound
    winsound.Beep(500, 700)  # Beep sound
    requests.get(f"http://{nodeMCU_ip}/relay/off")  # Send "off" command to NodeMCU
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    message = f"🔔🔔Gate 🔔🔔Closed ❌at time: {current_time} {current_date} by Khanfar Systems ."
    send_telegram_message(message)

    return jsonify({'statusCode': 200, 'msg': 'Success', 'status': 'Off'})

@app.route('/OnOff/', methods=['GET'])
def relay_on_off():
    print("Gate has opened.\r\n")
    winsound.Beep(500, 700)  # Beep sound
    winsound.Beep(400, 700)  # Beep sound
    requests.get(f"http://{nodeMCU_ip}/relay/on")  # Send "on" command to NodeMCU
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    message = f"🔔🔔Gate 🔔🔔Opened 💡at time: {current_time} {current_date} by Khanfar Systems."
    send_telegram_message(message)
    time.sleep(2)
    winsound.Beep(400, 700)  # Beep sound
    winsound.Beep(500, 700)  # Beep sound
    requests.get(f"http://{nodeMCU_ip}/relay/off")  # Send "off" command to NodeMCU
    print("Gate has closed.\r\n")
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    message = f"🔔🔔Gate 🔔🔔Closed ❌at time: {current_time} {current_date} by Khanfar Systems."
    send_telegram_message(message)

    return jsonify({'statusCode': 200, 'msg': 'Success', 'status': 'On Off'})

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
