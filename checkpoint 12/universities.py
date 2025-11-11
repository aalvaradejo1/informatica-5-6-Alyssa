import requests

universities = {
    "EAC" : {"Majors" : "","Cost" : 7750,"Distance" : 428, "Official name" : "Eastern Arizona College"},
    "Tec Milenio" : {"Majors" : "","Cost" : 7750,"Distance" : 428, "Official name" : "Universidad Tecmilenio"},
    "BYU-Pathway" : {"Majors" : 4,"Cost" : 7750,"Distance" : 428, "Official name" : ""},
    "UACJ" : {"Majors" : "","Cost" : 7750,"Distance" : 428, "Official name" : "Universidad Autonoma de Ciudad Juarez"},
    "Tec de Monterrey" : {"Majors" : "","Cost" : 7750,"Distance" : 428, "Official name" : "Tecnologico de Monterrey"}
}

name = input("Type the name of a university: ")
response = requests.get("http://universities.hipolabs.com/search?country=mexico")