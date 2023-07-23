from pagefactory.java_page import JavaPage
from pagefactory.python_page import PythonPage
from pagefactory.typescript_page import TypeScriptPage


class PageFactory:

    @staticmethod
    def build_page(language):
        try:
            if language == "python":
                return PythonPage()
            elif language == "java":
                return JavaPage()
            elif language == "typescript":
                return TypeScriptPage()
            raise AssertionError("Language type is not valid.")
        except AssertionError as e:
            print(e)