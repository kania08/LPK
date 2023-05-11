import streamlit as st
import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Homepage", "Latihan Soal", "Pengolahan Data Analisis Titrimetri", "Analisa Data Kimia Organik"])

with tab1:
   st.header("Homepage")
   st.title(':blue[WELCOME!]')
   st.write('1. Ekke Rose M.,'
            '2. Kania Meilani,'
            '3. Lulu lutfihana A.,' 
            '4. Pandan Tsiqqa A.,'
            '5. Stephanny Aprillilova')
   image = Image.open('Image 2023-05-10 at 20.25.25.jpg')
   st.image(image, caption='labs')
   if st.button('FILOSOFI TEMA'):
    st.write('tema kita yaitu LABERS yaitu seorang analisis kimia atau dalam bidang ahli kimia pastinya tidak asing dalam ruangan laboratorium dalam hal berbagai pengujian dan penelitian')
    

with tab2:
   st.header("Latihan Soal")
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
        st.write("SALAH!!")
    elif opsi2:
        st.write("SALAH!!") 
    elif opsi3:
        st.write("SALAH!!")
    elif opsi4:
        st.write("BENAR!!")
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
        st.write("SALAH!!")
    elif opsi2:
        st.write("SALAH!!")
    elif opsi3:
        st.write("BENAR!!")
        st.balloons()
    elif opsi4:
        st.write("SALAH!!")
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
          st.write("BENAR!!")
          st.balloons()
    elif opsi2:
          st.write("SALAH!!")
    elif opsi3:
          st.write("SALAH!!")
    elif opsi4:
          st.write("SALAH!!")     
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
          st.write("SALAH!!")
    elif opsi2:
        st.write("SALAH!!")
    elif opsi3:
        st.write("SALAH!!")
    elif opsi4:
        st.write("BENAR!!")
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
          st.write("SALAH!!")
    elif opsi2:
          st.write("SALAH!!")
    elif opsi3:
         st.write("SALAH!!")
    elif opsi4:
          st.write("BENAR!!")
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
         st.write("SALAH!!")
    elif opsi2:
          st.write("SALAH!!")
    elif opsi3:
          st.write("BENAR!!")
          st.balloons()
    elif opsi4:
          st.write("SALAH!!")
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
          st.write("BENAR!!")
          st.balloons()
    elif opsi2:
          st.write("SALAH!!")
    elif opsi3:
          st.write("SALAH!!")
    elif opsi4:
         st.write("SALAH!!")
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
          st.write("SALAH!!")
    elif opsi2:
          st.write("SALAH!!")
    elif opsi3:
         st.write("BENAR!!")
         st.balloons()
    elif opsi4:
         st.write("BENAR!!")
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
          st.write("SALAH!!")
    elif opsi2:
         st.write("BENAR!!")
         st.balloons()
    elif opsi3:
          st.write("SALAH!!")
    elif opsi4:
          st.write("SALAH!!")
elif Soal == "Soal 10":
    st.write("Kenapa keton sulit dioksidasi?")
    col1, col2 = st.columns (2)
    with col1:
        opsi1= st.button("karena pH 10")
        opsi2= st.button("karena tidak ada gugus hidrogennya")
    with col2:
        opsi3= st.button("karena sudah takdir")
        opsi4= st.button("Semuanya Benar")
    if opsi1:
        st.write("SALAH!!")
    elif opsi2:
        st.write("BENAR!!")
        st.balloons()
    elif opsi3:
        st.write("SALAH!!")
    elif opsi4:
        st.write("SALAH!!")
   
   

with tab3:
   st.header("Pengolahan Data Analisis Titrimetri")
if (selected == 'Pengolahan Data Titrimetri'):
    bobot = st.number_input('Masukkan bobot sample')
    volume = st.number_input('Masukkan volume larutan yang di standarisasi')
    Beratekivalen = st.number_input('Masukkan berat ekivalen dalam sample')
    tombol=st.button('hitung normalitas')
    if tombol:
        nilai_normalitas=bobot/(volume*Beratekivalen)
        st.success(f'nilai normalitas adalah{nilai_normalitas}')
   
with tab4:
        st.header("Analisa data kimia Organik")
        st.button("1-butanol","2-butanol","t-butilalkohol","heksana","formaldehida","aseton")
        st.button("uji ceric nitrat")

sampel = st.text_input('masukkan sampel')
ujisampel = st.text_input('masukkan uji sampel')
perubahanwarna = st.button('warna akhir sampel')
sampel == "1-butanol","2-butanol","t-butilalkohol"
    if perubahanwarna == "merah ceri":
        st.write("alkohol")
    sampel == "heksana","formaldehida","aseton"
    if perubahanwarna == "tidak terjadi perubahan warna":
        st.write("aldehida","keton")
        



        

        

        
    
    
     
    
   
