import functions.define as define
import functions.print as pr
import functions.aesthetic as text
from functions.aesthetic import TAz, TRo, FAz, SRe

font_2 = 'mini'

def search_data(num):
    search_id, search_by = 0,0
    while True:
        if num == 1:
            text.subtittle("R A R E Z A")
            print(FAz + "Ingrese el tipo de rareza a buscar:" + SRe + "\n")
            print(TRo + "1. " + TAz + "Común.")
            print(TRo + "2. " + TAz + "Poco Común.")
            print(TRo + "3. " + TAz + "Rara.")
            print(TRo + "4. " + TAz + "Mítica.")
            print(TRo + "5. " + TAz + "Menú Anterior.")
            print(SRe)
            n = input()
                  
            if not pr.siEntradaValida(n):
                pr.inputNoValido()
            else:
              n = int(n)
              search_id = "Rareza"
              if n < 5: 
                search_by = define.rarity(n)
                break
              elif n == 5: break
              else:
                pr.inputNoValido()
                        
        elif num == 2:
            text.subtittle("C O L O R")
            print(FAz + "Ingrese el tipo de color a buscar:" + SRe + "\n")
            print(TRo + "1. " + TAz + "Azul.")
            print(TRo + "2. " + TAz + "Rojo.")
            print(TRo + "3. " + TAz + "Blanco.")
            print(TRo + "4. " + TAz + "Negro.")
            print(TRo + "5. " + TAz + "Verde.")
            print(TRo + "6. " + TAz + "Menú Anterior.")
            print(SRe)
            n = input()
                  
            if not pr.siEntradaValida(n):
                pr.inputNoValido()
            else:
              n = int(n)
              search_id = "Color"
              if n < 6: 
                search_by = define.color(n)
                break
              elif n == 6: break
              else: pr.inputNoValido()
              if n<6: break
    
        elif num == 3:
            text.subtittle("T I P O")
            print(FAz + "Ingrese el tipo de carta a buscar:" + SRe + "\n")
            print(TRo + "1. " + TAz + "Tierra.")
            print(TRo + "2. " + TAz + "Encantamiento.")
            print(TRo + "3. " + TAz + "Instantáneo.")
            print(TRo + "4. " + TAz + "Artefacto.")
            print(TRo + "5. " + TAz + "Criatura.")
            print(TRo + "6. " + TAz + "Conjuro.")
            print(TRo + "7. " + TAz + "Planeswalker.")
            print(TRo + "8. " + TAz + "Menú Anterior.")
            print(SRe)
            n = input()
              
            if not pr.siEntradaValida(n):
                pr.inputNoValido()
            else:
              n = int(n)
              search_id = "Tipo"
              if n < 8:
                  search_by = define.tipe(n)
                  break
              elif n == 8: break
              else: pr.inputNoValido()

    return search_id, search_by