# pages/elements/file_upload_elements.py

class FileUploadElements:
    """Selectores para la página de Subida de Archivos."""

    # Campo de entrada de archivo. Este es el selector clave.
    FILE_INPUT = "#file-upload"

    # Botón para iniciar la subida (Submit)
    UPLOAD_BUTTON = "#file-submit"

    # Elemento que muestra el nombre del archivo subido con éxito
    UPLOADED_FILE_NAME = "#uploaded-files"

    # URL de la página de File Upload
    UPLOAD_URL = "https://the-internet.herokuapp.com/upload"