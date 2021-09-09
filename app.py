from flask import request
from flask_restful import Resource,Api
from flask import Flask
from typing import Dict
from flask import Flask
import random


def create_app(config_dict: Dict = {}):
    app = Flask(__name__)    
    return app

class VistaCita(Resource):
    def post(self, id_cita):       
        data={
            "id" : id_cita,
            "entidadTratante" : request.json["entidadTratante"],
            "usuarioTratante" : request.json["usuarioTratante"],
            "usuarioTomador" : request.json["usuarioTomador"],
            "servicioOfertado" : request.json["servicioOfertado"],
            "fechaDesde" : request.json["fechaDesde"],
            "fechaHasta" : request.json["fechaHasta"] 
        }
        return data

    def get(self, id_cita):
        data={
            "id" : id_cita,
            "entidadTratante" : random.randint(100, 999),
            "usuarioTratante" : random.randint(100, 999),
            "usuarioTomador" : random.randint(100, 999),
            "servicioOfertado" : random.randint(100, 999),
            "fechaDesde" : "10-10-2021 08:00",
            "fechaHasta" : "10-10-2021 08:30" 
        }
        return data

class HealthCheck(Resource):    

    def get(self):
        data={
            "echo" : "ok"
        }
        return data



app = create_app()
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaCita, "/cita/<int:id_cita>")
api.add_resource(HealthCheck, "/cita/healtchek")


if __name__ == '__main__':
    app.run()