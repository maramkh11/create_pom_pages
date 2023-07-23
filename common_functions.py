import csv
import os
import re
import shutil
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import pandas as pd

from common_names import CSVColumnsNames

load_dotenv()

CSV_COLUMNS_NAMES=(CSVColumnsNames.PAGE_NAME.value,
                   CSVColumnsNames.PACKAGE.value,
                   CSVColumnsNames.EXTEND.value)

def get_programming_langauge():
    return os.getenv("Programming_Language")

def get_ui_framework():
   return os.getenv("UI_Framework") 

def get_csv_data():
    csv_file_name=os.getenv("CSV_Data_File_Name")
    if os.getenv("HTML_Elements_File_Name"):
        inner_text_list=get_html_elements_inner_text()
        data = {CSVColumnsNames.PAGE_NAME.value: inner_text_list,
                CSVColumnsNames.PACKAGE.value:[None] * len(inner_text_list),
                CSVColumnsNames.EXTEND.value:[None] * len(inner_text_list)}
        df = pd.DataFrame(data)
        df.to_csv(csv_file_name, index=False)

    pages_list=[]
    with open(csv_file_name,newline='',encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            pages_list.append(row)
        csvfile.close()    
    return pages_list


def get_html_elements_inner_text():
    tag_name=os.getenv("Tag_Name")
    with open(os.getenv("HTML_Elements_File_Name"), 'r', encoding='utf-8') as file:
        html_content = file.read()
        tag_names_list = list(set(re.findall(r'<\s*([a-zA-Z0-9]+)', html_content)))
        print(tag_names_list)
    soup = BeautifulSoup(html_content, 'html.parser')
    inner_texts = [element.get_text(strip=True) for element in soup.find_all(tag_name)]
    inner_texts = [item for item in inner_texts if item]
    return inner_texts


def get_directories_name(pages_data_list:list):
    packages_list=[]
    for page in pages_data_list:
        packages_list.append(page["package"])
    return list(set(packages_list))    

def remove_directory(directory):
    try:
        folder_name=f'./{directory}/'
        if os.path.exists(folder_name) and folder_name !='':
            files=os.listdir(folder_name)
            if len(files)>0:
                shutil.rmtree(folder_name)
            print(f"Directory '{directory}' successfully removed.")
    except OSError as e:
        print(f"Error: {e}")

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' successfully created.")

def remove_all_directories(directories_name_list:list):
    for name in directories_name_list:
        remove_directory(name)

def create_all_directories(directories_name_list:list):
    for name in directories_name_list:
        create_directory(name)             
  