import streamlit as st
import easyocr
from PIL import Image
import re
import sqlite3 
import pandas as pd

st.write('<h1 style="color: orange;">BUSINESS CARD DATA EXTRACTION</h1>',unsafe_allow_html=True)
st.write('<h4 style="color: green;">SELECT A PAGE YOU WANT TO  VIEW</h4>',unsafe_allow_html=True)
current_page = st.selectbox("Selection", ["Home", "Extract & Upload", "Data Modification"])

# Define the content for each "page"
def page_1():
    st.write('<h5 style="color: brown;">YOU CAN COPY THE LINK OF THE IMAGE TO EXTRACT THE DATA</h5>',unsafe_allow_html=True)
    image_url = "/content/1.png"
    st.image(image_url, use_column_width=True)
    st.write('<h5 style="color: blue;">LINK:/content/1.png</h5>',unsafe_allow_html=True)

    image_url = "/content/2.png"
    st.image(image_url, use_column_width=True)
    st.write('<h5 style="color: black;">LINK:/content/2.png</h5>',unsafe_allow_html=True)

    image_url = "/content/3.png"
    st.image(image_url, use_column_width=True)
    st.write('<h5 style="color: green;">LINK:/content/3.png</h5>',unsafe_allow_html=True)

    image_url = "/content/4.png"
    st.image(image_url, use_column_width=True)
    st.write('<h5 style="color: red;">LINK:/content/4.png</h5>',unsafe_allow_html=True)

    image_url = "/content/5.png"
    st.image(image_url, use_column_width=True)
    st.write('<h5 style="color: orange;">LINK:/content/5.png</h5>',unsafe_allow_html=True)

    

def page_2():
    
    def img_to_binary(file):
        with open(file, 'rb') as file:
            binaryData = file.read()
            return binaryData
    def doit(res):
        data = {"company_name" : [],
                "card_holder" : [],
                "designation" : [],
                "mobile_number" :[],
                "email" : [],
                "website" : [],
                "area" : [],
                "city" : [],
                "state" : [],
                "pin_code" : [],
                "image" : img_to_binary(user_input)
               }

        for i,l in enumerate(res):
            #to get company name
            if (i>4 and l.isalpha()) or (i==7 and re.match(r'^[a-zA-Z ]+$',l)) :
                data["company_name"].append(l)
                if len(data["company_name"]) ==2:
                    my_list = data["company_name"]
                    joined_result = " ".join(my_list)
                    data["company_name"]=joined_result
                
                    
        
            
        #to get name
            elif i==0:
                data["card_holder"]=res[0]
        #to get designation
            elif i==1:
                data["designation"]=res[1]

        #to get mobile number
            elif "-" in l:
                data["mobile_number"].append(l)
                if len(data["mobile_number"])==2:
                    my_list = data["mobile_number"]
                    joined_result = " & ".join(my_list)
                    data["mobile_number"]=joined_result
                

        #to get website name
            elif "www " in l.lower() or "www." in l.lower():
                data["website"]=l
            elif l=="WWW":
                data["website"]=res[4] +"." + res[5]
        #to get mailid
            elif "@" in l:
                data["email"]=l
            elif re.match(r'^\d+ \w+',l):
                if "," in l:
                    substrings = l.split(',')
                    first_element = substrings[0]
                    data["area"]=first_element
                if "," not in l:
                    data["area"]=l
        #to get city
            match1 = re.findall('.+St , ([a-zA-Z]+).+', l)
            match2 = re.findall('.+St,, ([a-zA-Z]+).+', l)
            match3 = re.findall('^[E].+',l)
            if match1:
                data["city"]=match1[0]
            
            elif match2:
                data["city"]=match2[0]
            
            elif match3:
                data["city"]=match3[0]
            
        
        #to get state name
            state_match = re.findall('[a-zA-Z]{9} +[0-9]',l)
            if state_match:
                data["state"]=l[:9]
            elif re.findall('^[0-9].+, ([a-zA-Z]+);',l):
                data["state"]=l.split()[-1]
            if len(data["state"])== 2:
                data["state"].pop(0)

        #to get pincode
            if len(l)>=6 and l.isdigit():
                data["pin_code"]=l
            elif re.findall('[a-zA-Z]{9} +[0-9]',l):
                data["pin_code"]=l[10:]
        string_data={}
        for key, value in data.items():
            if isinstance(value, list):
                string_data[key]=' '.join([str(item) for item in value])
            else:    
                string_data[key] = value
        st.write(string_data)
        return string_data
    st.write('<h4 style="color: red;">FOR DATA EXTRACTION GIVE THE LINK PRESS ENTER</h4>',unsafe_allow_html=True)
    user_input = st.text_input("Give the link of the image for extraction")
    
    if user_input:
        reader = easyocr.Reader(['en'])
        result = reader.readtext(user_input, detail=0, paragraph=False)
        z=doit(result)
        res=[]
        t= tuple(z.values())
        for i in t:
            if isinstance(i,list):
                for c in i:
                    res.append(c)
            else:
                res.append(i)
        values = tuple(res)
        sqlite_db_file ="/content/bizD.db"
        sqlite_conn = sqlite3.connect(sqlite_db_file)
        sqlite_cursor = sqlite_conn.cursor()
        bizz_table = '''CREATE TABLE IF NOT EXISTS biz1_details(
                company_name TEXT ,
                card_holder TEXT,
                designation TEXT,
                mobile_number TEXT,
                email TEXT PRIMARY KEY,
                website TEXT,
                area TEXT,
                city TEXT,
                state TEXT,
                pin_code TEXT,
                image TEXT)'''
        sqlite_cursor.execute(bizz_table)
        sqlite_conn.commit()
        bizz_insert ='''INSERT INTO biz1_details(company_name,card_holder,designation,
                mobile_number,email,website,area,city,state,pin_code ,image)
            VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
    
    def on_button_click():
        
        try:
            sqlite_cursor.execute(bizz_insert, values)
            sqlite_conn.commit()
            st.write("UPLOADED!!")
        except:
            st.write("Already inserted")
        
    st.write('<h4 style="color: green;">AFTER DATA EXTRACTION PRESS THE BUTTON TO UPLOAD TO SQL</h4>',unsafe_allow_html=True)
    if st.button("Upload Data into SQL"):
        on_button_click()
    
       
    
    
        
    
    







        
    
def page_3():
    
    st.write('<h5 style="color: purple;">THE TABLE VIEW</h5>',unsafe_allow_html=True)
    sqlite_db_file ="/content/bizD.db"
    sqlite_conn = sqlite3.connect(sqlite_db_file)
    df = pd.read_sql_query('SELECT * FROM biz1_details ',sqlite_conn)
    sqlite_conn.commit()
    st.dataframe(df)
    st.write('<h4 style="color: purple;">SELECT AN OPTION WHETHER TO UPDATE/DELETE THE TABLE</h4>',unsafe_allow_html=True)
    selected_option = st.radio("OPTIONS", ["UPDATE","DELETE"])
    if selected_option=="UPDATE":
        st.write('<h5 style="color: purple;">SELECT THE BUSINESS FIRM YOU WANT TO UPDATE</h5>',unsafe_allow_html=True)
        sqlite_db_file ="bizD.db"
        sqlite_conn = sqlite3.connect(sqlite_db_file)
        sqlite_cursor = sqlite_conn.cursor()
        query = "SELECT company_name  FROM biz1_details"
        sqlite_cursor.execute(query)
        data = sqlite_cursor.fetchall()
        sqlite_conn.commit()
        options=[row[0] for row in data]
        selected_option = st.selectbox("Select an option:", options)
        st.write('<h5 style="color: purple;">SELECT THE ELEMENT TO UPDATE</h5>',unsafe_allow_html=True)
        conn = sqlite3.connect('bizD.db')  
        cursor = conn.cursor()
        table_name = "biz1_details" 
        query = f"PRAGMA table_info({table_name})"
        cursor.execute(query)
        column_info = cursor.fetchall()
        filled_columns = []
        for column in column_info:
            column_name = column[1]
            query = f"SELECT * FROM {table_name} WHERE {column_name} IS NOT NULL"
            cursor.execute(query)
            data = cursor.fetchone()
            if data is not None:
                filled_columns.append(column_name)
        element = st.radio("OPTIONS",filled_columns )
        st.write('<h5 style="color: purple;">GIVE THE TEXT TO ENTER FOR UPDATION</h5>',unsafe_allow_html=True)
        old_value = st.text_input("GIVE OLD VALUE AND PRESS ENTER")
        new_value= st.text_input("GIVE NEW VALUE AND PRESS ENTER")
        if old_value and new_value:
            sqlite_db_file ="bizD.db"
            sqlite_conn = sqlite3.connect(sqlite_db_file)
            sqlite_cursor = sqlite_conn.cursor()
            query = f'''UPDATE biz1_details SET {element} = ? WHERE {element} = ?'''
            sqlite_cursor.execute(query, (new_value,old_value))
            sqlite_conn.commit()
            st.write('<h5 style="color: purple;">UPDATED!!</h5>',unsafe_allow_html=True)
            sqlite_db_file ="bizD.db"
            sqlite_conn = sqlite3.connect(sqlite_db_file)
            if st.button("Click Me to view the UPDATED Table"):
                st.write('<h5 style="color: purple;">VIEW THE UPDATED TABLE</h5>',unsafe_allow_html=True)
                sqlite_db_file ="bizD.db"
                sqlite_conn = sqlite3.connect(sqlite_db_file)
                sqlite_cursor = sqlite_conn.cursor()
                df = pd.read_sql_query('SELECT * FROM biz1_details ',sqlite_conn)
                sqlite_conn.commit()
                st.dataframe(df)
    if selected_option=="DELETE":
        st.write('<h5 style="color: purple;">DELETING THE DATA SECTION</h5>',unsafe_allow_html=True)
        sqlite_db_file ="bizD.db"
        sqlite_conn = sqlite3.connect(sqlite_db_file)
        sqlite_cursor = sqlite_conn.cursor()
        conn = sqlite3.connect('bizD.db')  
        cursor = conn.cursor()
        table_name = "biz1_details" 
        query = f"PRAGMA table_info({table_name})"
        cursor.execute(query)
        column_info = cursor.fetchall()
        filled_columns = []
        for column in column_info:
            column_name = column[1]
            query = f"SELECT * FROM {table_name} WHERE {column_name} IS NOT NULL"
            cursor.execute(query)
            data = cursor.fetchone()
            if data is not None:
                filled_columns.append(column_name)
        element = st.radio("OPTIONS",filled_columns)
        st.write('<h5 style="color: purple;">GIVE THE VALUE TO DELETE THE DATA</h5>',unsafe_allow_html=True)
        old_value = st.text_input("GIVE THE VALUE AND PRESS ENTER")
        if old_value:
            sqlite_db_file ="/content/bizD.db"
            sqlite_conn = sqlite3.connect(sqlite_db_file)
            sqlite_cursor = sqlite_conn.cursor()
            if st.button("Click Me to view the UPDATED Table"):
                sqlite_db_file ="/content/bizD.db"
                sqlite_conn = sqlite3.connect(sqlite_db_file)
                sqlite_cursor = sqlite_conn.cursor()
                query = f'''DELETE FROM biz1_details WHERE "{element}" = "{old_value}" '''
                sqlite_cursor.execute(query)
                sqlite_conn.commit()
                st.write('<h5 style="color: purple;">THE CHANGED TABLE</h5>',unsafe_allow_html=True)
                df = pd.read_sql_query('SELECT * FROM biz1_details ',sqlite_conn)
                sqlite_conn.commit()
                st.write(df)
        
        
        


    
   
        
        



try:
    if current_page == "Home":
        page_1()
    elif current_page == "Extract & Upload":
        page_2()
    elif current_page == "Data Modification":
        page_3()
except Exception as e:
    
    st.write(" ")





