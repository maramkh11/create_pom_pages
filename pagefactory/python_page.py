from common_names import CommonNames, Suffix
from pagefactory.abstract_page import AbstractPage


class PythonPage(AbstractPage):
    
    def __init__(self):
        self.language = "python"
        
    def get_module_name(self,file_name:str):
        if file_name:
            file_name=file_name.lower()
            file_name_list=file_name.split()
            file_name="_".join(file_name_list) +"_"+CommonNames.PAGE.value  + Suffix.PYTHON.value
            return file_name

    def get_class_name(self,file_name):
        if file_name:
            file_name_list=file_name.split()
            class_name=[i.capitalize() for i in file_name_list]
            class_name = "".join(class_name)
            return class_name
            

    def write_class_file(self,class_name,extends=None):
        extends=str(extends or "")
        content="""class {}{}:

    def __init__(self):
        pass
    
        """
        if len(extends)>0:
            extends=f"({extends})"
        content=content.format(class_name,extends)
        return content
    