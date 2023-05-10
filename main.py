import streamlit as st
from streamlit_option_menu import option_menu

#navigasi sidebar
with st.sidebar:
    selected = option_menu('Materi & Latihan',
    ['Homepage',
    'Latihan',
    'Pengolahan Data Titrimetri',
    'Analisa Data Kimia Organik'],
    default_index=0)

#Homepage
if (selected == 'Homepage') :
     st.title(':blue[WELCOME TO OUR WEBS]')
     
     st.header('KELOMPOK 3')
     st.write('1.Ekke Rose M.,'
              ,'2.Kania Meilani,'
              ,'3.Lulu lutfihana A.,' 
              ,'4.Pandan Tsiqqa A.,'
              ,'5.Stephanny Aprillilova')
     
     txt = st.text_area('Website','''
     Website ini merupakan situs yang berisi materi dan latihan analisis titrimetri dan kimia organik yang dapat mempermudah kegiatan
     pembelajaran serta sebagai sarana latihan untuk mengasah kemampuan dalam materi tersebut.
     ''')
        
#Latihan
if (selected == 'Latihan') :
    st.title('Latihan Soal')
    #soal pertama
    st.write("1. Titran pada standardisasi alkalimetri adalah...")
    col1, col2 = st.columns (2)
    with col1:
        opsi1 = st.button("HCL")
        opsi2 = st.button("KMNO4")
    with col2:
        opsi3 = st.button("AgNO3")
        opsi4 = st.button("NaOH")
    if opsi1:
        st.write("Salah")
    elif opsi2:
        st.write("Salah")
    elif opsi3:
        st.write("salah")
    elif opsi4:
        st.write ("Benar")
        st.balloons()

    #soal kedua
    st.write("2. Indikator dalam standardisasi NaOH adalah...")
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
        st.write("benar")
        st.balloons()
    elif opsi4:
        st.write("salah")
        
    #Soal ketiga
    st.write("3. K2Cr2O7 digunakan sebagai baku primer dalam standarisasi...")
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
        
    #Soal keempat
    st.write("4. Mengapa pada titrasi permanganometri tidak digunakan indikator...")
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
        st.write("benar")
        st.balloons()
        
    #Soal kelima
    st.write("5.Trayek pH Fenolftalein adalah...")
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
        st.write("benar")
        st.balloons()
        
    #Soal keenam
    st.write("6. Alkil halida-alkil halida yang dapat digunakan untuk membuat 2-metil-3-siklobutilpentana dengan cara Corey-House adalah(alkil halida sesuai tahapannya)...")
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
        st.write("benar")
        st.balloons()
    elif opsi4:
        st.write("salah") 
        
    #Soal ketujuh
    st.write("7. Campuran reagen berikut yang menghasilkan reagen uji Tollens adalah...")
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
        

    #Soal kedelapan
    st.write("8. Senyawa 3-metil-3-heksena direaksikan dengan asam bromida menghasilkan...")
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
        
    #Soal kesembilan
    st.write("9. Hasil uji positif adldehid dan keton menggunakan pereaksi NaHSO3 adalah terbentuknya...")
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
        
    #Soal kesepuluh
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
    st.subheader ('KODE WARNA')
    st.write('0=tidak terjadi perubahan')
    st.write('1=merah muda')
    st.write('2=ungu')
    st.write('3=endapan kuning')
    st.write('4=endapan merah bata')
    st.write('5=endapan cermin perak')
    st.write('6=hijau')
    st.write('7=coklat')
    
    st.subheader('Uji iodoform')
    perubahan1 = st.number_input('Masukkan warna akhir (ketik dengan huruf kecil)')
    if perubahan1==3:
        st.write('alkohol sekunder')
    elif perubahan1==1:
        st.write('alkohol primer atau alkohol tersier')
        
    st.subheader('Uji schiff')
    perubahan2 = st.number_input('Masukkan warna akhir (ketik dengan huruf kecil)')
    if perubahan2==2:
        st.write('formaldehida')
    elif perubahan2==1:
        st.write('aseton')
    st.subheader('Uji jones')
    perubahan3 = st.number_input('Masukkan warna akhir (ketik dengan huruf kecil)')
    if perubahan3==6:
        st.write('alkohol primer atau alkohol sekunder')
    elif perubahan3==7:
        st.write('alkohol tersier')
    st.subheader('Uji fehling')
    perubahan4 = st.number_input('Masukkan warna akhir (ketik dengan huruf kecil)')
    if perubahan4==4:
        st.write('aldehida')
    elif perubahan4==1:
        st.write('keton')
    st.subheader('Uji tollens')
    perubahan5 = st.number_input('Masukkan warna akhir (ketik dengan huruf kecil)')
    if perubahan5==5:
        st.write('aldehida')
    elif perubahan5==0:
        st.write('keton')
