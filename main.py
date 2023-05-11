import streamlit as st
from streamlit_option_menu import option_menu
import streamlit as st

from PIL import Image


#navigasi sidebar
with st.sidebar:
    selected = option_menu('Analisis Titrimetri & Kimia Organik',
    ['Homepage',
    'Latihan',
    'Pengolahan Data Titrimetri',
    'Analisa Data Kimia Organik'],
    default_index=0)

#Homepage
if (selected =='Homepage') :
     st.title(':blue[WELCOME!]')
     st.write('Ekke Rose M.,'
              'Kania Meilani,'
              'Lulu lutfihana A.,' 
              'Pandan Tsiqqa A.,'
              'Stephanny Aprillilova')
        
image = Image.open('Image 2023-05-10 at 20.25.25.jpg')
st.image(image, caption='labs')
     
    
    
      
     
        
#Latihan soal
Soal=st.selectbox(
    'pilih soal',
    ('Soal 1','Soal 2','Soal 3','Soal 4','Soal 5','Soal 6','Soal 7','Soal 8','Soal 9','Soal 10'))
    
if Soal == "Soal 1":
    st.write("titran pada standardisasi alkalimetri adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1 = st.button("HCL")
        opsi2 = st.button("KMNO4")
    with col2:
        opsi3 = st.button("AgNO3")
        opsi4 = st.button("NaOH")
    if opsi1:
        st.write("salah")
    elif opsi2:
          st.write("salah")
    elif opsi3:
          st.write("salah")
    elif opsi4:
          st.write("salah")
          st.balloons()
elif Soal == "Soal2":
    st.write("Indikator dalam standardisasi NaOH adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("SM")
        opsi2= st.button("MM")
    with col2:
        opsi3= st.button("PP")
        opsi4= st.button("BTB")
    if opsi1:
          st.write("salah")
    elif opsi2:
          st.write("salah")
    elif opsi3:
          st.write("salah")
          st.balloons()
    elif opsi4:
          st.write("salah")
elif Soal == "Soal 3":
    st.write("K2Cr2O7 digunakan sebagai baku primer dalam standarisasi...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("NA2S2O3 0,1N")
        opsi2= st.button("KMnO7 0,1N")
    with col2:
        opsi3= st.button("Na2B407,1N")
        opsi4= st.button("HCl 0,1N")
    if opsi1:
          st.write("benar")
          st.balloons()
    elif opsi2:
          st.write("salah")
    elif opsi3:
          st.write("salah")
    elif opsi4:
          st.write("salah")
            
elif Soal == "Soal 4":
    st.write("Mengapa pada titrasi permanganometri tidak digunakan indikator...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("karena penambahan H2SO4 sebagai pengganti indikator")
        opsi2= st.button("karena pemanasan yang dilakukan akan menyebabkan perubahan warna")
    with col2:
        opsi3= st.button("karena asam oksalat bersifat auto indikator")
        opsi4= st.button("karena KMnO4 bersifat auto indikator")
    if opsi1:
          st.write("salah")
    elif opsi2:
         st.write("salah")
    elif opsi3:
         st.write("salah")
    elif opsi4:
         st.write("salah")
         st.balloons()
        
elif Soal == "Soal 5":
    st.write("Trayek pH Fenolftalein adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("3,1 - 4,4")
        opsi2= st.button("6,0 - 7,6")
    with col2:
        opsi3= st.button("4,2 - 6,3")
        opsi4= st.button("8,2 - 10")
    if opsi1:
          st.write("salah")
    elif opsi2:
          st.write("salah")
    elif opsi3:
          st.write("salah")
    elif opsi4:
          st.write("salah")
          st.balloons()
        
elif Soal == "Soal 6":
    st.write("Alkil halida-alkil halida yang dapat digunakan untuk membuat 2-metil-3-siklobutilpentana dengan cara Corey-House adalah(alkil halida sesuai tahapannya)...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("1-bromo-1-siklobutilpropana dan 2-bromopropana")
        opsi2= st.button("Metilbromida dan 2-bromo-3-siklobutilpentana")
    with col2:
        opsi3= st.button("2-bromo-3-siklobutilpentana dan metilbromida")
        opsi4= st.button("2-bromopropana dan 1-bromo-1-siklopropilpropana")
    if opsi1:
          st.write("salah")
    elif opsi2:
          st.write("salah")
    elif opsi3:
          st.write("salah")
          st.balloons()
    elif opsi4:
          st.write("salah")
elif Soal == "Soal 7":
    st.write("Campuran reagen berikut yang menghasilkan reagen uji Tollens adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("AgNO3 + NaOH + NH4OH")
        opsi2= st.button("Etanol + Air + HCl")
    with col2:
        opsi3= st.button("CuSO4 + NaOH + NaK-Tartrat")
        opsi4= st.button("CuSO4 + Na2CO3")
    if opsi1:
          st.write("benar")
          st.balloons()
    elif opsi2:
          st.write("salah")
    elif opsi3:
          st.write("salah")
    elif opsi4:
          st.write("salah")
        
elif Soal == "Soal 8":
    st.write("Senyawa 3-metil-3-heksena direaksikan dengan asam bromida menghasilkan...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("3-bromo-4-metilheksana")
        opsi2= st.button("3-bromoheksana")
    with col2:
        opsi3= st.button("3-bromo-3-metilheksana")
        opsi4= st.button("4-bromo-3-metilheksanaa")
    if opsi1:
          st.write("salah")
    elif opsi2:
          st.write("salah")
    elif opsi3:
         st.write("benar")
         st.balloons()
    elif opsi4:
         st.write("salah")
        
elif Soal == "Soal 9":
    st.write("Hasil uji positif adldehid dan keton menggunakan pereaksi NaHSO3 adalah terbentuknya...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("Endapan merah bata")
        opsi2= st.button("Endapan putih")
    with col2:
        opsi3= st.button("Endapan cermin perak")
        opsi4= st.button("Endapan atau minyak kuning-kuning coklat")
    if opsi1:
          st.write("salah")
    elif opsi2:
          st.write("benar")
          st.balloons()
    elif opsi3:
          st.write("salah")
    elif opsi4:
          st.write("salah")
        
elif Soal == "Soal 10 ":
    st.write("10. Kenapa keton sulit dioksidasi?")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("karena pH 10")
        opsi2= st.button("karena tidak ada gugus hidrogennya")
    with col2:
        opsi3= st.button("karena sudah takdir")
        opsi4= st.button("Semuanya Benar")
    if opsi1:
        st.write("salah")
    elif opsi2:
        st.write("benar")
        st.balloons()
    elif opsi3:
        st.write("salah")
    elif opsi4:
        st.write("salah")
        
if (selected == 'Pengolahan Data Titrimetri'):
    bobot = st.number_input('Masukkan bobot sample')
    volume = st.number_input('Masukkan volume larutan yang di standarisasi')
    Beratekivalen = st.number_input('Masukkan berat ekivalen dalam sample')
    tombol=st.button('hitung normalitas')
    if tombol:
        nilai_normalitas=bobot/(volume*Beratekivalen)
        st.success(f'nilai normalitas adalah{nilai_normalitas}')
        
if (selected == 'Analisa Data Kimia Organik'):
    st.subheader('Uji Ceric Nitrat')
    option = st.selectbox(
    'Warna akhir'
    ('Tidak Terjadi Perubahan','merah ceri'))
