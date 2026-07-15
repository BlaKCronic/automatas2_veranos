# Proyecto - Compilador FrontEnd (HTML5 + CSS3)

Analizador lexico, sintactico y semantico para un subconjunto representativo
de **HTML5** y **CSS3**, construido con ANTLR 4.13.2 y una interfaz en
Streamlit. El JavaScript queda deliberadamente fuera de alcance (ver
enunciado del proyecto).

## Instrucciones

### Comandos enviroment
```
python -m venv .venv
```
```
.\.venv\Scripts\Activate.ps1
```

Si da error de permisos
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Dependencias
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

### Correr app
```
streamlit run app.py
```

### Comando para desactivar
```
deactivate
```

### Regenerar los parsers de ANTLR (solo si se modifica algun .g4)
Requiere Java y `antlr-4.13.2-complete.jar` en el CLASSPATH.
```
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 HTMLLexer.g4
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener HTMLParser.g4
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -listener CSS.g4
```

Hay archivos de prueba en `ejemplos/` (`valido.html`, `con_problemas.html`,
`valido.css`, `con_problemas.css`, `falso.html`) para probar la app sin
tener que escribir codigo HTML/CSS a mano.

---

## Arquitectura del proyecto

```
archivo.py              -> Archivo: valida EXTENSION (.html/.htm/.css) y lee el contenido
validador_contenido.py  -> ValidadorContenido: valida CONTENIDO (heuristica), mas alla de la extension
analizador_lexico.py    -> AnalizadorLexico: corre HTMLLexer/CSSLexer, junta tokens y errores lexicos
analizador_sintactico.py-> AnalizadorSintactico (helper): corre HTMLParser/CSSParser, arbol + errores
analizador_semantico.py -> AnalizadorSemantico: recorre el arbol con un Listener y junta "hallazgos"
app.py                   -> interfaz Streamlit que conecta todo lo anterior
HTMLLexer.g4 / HTMLParser.g4 -> gramatica de HTML5 (lexer y parser separados, por los modos de lexer)
CSS.g4                   -> gramatica de CSS3 (combinada, lexer+parser en un solo archivo)
```

`archivo.py` y `validador_contenido.py` estan separados a proposito
(criterio 4 del proyecto): `Archivo` solo sabe leer el archivo y mirar su
nombre/extension; `ValidadorContenido` es un helper aparte que analiza el
TEXTO del archivo con expresiones regulares (cuenta etiquetas tipo
`<tag>`, reglas tipo `selector { propiedad: valor; }`, `@media`/`@import`,
etc.) para detectar si el contenido realmente corresponde al lenguaje que
promete la extension (por ejemplo, un `.html` que en realidad es texto
plano -- ver `ejemplos/falso.html`).

## Alcance de las gramaticas (por que no es "todo HTML5/CSS3")

Este proyecto cubre un **subconjunto representativo** de cada lenguaje, no
la especificacion completa (que incluye cientos de reglas de recuperacion
de errores pensadas para navegadores, tags de auto-cierre implicito como
`<p>`/`<li>`, entidades HTML, etc.). Esto fue una decision de alcance
deliberada para mantener la gramatica mantenible y depurable dentro de un
proyecto de curso.

**HTML (`HTMLLexer.g4` + `HTMLParser.g4`)**
- DOCTYPE, comentarios, CDATA, elementos, atributos (con o sin comillas),
  texto y elementos vacios (`void elements`: `br`, `img`, `input`, `meta`,
  `link`, `hr`, etc.)
- El lexer usa **modos** (`DEFAULT_MODE` / `TAG`) porque HTML es sensible
  al contexto: fuera de una etiqueta el alfabeto es texto libre, dentro de
  `<...>` son nombres, `=`, cadenas y `>`/`/>`. Por eso el HTML esta
  separado en `HTMLLexer.g4` (lexer grammar) y `HTMLParser.g4` (parser
  grammar): ANTLR no permite `mode` dentro de una gramatica combinada.
- Los elementos vacios se distinguen a nivel **lexico** (token `VOID_NAME`
  declarado antes que el `NAME` generico) para que la gramatica exija, a
  nivel sintactico, que un elemento normal sin autocierre tenga **alguna**
  etiqueta de cierre -- pero sin verificar que el nombre coincida (eso
  queda para la capa semantica).
- El contenido de `<style>` y `<script>` se trata como texto plano: no se
  vuelve a tokenizar como CSS/JS dentro del HTML. El CSS se analiza aparte
  cuando se sube un archivo `.css` independiente.

**CSS (`CSS.g4`)**
- Selectores: tipo, universal `*`, clase, id, atributo (`[attr=valor]`),
  pseudo-clase, pseudo-elemento y combinadores (descendiente, `>`, `+`,
  `~`).
- At-rules soportadas explicitamente: `@media`, `@import`, `@font-face`,
  `@keyframes`.
- Declaraciones `propiedad: valor;` con numeros+unidad, porcentajes,
  colores hexadecimales, strings, funciones (`rgb()`, `url()`, `calc()`,
  etc.) y `!important`.
- `calc()` se reconoce sintacticamente como una lista de tokens dentro de
  parentesis, sin evaluar su aritmetica (esta fuera de alcance).
- No existe un token lexico "unidad" (`px`, `em`, `s`, ...): un numero
  seguido de un identificador se acepta sintacticamente sin importar cual
  sea ese identificador, y es la capa **semantica** la que valida si es
  una unidad CSS conocida. Esto evita una ambiguedad real entre, por
  ejemplo, el selector de etiqueta `s` (`<s>`, texto tachado) y la unidad
  `s` de segundos.

## Validacion semantica (criterio 6)

Implementada con **Listener de ANTLR** (`HTMLSemanticListener` y
`CSSSemanticListener` en `analizador_semantico.py`), que se recorre con
`ParseTreeWalker` **despues** de que el analisis lexico y sintactico
terminan sin errores. Cada hallazgo tiene un `nivel` (`error` /
`advertencia` / `info`) y una `categoria`.

Chequeos de HTML:
- Etiqueta de cierre cuyo nombre no coincide con la de apertura.
- Elemento que deberia ser vacio pero se escribio como normal.
- `<html>` sin `lang`, falta de `<meta charset>`, `<head>`/`<body>`
  faltantes o duplicados.
- `id` duplicados en el documento.
- Formularios sin `action`, o con `method` distinto de GET/POST.
- Atributos de evento inline (`onclick`, `onerror`, ...) como riesgo XSS.
- `target="_blank"` sin `rel="noopener noreferrer"`.
- Recursos (`src`/`href`) cargados por `http://` (contenido mixto).

Chequeos de CSS:
- Propiedad declarada mas de una vez dentro de la misma regla.
- Unidad numerica no reconocida.
- Color hexadecimal con longitud invalida (no 3/4/6/8 digitos).
- Regla o `@media` vacios.
- `@import` declarado despues de otra regla (invalido segun la spec: los
  navegadores lo ignoran si no es la primera regla).
- `@import` de un recurso por `http://`.
- `font-family` sin familia generica de respaldo.

## Mapeo de requisitos "de lenguaje web" sobre HTML/CSS

El profesor pide agregar vistas, modelos, controladores, rutas,
formularios, validaciones, plantillas, sesiones, cookies, peticiones
GET/POST, conexion a base de datos, autenticacion y seguridad basica "si
elegiste un lenguaje usado en desarrollo web". HTML y CSS son lenguajes de
**marcado y estilo**, no ejecutan logica de servidor: no hay proceso que
reciba peticiones, no hay ORM ni motor de base de datos, y no hay
"controlador" que arme una respuesta. Por eso estos criterios se mapean a
**patrones detectables en el propio marcado**, en vez de simularse con un
backend aparte (lo cual se hubiera salido del alcance de un "compilador
front end"):

| Criterio del profesor | Como se detecta en este proyecto |
|---|---|
| Vistas / plantillas | El propio documento HTML actua como vista. El tag `<template>` se reporta explicitamente como plantilla reutilizable. |
| Rutas | Atributo `action` de `<form>` y `href` de `<a>`. |
| Peticiones GET / POST | Atributo `method` de `<form>` (GET por defecto si no se especifica, como en el estandar HTML). |
| Formularios | Cualquier `<form>` y sus `<input>`/`<button>`. |
| Validaciones | Atributos `required`, `pattern`, `min`, `max`, `minlength`, `maxlength`, `step` y tipos `email`/`url`/`number`/`tel`/`date`. |
| Autenticacion | `<input type="password">`, con verificacion de `autocomplete` seguro. |
| Sesiones / cookies | `<input type="hidden">` (patron tipico de token CSRF / dato de sesion enviado por el formulario). |
| Seguridad basica | Atributos de evento inline (riesgo XSS), `target="_blank"` sin `rel="noopener"`, recursos servidos por HTTP sin cifrar, falta de `lang`/`charset`. |
| Modelos / controladores / conexion a BD | **No aplican de forma literal**: HTML/CSS no ejecutan codigo de servidor. Se documenta aqui en vez de simularse, para no fabricar un backend que quedaria fuera del alcance del "compilador front end" que pide este proyecto. |

## Alfabeto

Basado en el documento del proyecto (letras, digitos, operadores,
agrupacion, separadores, caracteres especiales y espacios en blanco), las
gramaticas de HTML y CSS usan subconjuntos de ese alfabeto segun lo que
cada lenguaje realmente necesita: HTML usa sobre todo letras/digitos para
nombres y `<>/="'` para su sintaxis de etiquetas; CSS usa ademas
`{}[]():;,.` y operadores (`+ - * / % ! # @`) para selectores, funciones y
valores.
