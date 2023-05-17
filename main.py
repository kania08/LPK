import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image

#navigasi sidebar
with st.sidebar:
   selected = option_menu('Analisis Titrimetri & Kimia Organik',
                          ['Homepage',
                           'Latihan Soal',
                           'Pengolahan Data Analisis Titrimetri',
                           'Analisa Data Kimia Organik'],
                          default_index=0)
#homepage
if (selected =='Homepage') :
     st.title(':blue[WELCOME!]')
     st.write('EKKE ROSE M.,'
               'KANIA MEILANI,'
               'LULU LUTFIHANA A.,'
               'PANDAN TSIQQA A.,'
               'STEPHANNY APRILLILOVA')
     image = Image.open('Image 2023-05-10 at 20.25.25.jpg')
     st.image(image, caption='anak kimia')
     st.header('FILOSOFI TEMA')
     st.write('Tema dari website kami yaitu LABERS dimana tema kami mengusung seorang analisis kimia atau dalam bidang ahli kimia pastinya tidak asing dalam ruangan laboratorium dalam hal berbagai pengujian dan penelitian')
    

#Latihan
if (selected == 'Latihan Soal'):
   st.title('Latihan Soal')
   #soal pertama
   st.write('1. Titran pada standardisasi alkalimetri adalah...')
   col1, col2 = st.columns (2)
   with col1:
      opsi1 = st.button("HCL")
      opsi2 = st.button("KMNO4")
   with col2:
      opsi3 = st.button("AgNO3")
      opsi4 = st.button("NaOH")
   if opsi1:
      score=score+0
      st.write("SALAH!!")
      st.write('Kamu mendapat score', score)
   elif opsi2:
      score=score+0
      st.write("SALAH!!") 
      st.write('Kamu mendapat score', score)
   elif opsi3:
      score=score+0
      st.write("SALAH!!")
      st.write('Kamu mendapat score', score)
   elif opsi4:
      score=score+10
      st.write("BENAR!!")
      st.write('Kamu mendapat score', score)
      st.balloons()
   #soal kedua
   st.write("2. indikator dalam standardisasi NaOH adalah...")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("SM")
        opsi2= st.button("MM")
   with col2:
        opsi3= st.button("PP")
        opsi4= st.button("BTB")
   if opsi1:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi2:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi3:
        score=score+10
        st.write('BENAR!!')
        st.write('Kamu mendapat score', score)
        st.balloons()
   elif opsi4:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   #soal ketiga
   st.write("3. K2Cr2O7 digunakan sebagai baku primer dalam standarisasi...")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("NA2S2O3 0,1N")
        opsi2= st.button("KMnO7 0,1N")
   with col2:
        opsi3= st.button("Na2B407,1N")
        opsi4= st.button("HCl 0,1N")
   if opsi1:
        score+=10
        st.write("BENAR!!")
        st.write('Kamu mendapat score', score)
        st.balloons()
   elif opsi2:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi3:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi4:
        score=score+0
        st.write("SALAH!!")     
        st.write('Kamu mendapat score', score)
   #soal keempat
   st.write("4. Mengapa pada titrasi permanganometri tidak digunakan indikator...")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("karena penambahan H2SO4 sebagai pengganti indikator")
        opsi2= st.button("karena pemanasan yang dilakukan akan menyebabkan perubahan warna")
   with col2:
        opsi3= st.button("karena asam oksalat bersifat auto indikator")
        opsi4= st.button("karena KMnO4 bersifat auto indikator")
   if opsi1:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi2:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi3:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi4:
        score=score+10
        st.write("BENAR!!")
        st.write('Kamu mendapat score', score)
        st.balloons() 
   #soal kelima
   st.write("5. Trayek pH Fenolftalein adalah...")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("3,1 - 4,4")
        opsi2= st.button("6,0 - 7,6")
   with col2:
        opsi3= st.button("4,2 - 6,3")
        opsi4= st.button("8,2 - 10")
   if opsi1:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi2:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi3:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi4:
        score=score+10
        st.write("BENAR!!")
        st.write('Kamu mendapat score', score)
        st.balloons()
   #soal keenam
   st.write("6. Alkil halida-alkil halida yang dapat digunakan untuk membuat 2-metil-3-siklobutilpentana dengan cara Corey-House adalah(alkil halida sesuai tahapannya)...")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("1-bromo-1-siklobutilpropana dan 2-bromopropana")
        opsi2= st.button("Metilbromida dan 2-bromo-3-siklobutilpentana")
   with col2:
        opsi3= st.button("2-bromo-3-siklobutilpentana dan metilbromida")
        opsi4= st.button("2-bromopropana dan 1-bromo-1-siklopropilpropana")
   if opsi1:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi2:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi3:
        score=score+10
        st.write("BENAR!!")
        st.write('Kamu mendapat score', score)
        st.balloons()
   elif opsi4:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   #soal ketujuh
   st.write("7. Campuran reagen berikut yang menghasilkan reagen uji Tollens adalah...")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("AgNO3 + NaOH + NH4OH")
        opsi2= st.button("Etanol + Air + HCl")
   with col2:
        opsi3= st.button("CuSO4 + NaOH + NaK-Tartrat")
        opsi4= st.button("CuSO4 + Na2CO3")
   if opsi1:
          score=score+10
          st.write("BENAR!!")
          st.write('Kamu mendapat score', score)
          st.balloons()
   elif opsi2:
          score=score+0
          st.write('Kamu mendapat score', score)
          st.write("SALAH!!")
   elif opsi3:
          score=score+0
          st.write("SALAH!!")
          st.write('Kamu mendapat score', score)
   elif opsi4:
         score=score+0
         st.write("SALAH!!")
         st.write('Kamu mendapat score', score)
   #soal kedelapan
   st.write("8. Pemanasan 3-pentanol pada suhu 250oC dengan adanya katalis Al2O3 akan menghasilkan..")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button('3,3-dipentoksipentana')
        opsi2= st.button('3-pentoksipentana')
   with col2:
        opsi3= st.button('3,3-dipentoksi eter')
        opsi4= st.button('3-pentoksi-3-pentana')
   if opsi1:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi2:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi3:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi4:
        score=score+10
        st.write("BENAR!!")
        st.write('Kamu mendapat score', score)
        st.balloons()
   #soal kesembilan
   st.write("9. Hasil uji positif adldehid dan keton menggunakan pereaksi NaHSO3 adalah terbentuknya...")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("Endapan merah bata")
        opsi2= st.button("Endapan putih")
   with col2:
        opsi3= st.button("Endapan cermin perak")
        opsi4= st.button("Endapan atau minyak kuning-kuning coklat")
   if opsi1:
         score=score+0
         st.write("SALAH!!")
         st.write('Kamu mendapat score', score)
   elif opsi2:
         score=score+10
         st.write("BENAR!!")
         st.write('Kamu mendapat score', score)
         st.balloons()
   elif opsi3:
         score=score+0
         st.write("SALAH!!")
         st.write('Kamu mendapat score', score)
   elif opsi4:
         score=score+0
         st.write("salah!!")
         st.write('Kamu mendapat score', score)
   #soal kesepuluh
   st.write("10. Kenapa keton sulit dioksidasi?")
   col1, col2 = st.columns (2)
   with col1:
        opsi1= st.button("karena pH 10")
        opsi2= st.button("karena tidak ada gugus hidrogennya")
   with col2:
        opsi3= st.button("karena sudah takdir")
        opsi4= st.button("Semuanya Benar")
   if opsi1:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi2:
        score=score+10
        st.write("BENAR!!")
        st.write('Kamu mendapat score', score)
        st.balloons()
   elif opsi3:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
   elif opsi4:
        score=score+0
        st.write("SALAH!!")
        st.write('Kamu mendapat score', score)
if (selected == 'Pengolahan Data Analisis Titrimetri'):
   bobot = st.number_input('Masukkan bobot sample',
                           format='%.4f')
   volume = st.number_input('Masukkan volume larutan yang di standarisasi')
   Beratekivalen = st.number_input('Masukkan berat ekivalen dalam sample')
   tombol=st.button('hitung normalitas')
   if tombol:
        nilainormalitas=bobot/(volume*Beratekivalen)
        rounded_nilainormalitas=round(nilainormalitas,4)
        st.success(f'nilai normalitas adalah{nilai_normalitas}')
       
if (selected == 'Analisa Data Kimia Organik'):
   st.header('Uji Ceric Nitrat')
   sample=st.text_input('Masukkan saample yang digunakan')
   st.write('Silahkan Klik Button Di Bawah Sesuai dengan warna akhir yang didapat')
   tombol1=st.button('Merah ceri')
   if tombol1:
      st.write('senyawa yang mengandung gugus hidroksil')
   tombol2=st.button('Tidak berwarna')
   if tombol2:
      st.write('senyawa yang tidak mengandung gugus hidroksil')
      
      
      


        



        

        

        
    
    
     
    
   
