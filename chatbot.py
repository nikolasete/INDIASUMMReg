import openai
import telegram
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Inicializa el bot de Telegram
bot = telegram.Bot(token="TU_API_TOKEN_AQUÍ")

# Inicializa el servicio de hojas de cálculo de Google
service = build('sheets', 'v4', credentials=creds)

# Esta función se llamará cada vez que el usuario envíe un mensaje al bot
def handle_message(msg):
    # Recoge el mensaje enviado por el usuario
    text = msg["text"]
    # Recoge el número de teléfono del usuario si ha presionado el botón de "Compartir número de teléfono"
    if "contact" in msg:
        phone_number = msg["contact"]["phone_number"]
    else:
        phone_number = None
    # Recoge la fecha actual
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Añade la información recogida a la hoja de cálculo de Google
    add_data_to_spreadsheet(text, phone_number, date)

# Esta función añade la información recogida a la hoja de cálculo de Google
def add_data_to_spreadsheet(text, phone_number, date):
    # Especifica el ID de la hoja de cálculo de Google y la fila a la que se añadirá la información
    spreadsheet_id = "TU_ID_DE_HOJA_DE_CÁLCULO_AQUÍ"
    row = [text, phone_number, date]
    body = {
        "values": [row]
    }
    result = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range="A1", valueInputOption="RAW", insertDataOption="INSERT_ROWS", body=body).execute()

# Esta función procesa los mensajes enviados por el usuario
def main():
    # Obtiene los últimos mensajes enviados al bot
    updates = bot.get_updates()
    # Procesa cada mensaje enviado
    for update in updates:
        handle_message(update["message"])

# Ejecuta la función principal
if __name__ == "__main__":
    main()
