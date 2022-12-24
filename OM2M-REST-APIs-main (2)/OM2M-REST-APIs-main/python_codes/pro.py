from oneM2M_functions import *

uri_cse = "http://127.0.0.1:8080/~/in-cse/in-name/"

ae1 = "Prana CO2"
cnt1 = "CO2"

create_ae(uri_cse, ae1)

uri_ae1 = uri_cse + ae1

create_cnt(uri_ae1, cnt1)
uri_cnt1 = uri_ae1 +"/"+ cnt1
create_data_cin(uri_cnt1, "random_value")

ae2 = "VOC"
cnt2 = "VOC"
cnt3 = "Temperature"
cnt4 = "Humidity"

create_ae(uri_cse,ae2)
uri_ae2 = uri_cse + ae2

create_cnt(uri_ae2, cnt2)
uri_cnt2 = uri_ae2 +"/"+ cnt2
create_data_cin(uri_cnt2, "random_value")

create_cnt(uri_ae2, cnt3)
uri_cnt3 = uri_ae2 +"/"+ cnt3
create_data_cin(uri_cnt3, "random_value")

create_cnt(uri_ae2, cnt4)
uri_cnt4 = uri_ae2 +"/"+ cnt4
create_data_cin(uri_cnt4, "random_value")

ae3 = "PM Sensor"
cnt5 = "PM 2.5"
cnt6 = "PM 10"

create_ae(uri_cse,ae3)
uri_ae3 = uri_cse + ae3

create_cnt(uri_ae3, cnt5)
uri_cnt5 = uri_ae3 +"/"+ cnt5
create_data_cin(uri_cnt5, "random_value")

create_cnt(uri_ae3, cnt6)
uri_cnt6 = uri_ae3 +"/"+ cnt6
create_data_cin(uri_cnt6, "random_value")



