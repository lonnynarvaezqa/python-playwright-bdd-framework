from pages.base_page import BasePage
from pages.elements.file_upload_elements import FileUploadElements

class FileUploadPage(BasePage):

    def navigate(self):
        """Navigates to the file upload page."""
        self.page.goto(FileUploadElements.UPLOAD_URL)

    def select_file(self, file_path):
        """Selects a file using the file input selector.
        Playwright handles the OS dialog interaction natively.
        """
        self.page.set_input_files(FileUploadElements.FILE_INPUT, file_path)

    def click_upload_button(self):
        """Clicks the upload button."""
        self.page.click(FileUploadElements.UPLOAD_BUTTON)

    def get_uploaded_file_name(self):
        """Returns the name of the uploaded file displayed on the results page."""
        return self.page.inner_text(FileUploadElements.UPLOADED_FILE_NAME)
