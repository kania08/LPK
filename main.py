import streamlit as st
from PIL import Image
import tkinter as tk
from tkinter import string var

tab1, tab2, tab3, tab4 = st.tabs(["Homepage", "Latihan Soal", "Pengolahan Data Analisis Titrimetri", "Analisa Data Kimia Organik"])

with tab1:
   st.title(':blue[WELCOME!]')
   st.write('1. Ekke Rose M.,'
            '2. Kania Meilani,'
            '3. Lulu lutfihana A.,' 
            '4. Pandan Tsiqqa A.,'
            '5. Stephanny Aprillilova')
   image = Image.open('Image 2023-05-10 at 20.25.25.jpg')
   st.image(image, caption='anak kimia')
   st.header('FILOSOFI TEMA')
   st.write('tema kita yaitu LABERS yaitu seorang analisis kimia atau dalam bidang ahli kimia pastinya tidak asing dalam ruangan laboratorium dalam hal berbagai pengujian dan penelitian')
    

with tab2:
root =tk.Tk()
root.geometry('500x500')

question = ['ya or no = ?','betul betul...','begitukah?','yuhu...']
options=[['s','b','c','y'],['a','b','c','d'],['1','2','3','hm'],['apa','iy','dik','ok']]

frame = tk.Frame(root, padx=10,pady=10,bg='#fff')
question_label= tk.Label(frame,height=5, width=28,font('Verdana',20),wraplength=500)

option1 = tk.Radiobutton(frame, bg='#fff',font('Verdana',20))   
option2 = tk.Radiobutton(frame, bg='#fff',font('Verdana',20))
option3 = tk.Radiobutton(frame, bg='#fff',font('Verdana',20))
option4 = tk.Radiobutton(frame, bg='#fff',font('Verdana',20))

button_next = tk.Button(frame, text='Next',font('Verdana',20))

frame.pack(fill='both',expand=true)
question_label.grid(row=0,column=0)

option1.grid(row=1, column=0)
option2.grid(row=2, column=0)
option3.grid(row=3, column=0)
option4.grid(row=4, column=0)

button_next.grid(row=1,column=0)

root.mainloop()


with tab3:
    bobot = st.number_input('Masukkan bobot sample')
    volume = st.number_input('Masukkan volume larutan yang di standarisasi')
    Beratekivalen = st.number_input('Masukkan berat ekivalen dalam sample')
    tombol=st.button('hitung normalitas')
    if tombol:
        nilai_normalitas=bobot/(volume*Beratekivalen)
        st.success(f'nilai normalitas adalah{nilai_normalitas}') 
      
      
with tab4:
        st.write("1-butanol","2-butanol","t-butilalkohol","heksana","formaldehida","aseton")
        st.write("uji ceric nitrat")

sampel = st.text_input('masukkan sampel')
ujisampel = st.text_input('masukkan uji sampel')
perubahanwarna = st.button('warna akhir sampel')

        



        

        

        
    
    
     
    
   
