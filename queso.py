from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import chess

#driver = webdriver.Firefox(executable_path= r"C:\Users\maxpr\Downloads\geckodriver-v0.29.1-win64(1)\geckodriver.exe")
driver = webdriver.Firefox(executable_path="/home/famdjg/Descargas/geckodriver")
board = chess.Board()
#url = "https://lichess.org/2Se9AqUy"
url = input("Url: ")
driver.get(url)
i = 1
action = ActionChains(driver)
desplazamiento = 60


def mover():
    pieza_mover = input("Pieza a mover")
    piezas_bishop = driver.find_elements_by_xpath("//piece[@class = 'white bishop']")
    piezas_pawn = driver.find_elements_by_xpath("//piece[@class = 'white pawn']")
    piezas_rook_w = driver.find_elements_by_xpath("//piece[@class = 'white rook']")
    piezas_rook_b = driver.find_elements_by_xpath("//piece[@class = 'black rook']")
    piezas_knight = driver.find_elements_by_xpath("//piece[@class = 'white knight']")
    print(piezas_pawn[7].location)
    #print(piezas_pawn[1].location)
    #print(piezas_pawn[2].location)
    print(piezas_rook_w[0].location)
    print(piezas_rook_b[1].location)
    #print(piezas_pawn)
    driver.implicitly_wait(10)
    movimientos = []
    if pieza_mover == "peon":
        action.drag_and_drop_by_offset(piezas_pawn[0],0,-desplazamiento).perform()

mover()

while i == 1:
    elem = driver.find_elements_by_xpath("//l4x")
    driver.implicitly_wait(1)
    movimientos = []

    piezas_pawn = driver.find_elements_by_xpath("//piece[@class = 'white pawn']")
    pieza_ulti = driver.find_elements_by_xpath("//pieces[@class = 'last move']")

    numP = 0
    ubicacion_original = 0

    for numP in range(7):
        if piezas_pawn[numP].location == pieza_ulti[0].location:
            ubicacion_original = pieza_ulti[1].location
            break


    for value in elem:
        movimientos.append(value.text)
        print(value.text)