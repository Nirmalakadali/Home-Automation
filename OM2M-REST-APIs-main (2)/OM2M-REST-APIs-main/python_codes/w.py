# from urllib import response'
# import flask
# from flask import Flask, redirect, url_for, request, render_template

import requests
import matplotlib.pyplot as plt

# app = Flask(_name_)


# @app.route('/')
# def first():
#     return render_template('project.html')


# @app.route('project.html', methods=['GET'])
uri_cnt1 = "http://127.0.0.1:8080/~/in-cse/in-name/DHT11/Humidity?rcn=4"
uri_cnt2 = "http://127.0.0.1:8080/~/in-cse/in-name/DHT11/Temperature?rcn=4"
uri_cnt3 = "http://127.0.0.1:8080/~/in-cse/in-name/Ultrasonic-sensor/Distance?rcn=4"
uri_cnt4 = "http://127.0.0.1:8080/~/in-cse/in-name/WaterlevelSensor/Waterlevel?rcn=4"
header = {
    'X-M2M-Origin': 'admin:admin',
    'Content-type': 'application/json'
}
response = requests.get(uri_cnt1, headers=header)
data1 = response.json()
data1 = data1["m2m:cnt"]["m2m:cin"]

x1 = []
y1 = []

c = 0
for i in data1:
    if c >= 2:
        x1.append(int(c))
        y1.append(float(i["con"]))
        pass
    c = c + 1

response = requests.get(uri_cnt2, headers=header)
data2 = response.json()
data2 = data2["m2m:cnt"]["m2m:cin"]

x2 = []
y2 = []
c = 0
for i in data2:
    if c >= 2:
        x2.append(int(c))
        y2.append(float(i["con"]))
        pass
    c = c + 1

response = requests.get(uri_cnt3, headers=header)
data3 = response.json()
data3 = data3["m2m:cnt"]["m2m:cin"]

x3 = []
y3 = []

c = 0
for i in data1:
    if c >= 2:
        x3.append(int(c))
        y3.append(float(i["con"]))
    pass
    c = c + 1

response = requests.get(uri_cnt4, headers=header)
data4 = response.json()
data4 = data4["m2m:cnt"]["m2m:cin"]

x4 = []
y4 = []

c = 0
for i in data1:
    if c >= 2:
        x4.append(int(c))
        y4.append(float(i["con"]))
        pass
    c = c + 1

plt.plot(x1, y1)

plt.ylabel('Humidity')
plt.title('HUMIDITY')
plt.xlabel('Time')
plt.show()

plt.plot(x2, y2)

plt.ylabel('Temperature')
plt.title('TEMPERATURE')
plt.xlabel('Time')
plt.show()

plt.plot(x3, y3)

plt.ylabel('Distance')
plt.title('DISTANCE')
plt.xlabel('Time')
plt.show()

plt.plot(x4, y4)

plt.ylabel('Waterlevel')
plt.title('WATERLEVEL')
plt.xlabel('Time')
plt.show()
    # return render_template(('project.html', x1=x1, y1=y1, x2=x2, y2=y2, x3=x3, y3=y3, x4=x4, y4=y4))
    # app.run