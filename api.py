from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from random import randint
import requests
def hello_world(request):
    
    return Response("test")

def nb_aleatoire(request):
    params = request.params
    if not bool(params):
        return Response(f'la valeur aleatoire est : {randint(0,100)}')
    else:
        try:
            params = dict(params)
            nb = int(params["nb"])
            return dict(tableau = list(randint(-1000,1000) for i in range(nb)))
        except:
           return Response("veuilez inserer le bon paramètre") 

def addition(request):
    pramas = request.params
    try:
        n1,n2 = request.params["n1"],request.params["n2"]
        return Response(f" Le résultat de la somme {n1} + {n2} = {int(n1) + int(n2)}") 
    except:
        return Response("veuilez inserer le bon paramètre") 
              
def produit(request):
    pramas = request.params
    try:
        n1,n2 = request.params["n1"],request.params["n2"]
        return Response(f"<p>Le résultat du produit de {n1} x {n2} = {int(n1)* int(n2)}</p>") 
    except:
        return Response("veuilez inserer le bon paramètre") 
    
def get_img(request):
    params = request.params
    try:
        num = params["num"]
        url = f"https://www.juleshaag.fr/devIA/devAPI/{num}.png"
        response = requests.get(url)
        return Response(body=response.content,status=200,content_type="image/png")
    except:
        return Response("veuilez inserer le bon paramètre")
        
def get_station(request):
    try:
        params = request.params
        id = params["id"]
        url = f'https://www.juleshaag.fr/devIA/devAPI/station_information.json'
        response = requests.get(url)
        stations = response.json()["data"]["stations"]
        
        if "addr" in params.keys():
            station = next(station for station in stations if station["station_id"] == id)
            return Response(station["address"])        
        elif "cap" in params.keys():  
            if id == "toutes":
                print("cap")            
                # print(sum(list(station["capacity"] for station in stations)))
                return Response(f'''la somme total est : 
                            {sum(list(station["capacity"] for station in stations))}''')    
            else:
                station = next(station for station in stations if station["station_id"] == id)
                return dict(capacity = station["capacity"])
        
        
        else:
            return next(station for station in stations if station["station_id"] == id)
    except:
        return Response("veuilez inserer le bon paramètre")

def get_address(request):
    url = f'https://www.juleshaag.fr/devIA/devAPI/station_information.json'
    n = request.matchdict["n"]
    response = requests.get(url)
    stations = response.json()["data"]["stations"]
    station = next(station for station in stations if station["station_id"] == n)
    return Response(station["address"])

def get_cap(request):
    url = f'https://www.juleshaag.fr/devIA/devAPI/station_information.json'
    response = requests.get(url)
    stations = response.json()["data"]["stations"]
    n = request.matchdict["n"]
    if n == "toutes":        
        capacity = dict((station["station_id"],station["capacity"]) for station in stations)
        capacity.__setitem__("capacity Total" ,sum(list(station["capacity"] for station in stations)))
        return capacity
    else:        
        station = next(station for station in stations if station["station_id"] == n)
        return dict(capacity = station["capacity"])



if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        config.add_route('val','/val')
        config.add_view(nb_aleatoire,route_name='val',renderer='json')
        config.add_route('addition','/calc/add')
        config.add_view(addition,route_name='addition')
        config.add_route('produit','/calc/prod')
        config.add_view(produit,route_name='produit')
        config.add_route("image","/img")
        config.add_view(get_img,route_name="image")
        config.add_route('station_velo','/stations_velo')
        config.add_view(get_station,route_name="station_velo",renderer="json")
        config.add_route('get_address','/stations_velo/{n}/addr')
        config.add_view(get_address,route_name='get_address')
        config.add_route("get_cap","/stations_velo/{n}/cap")
        config.add_view(get_cap,route_name="get_cap",renderer="json")
        app = config.make_wsgi_app()

    serve(app, host='127.0.0.1', port=8000)