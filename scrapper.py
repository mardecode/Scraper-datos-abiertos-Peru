# importando
from ast import arg
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("driver", help="path de chrome driver")
parser.add_argument("--contenido", help="ejem Dataset")
parser.add_argument("--categoria", help="ejem Economía y Finanzas")
parser.add_argument("--formato", help="ejem csv")
parser.add_argument("--reporte", help="ejem Donaciones")

args = parser.parse_args()

if args.contenido:
    tipo_contenido = args.contenido
else:
    tipo_contenido = 'Dataset'

if args.categoria:
    tipo_categoria = args.categoria
else:
    tipo_categoria = 'Economía y Finanzas'

if args.formato:
    tipo_formato = args.formato
else:
    tipo_formato = 'csv'

if args.reporte:
    consulta_buscador = args.reporte
else:
    consulta_buscador = 'Donaciones'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# driver_path = '/home/margarcuae/Descargas/chromedriver'
driver = webdriver.Chrome(args.driver, chrome_options=options)

consulta_contenido = '//a[@class="facetapi-inactive" and contains (text(), "' + \
    tipo_contenido + '" )]'
consulta_categoria = '//a[@class="facetapi-inactive" and contains (text(), "' + \
    tipo_categoria + '" )]'
consulta_formato = '//a[@class="facetapi-inactive" and contains (text(), "' + \
    tipo_formato + '" )]'

driver.get('https://www.datosabiertos.gob.pe/')
# click contenido
WebDriverWait(
    driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, consulta_contenido))).click()

# click categoria
WebDriverWait(
    driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, consulta_categoria))).click()

# despliega dropdown de tipos de datos
WebDriverWait(
    driver,
    5).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             '//*[@id="main"]/div/section/div/div/div/div/div[1]/div/div[4]/h2'))).click()

# click formato
WebDriverWait(
    driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, consulta_formato))).click()

# escribir consulta
WebDriverWait(
    driver, 5).until(
        EC.element_to_be_clickable(
            (By.ID, 'edit-query'))).send_keys(consulta_buscador)

# click en el boton buscar
WebDriverWait(
    driver, 5).until(
        EC.element_to_be_clickable(
            (By.ID, 'edit-submit-dkan-datasets'))).click()
# click en el primer resultado de la búsqueda
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.XPATH, '//h2[@class="node-title"][1]/a'))).click()

# busca el primer elemento que contenga la palabra data y lo descarga
WebDriverWait(
    driver,
    5).until(
        EC.element_to_be_clickable(
            (By.XPATH,
             '//ul[@class="resource-list"]/li/div/a[contains (text(),"Data")][1]//parent::*/span/a'))).click()