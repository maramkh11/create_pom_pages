import os
from dotenv import load_dotenv
from common_functions import create_all_directories, get_csv_data, get_directories_name, get_programming_langauge, remove_all_directories
from pagefactory.page_factory import PageFactory

load_dotenv()

def create_module_file(page_opject,page_data):
    page_name=page_data["page_name"]
    extend=page_data["extend"]
    package=page_data["package"]

    module_name=page_opject.get_module_name(page_name)
    class_name=page_opject.get_class_name(page_name)

    if extend and not len(extend)==0:
        extend_moudle_name=page_opject.get_module_name(extend)
        extend_class_name=page_opject.get_class_name(extend)
        extend_file_path = os.path.join(package,extend_moudle_name)
        if not os.path.exists(extend_file_path):
            with open(extend_file_path, 'w') as file:
                file.write(page_opject.write_class_file(extend_class_name))
                file.close()
        file_path = os.path.join(package,module_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(page_opject.write_class_file(class_name,extend_class_name))
                file.close()
    else:
        file_path = os.path.join(package,module_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(page_opject.write_class_file(class_name))
                file.close()                  

def create_pages():
    language=get_programming_langauge()
    page_object=PageFactory().build_page(language=language)
    pages_data_list=get_csv_data()
    directories_names=get_directories_name(pages_data_list)
    # remove_all_directories(directories_names)
    # create_all_directories(directories_names)
    for page_data in pages_data_list:
        create_module_file(page_object,page_data)

create_pages()        