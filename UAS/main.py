
from http import HTTPStatus
from flask import Flask, request, abort
from flask_restful import Resource, Api 
from models import Buah as JenisBuah
from engine import engine
from sqlalchemy import select
from sqlalchemy.orm import Session

session = Session(engine)

app = Flask(__name__)
api = Api(app)        

class BaseMethod():

    def __init__(self):
        self.raw_weight = {'Kualitas_Buah': 10, 'Harga': 5, 'Pelayanan': 5, 'Suasana': 5, 'Jarak': 5}

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k, v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(JenisBuah.No, JenisBuah.Nama_Toko, JenisBuah.Kualitas_Buah, JenisBuah.Harga, JenisBuah.Pelayanan, JenisBuah.Suasana, JenisBuah.Jarak)
        result = session.execute(query).fetchall()
        print(result)
        return [{'No': tokobuahterbaik.No, 'Nama_Toko': tokobuahterbaik.Nama_Toko, 'Kualitas_Buah': tokobuahterbaik.Kualitas_Buah, 'Harga': tokobuahterbaik.Harga, 'Pelayanan': tokobuahterbaik.Pelayanan, 'Suasana': tokobuahterbaik.Suasana, 'Jarak': tokobuahterbaik.Jarak} for tokobuahterbaik in result]

    @property
    def normalized_data(self):
        Kualitas_Buah_values = []
        Harga_values = []
        Pelayanan_values = []
        Suasana_values = []
        Jarak_values = []

        for data in self.data:
            Kualitas_Buah_values.append(data['Kualitas_Buah'])
            Harga_values.append(data['Harga'])
            Pelayanan_values.append(data['Pelayanan'])
            Suasana_values.append(data['Suasana'])
            Jarak_values.append(data['Jarak'])

        return [
            {'No': data['No'],
             'Nama_Toko': data['Nama_Toko'],
             'Kualitas_Buah': data['Kualitas_Buah'] / max(Kualitas_Buah_values),
             'Harga': min(Harga_values) / data['Harga'],
             'Pelayanan': data['Pelayanan'] / max(Pelayanan_values),
             'Suasana': data['Suasana'] / max(Suasana_values),
             'Jarak': data['Jarak'] / max(Jarak_values)
             }
            for data in self.data
        ]

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class WeightedProductCalculator(BaseMethod):
    def update_weights(self, new_weights):
        self.raw_weight = new_weights

    @property
    def calculate(self):
        normalized_data = self.normalized_data
        produk = []

        for row in normalized_data:
            product_score = (
                row['Kualitas_Buah'] ** self.raw_weight['Kualitas_Buah'] *
                row['Harga'] ** self.raw_weight['Harga'] *
                row['Pelayanan'] ** self.raw_weight['Pelayanan'] *
                row['Suasana'] ** self.raw_weight['Suasana'] *
                row['Jarak'] ** self.raw_weight['Jarak']
            )

            produk.append({
                'No': row['No'],
                'produk': product_score
            })

        sorted_produk = sorted(produk, key=lambda x: x['produk'], reverse=True)

        sorted_data = []

        for product in sorted_produk:
            sorted_data.append({
                'No': product['No'],
                'score': product['produk']
            })

        return sorted_data


class WeightedProduct(Resource):
    def get(self):
        calculator = WeightedProductCalculator()
        result = calculator.calculate
        return result, HTTPStatus.OK.value
    
    def post(self):
        new_weights = request.get_json()
        calculator = WeightedProductCalculator()
        calculator.update_weights(new_weights)
        result = calculator.calculate
        return {'data': result}, HTTPStatus.OK.value
    

class SimpleAdditiveWeightingCalculator(BaseMethod):
    @property
    def calculate(self):
        weight = self.weight
        result = {row['No']:
                  round(row['Kualitas_Buah'] * weight['Kualitas_Buah'] +
                        row['Harga'] * weight['Harga'] +
                        row['Pelayanan'] * weight['Pelayanan'] +
                        row['Suasana'] * weight['Suasana'] +
                        row['Jarak'] * weight['Jarak'], 2)
                  for row in self.normalized_data
                  }
        sorted_result = dict(
            sorted(result.items(), key=lambda x: x[1], reverse=True))
        return sorted_result

    def update_weights(self, new_weights):
        self.raw_weight = new_weights

class SimpleAdditiveWeighting(Resource):
    def get(self):
        saw = SimpleAdditiveWeightingCalculator()
        result = saw.calculate
        return result, HTTPStatus.OK.value

    def post(self):
        new_weights = request.get_json()
        saw = SimpleAdditiveWeightingCalculator()
        saw.update_weights(new_weights)
        result = saw.calculate
        return {'data': result}, HTTPStatus.OK.value


class Buah(Resource):
    def get_paginated_result(self, url, list, args):
        page_size = int(args.get('page_size', 10))
        page = int(args.get('page', 1))
        page_count = int((len(list) + page_size - 1) / page_size)
        start = (page - 1) * page_size
        end = min(start + page_size, len(list))

        if page < page_count:
            next_page = f'{url}?page={page+1}&page_size={page_size}'
        else:
            next_page = None
        if page > 1:
            prev_page = f'{url}?page={page-1}&page_size={page_size}'
        else:
            prev_page = None
        
        if page > page_count or page < 1:
            abort(404, description=f'Halaman {page} tidak ditemukan.') 
        return {
            'page': page, 
            'page_size': page_size,
            'next': next_page, 
            'prev': prev_page,
            'Results': list[start:end]
        }

    def get(self):
        query = select(JenisBuah)
        data = [{'No': tokobuahterbaik.No, 'Nama_Toko': tokobuahterbaik.Nama_Toko, 'Harga': tokobuahterbaik.Harga, 'Pelayanan': tokobuahterbaik.Pelayanan, 'Suasana': tokobuahterbaik.Suasana, 'Jarak': tokobuahterbaik.Jarak} for tokobuahterbaik in session.scalars(query)]
        return self.get_paginated_result('tokobuahterbaik/', data, request.args), HTTPStatus.OK.value


api.add_resource(Buah, '/tokobuahterbaik')
api.add_resource(WeightedProduct, '/wp')
api.add_resource(SimpleAdditiveWeighting, '/saw')

if __name__ == '__main__':
    app.run(port='5005', debug=True)
