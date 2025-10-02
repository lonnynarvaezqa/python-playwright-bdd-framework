# pages/file_upload_page.py
from pages.base_page import BasePage
from pages.elements.file_upload_elements import FileUploadElements

class FileUploadPage(BasePage):

    def navigate(self):
        """Navega a la página de subida de archivos."""
        self.page.goto(FileUploadElements.UPLOAD_URL)

    def select_file(self, file_path):
        """Selecciona un archivo usando el selector de entrada de archivo.
        Playwright maneja la interacción con el diálogo del OS de forma nativa.
        """
        self.page.set_input_files(FileUploadElements.FILE_INPUT, file_path)

    def click_upload_button(self):
        """Hace clic en el botón de subir."""
        self.page.click(FileUploadElements.UPLOAD_BUTTON)

    def get_uploaded_file_name(self):
        """Retorna el nombre del archivo subido que se muestra en la página de resultados."""
        return self.page.inner_text(FileUploadElements.UPLOADED_FILE_NAME)