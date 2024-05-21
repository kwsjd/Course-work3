# app.py
from flask import Flask, render_template, request, send_file
from data_generator import DataGenerator
import csv
import json

app = Flask(__name__)
generator = DataGenerator()


def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        if data:
            writer = None
            for data_type, items in data.items():

                if items:
                    if not writer:
                        headers = list(items[0].keys()) if items else []
                        writer = csv.DictWriter(csvfile, fieldnames=headers)
                        writer.writeheader()
                    writer.writerows(items)
                else:
                    print(f"No data available for {data_type}")
        else:
            csvfile.write("No data available")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/custom_data')
def custom_data():
    return render_template('custom_data.html')


@app.route('/generate', methods=['POST'])
def generate_data():
    data_type = request.form.get('data_type')
    count = request.form.get('count', default=1, type=int)
    file_format = request.form.get('file_format', 'json')
    data_generators = {
        'profiles': generator.generate_profiles,
        'vehicles': generator.generate_vehicle_data,
        'financial_records': generator.generate_financial_data,
        'events': generator.generate_event_data,
        'contact_info': generator.generate_contact_info,
        'identification_data': generator.generate_identification_data,
        'organization_data': generator.generate_organization_data,
        'geographic_data': generator.generate_geographic_data,
        'date_time_data': generator.generate_date_time_data,
        'financial_data_extended': generator.generate_financial_data_extended,
        'medical_data': generator.generate_medical_data,
        'educational_data': generator.generate_educational_data,
        'product_data_extended': generator.generate_product_data_extended,
        'technical_data': generator.generate_technical_data,
        'user_web_data': generator.generate_user_web_data,
        'media_data': generator.generate_media_data,
        'weather_data': generator.generate_weather_data,
        'transport_data': generator.generate_transport_data,
        'food_data': generator.generate_food_data
    }
    data_function = data_generators.get(data_type)
    if data_function:
        data = data_function(count)
    else:
        data = []

    if file_format == 'csv':
        csv_filename = f'generated_{data_type}.csv'
        save_to_csv(data, csv_filename)
        return send_file(csv_filename, as_attachment=True, download_name=csv_filename)
    else:  # JSON по умолчанию
        json_filename = f'generated_{data_type}.json'
        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        return send_file(json_filename, as_attachment=True, download_name=json_filename)


@app.route('/generate_custom', methods=['POST'])
def generate_custom_data():
    selected_data_types = request.form.getlist('data_types')
    file_format = request.form.get('file_format', 'json')
    count = int(request.form.get('count', 1))

    print("Selected data types:", selected_data_types)  # Логируем выбранные типы данных

    # Создаем экземпляр DataGenerator
    generator = DataGenerator()

    # Собираем данные из всех выбранных типов
    data = {}
    for data_type in selected_data_types:
        method_name = 'generate_' + data_type
        print("Looking for method:", method_name)  # Логируем имя искомого метода
        data_function = getattr(generator, method_name, None)
        if callable(data_function):
            data[data_type] = data_function(count)
            print(
                f"Data generated for {data_type}: {data[data_type][:1]}")  # Логируем первый элемент сгенерированных данных (если есть)
        else:
            print(f"Method not found: {method_name}")  # Логируем, если метод не найден

    # Генерируем файл для скачивания
    if file_format == 'csv':
        csv_filename = 'custom_data.csv'
        save_to_csv(data, csv_filename)
        print(f"CSV file saved: {csv_filename}")  # Логируем сохранение файла CSV
        return send_file(csv_filename, as_attachment=True, download_name=csv_filename)
    else:  # JSON по умолчанию
        json_filename = 'custom_data.json'
        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
        print(f"JSON file saved: {json_filename}")  # Логируем сохранение файла JSON
        return send_file(json_filename, as_attachment=True, download_name=json_filename)


if __name__ == "__main__":
    app.run(debug=True)
