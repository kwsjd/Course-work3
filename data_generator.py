# data_generator.py
from datetime import datetime, timedelta
from faker import Faker
import json
import random
import string

class DataGenerator:

    def __init__(self):
        self.fake = Faker()


    def generate_random_string(self, length=10):
        """Генерирует случайную строку заданной длины."""
        allowed_chars = string.ascii_letters + string.digits
        return ''.join(random.choice(allowed_chars) for _ in range(length))

    def generate_random_date(self, start_year=2000, end_year=2022):
        """
        Генерирует случайную дату между двумя годами.
        """
        year = random.randint(start_year, end_year)
        month = random.randint(1, 12)
        day = random.randint(1, 28)  # берем 28, чтобы избежать проблем с февралем
        random_date = datetime(year, month, day)
        return random_date

    def save_to_json(self, data, file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def generate_profiles(self, count):
        """Генерирует список профилей пользователей."""
        profiles = []
        for _ in range(count):
            profile = {
                "name": self.fake.name(),
                "address": self.fake.address(),
                "email": self.fake.email(),
                "birthdate": str(self.fake.date_of_birth()),
                "company": self.fake.company(),
                "job": self.fake.job()
            }
            profiles.append(profile)
        return profiles

    def generate_product_data(self, count):
        """Генерирует список данных о товарах."""
        products = []
        for _ in range(count):
            product = {
                "name": self.fake.word().capitalize() + " " + self.fake.word(),
                "sku": self.generate_random_string(8).upper(),  # SKU - Stock Keeping Unit
                "price": round(random.uniform(10.0, 1000.0), 2),
                "quantity": random.randint(1, 100),
                "category": self.fake.word(),
                "description": self.fake.text(max_nb_chars=100),
                "manufacturer": self.fake.company(),
                "weight": round(random.uniform(0.5, 20.0), 2),
                "color": self.fake.color_name(),
                "size": f"{random.randint(1, 100)}x{random.randint(1, 100)}x{random.randint(1, 100)} cm"
            }
            products.append(product)
        return products

    def generate_vehicle_data(self, count):
        """Генерирует список данных о транспортных средствах."""
        vehicles = []
        for _ in range(count):
            vehicle = {
                "make": self.fake.company(),
                "model": self.fake.word().capitalize(),
                "year": random.randint(1990, datetime.now().year),
                "vin": self.generate_random_string(17).upper(),
                "color": self.fake.color_name(),
                "mileage": random.randint(0, 300000),
                "price": round(random.uniform(5000.0, 70000.0), 2)
            }
            vehicles.append(vehicle)
        return vehicles

    def generate_financial_data(self, count):
        """Генерирует список финансовых данных."""
        financial_records = []
        for _ in range(count):
            record = {
                "account_number": self.generate_random_string(12).upper(),
                "account_type": random.choice(["Checking", "Savings", "Investment"]),
                "balance": round(random.uniform(1000.0, 100000.0), 2),
                "currency": self.fake.currency_code(),
                "owner": self.fake.name(),
                "bank_name": self.fake.company()
            }
            financial_records.append(record)
        return financial_records

    def generate_event_data(self, count):
        """Генерирует список данных о мероприятиях."""
        events = []
        for _ in range(count):
            event = {
                "title": self.fake.sentence(nb_words=6),
                "date": self.generate_random_date(2020, 2023).strftime("%Y-%m-%d"),
                "time": f"{random.randint(0, 23)}:{random.randint(0, 59):02d}",
                "location": self.fake.address(),
                "organizer": self.fake.company(),
                "description": self.fake.text(max_nb_chars=200)
            }
            events.append(event)
        return events



    def generate_contact_info(self, count):
        """Генерирует список контактной информации."""
        contact_info_list = []
        for _ in range(count):
            contact_info = {
                "phone_number": self.fake.phone_number(),
                "fax_number": self.fake.phone_number(),
                "postcode": self.fake.postcode(),
                "country": self.fake.country()
            }
            contact_info_list.append(contact_info)
        return contact_info_list

    def generate_identification_data(self, count):
        """Генерирует список идентификационных данных."""
        identification_data_list = []
        for _ in range(count):
            identification_data = {
                "ssn": self.fake.ssn(),
                "passport_number": self.fake.bothify(text='??########', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                "tax_id": self.fake.bothify(text='###-##-####')
            }
            identification_data_list.append(identification_data)
        return identification_data_list

    def generate_organization_data(self, count):
        """Генерирует данные организаций."""
        organizations = []
        for _ in range(count):
            organization = {
                "company_name": self.fake.company(),
                "industry": self.fake.job(),
                "department": self.fake.bs(),
                "employee_count": random.randint(1, 10000)
            }
            organizations.append(organization)
        return organizations

    def generate_geographic_data(self, count):
        """Генерирует географические данные."""
        geographic_data = []
        for _ in range(count):
            data = {
                "country": self.fake.country(),
                "city": self.fake.city(),
                "street_address": self.fake.street_address(),
                "latitude": self.fake.latitude(),
                "longitude": self.fake.longitude()
            }
            geographic_data.append(data)
        return geographic_data

    def generate_date_time_data(self, count):
        """Генерирует данные о дате и времени."""
        date_time_data = []
        for _ in range(count):
            data = {
                "date": self.fake.date(),
                "time": self.fake.time(),
                "date_time": self.fake.date_time().isoformat(),
                "time_delta": str(timedelta(days=random.randint(1, 365)))
            }
            date_time_data.append(data)
        return date_time_data

    def generate_financial_data_extended(self, count):
        """Генерирует расширенные финансовые данные."""
        financial_data = []
        for _ in range(count):
            data = {
                "credit_card_number": self.fake.credit_card_number(),
                "transaction_amount": round(random.uniform(100.0, 10000.0), 2),
                "currency": self.fake.currency_code()
            }
            financial_data.append(data)
        return financial_data

    def generate_medical_data(self, count):
        """Генерирует медицинские данные."""
        medical_data = []
        for _ in range(count):
            data = {
                "symptom": self.fake.word(),
                "diagnosis": self.fake.sentence(),
                "medicine": self.fake.word(),
                "doctor": self.fake.name()
            }
            medical_data.append(data)
        return medical_data

    def generate_educational_data(self, count):
        """Генерирует образовательные данные."""
        educational_data = []
        for _ in range(count):
            data = {
                "course": self.fake.word(),
                "specialization": self.fake.sentence(),
                "institution": self.fake.company(),
                "grade": random.choice(['A', 'B', 'C', 'D', 'F'])
            }
            educational_data.append(data)
        return educational_data

    def generate_product_data_extended(self, count):
        """Генерирует данные о продуктах и услугах."""
        products = []
        for _ in range(count):
            product = {
                "product_name": self.fake.word().capitalize() + " " + self.fake.word(),
                "category": self.fake.word(),
                "price": round(random.uniform(10.0, 1000.0), 2),
                "description": self.fake.text(max_nb_chars=100)
            }
            products.append(product)
        return products

    def generate_technical_data(self, count):
            """Генерирует технические данные."""
            technical_data = []
            for _ in range(count):
                data = {
                    "ip_address": self.fake.ipv4(),
                    "mac_address": self.fake.mac_address(),
                    "domain_name": self.fake.domain_name()
                }
                technical_data.append(data)
            return technical_data

    def generate_user_web_data(self, count):
            """Генерирует данные пользователей для веб-сайтов."""
            user_web_data = []
            for _ in range(count):
                data = {
                    "username": self.fake.user_name(),
                    "password": self.fake.password(),
                    "email": self.fake.email(),
                    "profile_image": self.fake.image_url()
                }
                user_web_data.append(data)
            return user_web_data

    def generate_media_data(self, count):
        """Генерирует данные о медиа-контенте."""
        media_data = []
        for _ in range(count):
            data = {
                "book_title": self.fake.sentence().rstrip('.'),
                "author": self.fake.name(),
                "isbn": self.fake.isbn13(),
                "movie_title": self.fake.sentence().rstrip('.'),
                "director": self.fake.name(),
                "genre": self.fake.word()
            }
            media_data.append(data)
        return media_data

    def generate_weather_data(self, count):
        """Генерирует данные о погоде."""
        weather_data = []
        for _ in range(count):
            data = {
                "temperature": random.randint(-30, 40),
                "humidity": random.randint(0, 100),
                "wind_speed": random.uniform(0, 100),
                "condition": self.fake.word()
            }
            weather_data.append(data)
        return weather_data

    def generate_transport_data(self, count):
        """Генерирует данные о транспорте."""
        transport_data = []
        for _ in range(count):
            data = {
                "flight_number": self.fake.bothify(text='??####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
                "route": self.fake.city() + ' - ' + self.fake.city(),
                "status": random.choice(['On Time', 'Delayed', 'Cancelled']),
                "vehicle_type": random.choice(['Bus', 'Train', 'Plane', 'Ship'])
            }
            transport_data.append(data)
        return transport_data

    def generate_food_data(self, count):
        """Генерирует пищевые данные."""
        food_data = []
        for _ in range(count):
            data = {
                "recipe_name": self.fake.sentence().rstrip('.'),
                "ingredients": [self.fake.word() for _ in range(random.randint(3, 10))],
                "nutritional_value": random.randint(100, 500),
                "calories": random.randint(50, 1000)
            }
            food_data.append(data)
        return food_data


    def generate_names(self, count):
        """Генерирует список имен."""
        return [self.fake.name() for _ in range(count)]

    def generate_mac_addresses(self, count):
        """Генерирует список MAC-адресов."""
        return [self.fake.mac_address() for _ in range(count)]

    def generate_cars(self, count):
        """Генерирует список машин с некоторыми характеристиками."""
        return [{
            'make': self.fake.company(),
            'model': self.fake.word().capitalize(),
            'year': random.randint(1990, datetime.now().year)
        } for _ in range(count)]
