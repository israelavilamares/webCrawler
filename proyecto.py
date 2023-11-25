
#crawler
from bs4 import BeautifulSoup
#autenticar
from requests.auth import HTTPBasicAuth
#autenticar2
#from selenium import webdriver

import requests 
import csv
from xlwt import Workbook
import pandas as pd
import re
#from openpyxl import Workbook


workbook = Workbook()       
table = workbook.add_sheet('this there are data')
table.write(0, 0, 'title')
table.write(0, 1, 'rating')
table.write(0, 2, 'director')
table.write(0, 3, 'creditos')
table.write(0, 4, 'comentario')
#table.write(0, 5, 'mejor Director')



url = "https://www.filmaffinity.com/mx/listtopmovies.php?list_id=400"
#basic = HTTPBasicAuth('221352209', 'ISRAEL2002')
#requests.get(url, auth=basic)
requests.get(url)
response = requests.get(url)

dato = response.content

soup = BeautifulSoup(dato,'html.parser')
#table= soup.find_all('div',attrs={'id':'data-movie-id'})
jobs = soup.find_all('div',{'class':'movie-card mc-flex movie-card-1'})

#dic = {}
line = 1
ratingNum = 7

contra = 0
for job in jobs:

    
    title = job.find('div',{'class':'mc-title'}).getText()
    rating = job.find('div',{'class':'mr-rating'}).getText()
    director = job.find('div',{'class':'mc-director'}).getText()
    credits = job.find('div',{'class':'credits'}).getText()
    
    #sustraer
    sustraer = rating 
    contra =  sustraer[0:2]
    #en consola
    print("titulo: " ,"1." + title,  "rating: ",rating,"Director: ",director,"creditos" ,credits)
    #verificar
    if(ratingNum > int(contra)):
    
       messsage = "esta es una buena pelicula "
    else:

        messsage = "esta es una mala pelicula °¬°"

    #url2 = "https://www.imdb.com/list/ls074047736/"
    #requests.get(url2)
    #response2 = requests.get(url2)
    #dato2 = response2.content
    #soup = BeautifulSoup(dato2,'html.parser')
    #jobs2 = soup.find_all('div',{'class':'lister-item mode-detail'})
    #line2 = 0
    #for job2 in jobs2:    
    #    Dictitle = job2.find('h3',{'class':'lister-item-header'}).getText()
    #    if(director == Dictitle):
    #        message2 = "es un Director conocido"
    #        break
    #    print(Dictitle)
    #line2 +=1


    #enviar a tabla
    table.write(line, 0, title) 
    table.write(line, 1,rating)
    table.write(line, 2,director)
    table.write(line, 3,credits)
    table.write(line, 4,messsage)
    #table.write(line, 5, message2)

    line +=1

workbook.save('pruebapelis.xls')






