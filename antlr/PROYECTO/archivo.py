# Importamos os para trabajar con nombres y extensiones de archivos
import os


# Clase para representar el archivo subido y validar su extension.
# Deliberadamente esta clase SOLO conoce el nombre/extension y el
# contenido crudo del archivo. No sabe nada de HTML ni de CSS: esa
# responsabilidad se delega a ValidadorContenido (validador_contenido.py),
# que es quien decide si el CONTENIDO realmente parece pertenecer al
# lenguaje que la extension promete.
class Archivo:

    # Extensiones que este proyecto sabe procesar
    EXTENSIONES_VALIDAS = {".html": "html", ".htm": "html", ".css": "css"}

    # Constructor de la clase
    def __init__(self, archivo_subido):

        # Guardamos el archivo que viene desde Streamlit
        self.archivo_subido = archivo_subido

        # Guardamos el nombre del archivo
        self.nombre = archivo_subido.name

    # Metodo para obtener la extension del archivo
    def obtener_extension(self):

        # Separamos el nombre del archivo y obtenemos la extension
        return os.path.splitext(self.nombre)[1].lower()

    # Metodo para saber a que tipo de lenguaje corresponde la extension
    # Retorna "html", "css" o None si la extension no es reconocida
    def tipo_por_extension(self):

        return self.EXTENSIONES_VALIDAS.get(self.obtener_extension())

    # Metodo para validar si el archivo es .html/.htm
    def es_html(self):

        return self.tipo_por_extension() == "html"

    # Metodo para validar si el archivo es .css
    def es_css(self):

        return self.tipo_por_extension() == "css"

    # Metodo para validar si la extension es alguna de las soportadas
    def extension_soportada(self):

        return self.tipo_por_extension() is not None

    # Metodo para leer el contenido del archivo
    def leer(self):

        # Leemos el archivo como bytes
        contenido_bytes = self.archivo_subido.read()

        # Convertimos los bytes a texto (ignoramos bytes invalidos en vez
        # de tronar la app si el usuario sube un archivo binario disfrazado)
        contenido_texto = contenido_bytes.decode("utf-8", errors="replace")

        # Retornamos el texto del archivo
        return contenido_texto

    # Metodo para regresar informacion del archivo
    def obtener_info(self):

        # Retornamos un diccionario con informacion simple
        return {
            "nombre": self.nombre,
            "extension": self.obtener_extension(),
            "tipo_detectado_por_extension": self.tipo_por_extension() or "desconocido",
        }
