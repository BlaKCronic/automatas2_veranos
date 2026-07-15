import streamlit as st

from archivo import Archivo
from validador_contenido import ValidadorContenido
from analizador_lexico import AnalizadorLexico
from analizador_sintactico import AnalizadorSintactico
from analizador_semantico import AnalizadorSemantico


# Etiquetas legibles para las categorias que usa el analizador semantico,
# alineadas con los criterios del profesor (rutas, formularios, sesiones,
# autenticacion, validaciones, plantillas, seguridad, etc.)
NOMBRES_CATEGORIA = {
    "ruta": "Rutas / peticiones",
    "formulario": "Formularios",
    "autenticacion": "Autenticacion",
    "sesion": "Sesiones / cookies",
    "validacion": "Validaciones",
    "plantilla": "Plantillas",
    "seguridad": "Seguridad",
    "estructura": "Estructura del documento",
    "css": "Reglas CSS",
}

ICONO_NIVEL = {
    "error": "🔴",
    "advertencia": "🟠",
    "info": "🔵",
}


class App:

    def __init__(self):
        st.set_page_config(page_title="Compilador FrontEnd - HTML5 y CSS3", layout="wide")
        self.validador_contenido = ValidadorContenido()

    def ejecutar(self):

        st.title("Compilador FrontEnd - HTML5 y CSS3")
        st.write(
            "Sube un archivo `.html`/`.htm` o `.css` para ver su analisis lexico, "
            "sintactico y semantico (ANTLR)."
        )

        archivo_subido = st.file_uploader("Selecciona tu archivo", type=["html", "htm", "css"])

        if archivo_subido is None:
            st.info("Primero sube un archivo .html/.htm o .css")
            return

        archivo = Archivo(archivo_subido)

        # --- Criterio 4a: validacion por EXTENSION ---
        if not archivo.extension_soportada():
            st.error(
                f"Extension \"{archivo.obtener_extension()}\" no soportada. "
                f"Este proyecto solo analiza archivos .html, .htm o .css."
            )
            return

        tipo = archivo.tipo_por_extension()
        codigo = archivo.leer()
        info = archivo.obtener_info()

        st.subheader("Informacion del archivo")
        col1, col2, col3 = st.columns(3)
        col1.metric("Nombre", info["nombre"])
        col2.metric("Extension", info["extension"])
        col3.metric("Tipo detectado", info["tipo_detectado_por_extension"].upper())

        # --- Criterio 4b: validacion de CONTENIDO (mas alla de la extension) ---
        contenido_valido, mensaje_contenido = self.validador_contenido.validar(codigo, tipo)

        continuar = True
        if not contenido_valido:
            st.warning(f"Validacion de contenido: {mensaje_contenido}")
            continuar = st.checkbox(
                "El contenido no parece coincidir con la extension. Analizar de todas formas.",
                value=False,
            )
        else:
            st.success(f"Validacion de contenido: {mensaje_contenido}")

        if not continuar:
            return

        st.subheader("Codigo original")
        st.code(codigo, language=tipo)

        # --- Analisis LEXICO ---
        analizador_lexico = AnalizadorLexico(tipo)
        analizador_lexico.analizar(codigo)
        tokens = analizador_lexico.obtener_tokens()
        errores_lexicos = analizador_lexico.obtener_errores()

        st.subheader("Analisis lexico")
        if len(tokens) == 0:
            st.warning("No se encontraron tokens")
        else:
            st.caption(f"{len(tokens)} tokens reconocidos")
            st.dataframe(tokens, use_container_width=True)

        if len(errores_lexicos) == 0:
            st.success("No hay errores lexicos")
        else:
            st.error(f"{len(errores_lexicos)} error(es) lexico(s)")
            st.dataframe(errores_lexicos, use_container_width=True)

        # --- Analisis SINTACTICO (usa el helper AnalizadorSintactico) ---
        # Se genera un flujo de tokens nuevo porque el anterior ya fue
        # consumido por CommonTokenStream.fill() en el analizador lexico.
        lexer, flujo_tokens = analizador_lexico.nuevo_flujo_tokens(codigo)
        analizador_sintactico = AnalizadorSintactico(tipo)
        arbol = analizador_sintactico.analizar(flujo_tokens)
        errores_sintacticos = analizador_sintactico.obtener_errores()

        st.subheader("Analisis sintactico")
        if len(errores_sintacticos) == 0:
            st.success("No hay errores sintacticos")
        else:
            st.error(f"{len(errores_sintacticos)} error(es) sintactico(s)")
            st.dataframe(errores_sintacticos, use_container_width=True)

        with st.expander("Ver arbol de derivacion (parse tree)"):
            st.code(analizador_sintactico.obtener_arbol_texto(), language="text")

        # --- Analisis SEMANTICO (Listener de ANTLR, corre solo si el ---
        # --- analisis sintactico no tuvo errores fatales) ---
        st.subheader("Analisis semantico")

        if len(errores_sintacticos) > 0:
            st.info(
                "El analisis semantico se omite porque hay errores sintacticos que impiden "
                "construir un arbol de derivacion confiable."
            )
            return

        analizador_semantico = AnalizadorSemantico(tipo)
        hallazgos = analizador_semantico.analizar(arbol)

        if len(hallazgos) == 0:
            st.success("No se encontraron observaciones semanticas.")
        else:
            errores = [h for h in hallazgos if h["nivel"] == "error"]
            advertencias = [h for h in hallazgos if h["nivel"] == "advertencia"]
            informativos = [h for h in hallazgos if h["nivel"] == "info"]

            col1, col2, col3 = st.columns(3)
            col1.metric("Errores semanticos", len(errores))
            col2.metric("Advertencias", len(advertencias))
            col3.metric("Informativos", len(informativos))

            st.dataframe(
                [
                    {
                        "nivel": f"{ICONO_NIVEL.get(h['nivel'], '')} {h['nivel']}",
                        "categoria": NOMBRES_CATEGORIA.get(h["categoria"], h["categoria"]),
                        "mensaje": h["mensaje"],
                        "linea": h["linea"],
                        "columna": h["columna"],
                    }
                    for h in hallazgos
                ],
                use_container_width=True,
            )

            if tipo == "html":
                st.caption(
                    "Mapeo de criterios de 'lenguaje web' sobre HTML/CSS: rutas y peticiones GET/POST "
                    "(formularios), autenticacion (input password), sesiones/cookies (input hidden / "
                    "tokens CSRF), validaciones (required/pattern/type), plantillas (<template>) y "
                    "aspectos basicos de seguridad (XSS inline, target=_blank, contenido mixto HTTP). "
                    "Ver Readme.md para el detalle completo de esta decision de diseno."
                )


if __name__ == "__main__":
    app = App()
    app.ejecutar()
