parser grammar HTMLParser;

options {
    tokenVocab = HTMLLexer;
}

// ============================================================
// Reglas sintacticas para el subconjunto de HTML5 tokenizado
// por HTMLLexer.g4.
//
// Nota de diseno: los elementos vacios (void elements: br, img,
// input, meta, etc.) se distinguen de los elementos normales a
// nivel LEXICO (token VOID_NAME vs NAME), por eso aqui existen
// dos alternativas separadas para "element". Gracias a esto la
// gramatica exige, a nivel sintactico, que todo elemento normal
// que no se autocierra tenga una etiqueta de cierre -- pero NO
// verifica que el NOMBRE de esa etiqueta de cierre coincida con
// el de apertura (</div> podria "cerrar" un <span>): esa
// verificacion de nombres, junto con reglas de accesibilidad,
// formularios, seguridad, etc., se hace en la capa semantica
// (HTMLSemanticListener), que es el lugar que corresponde para
// ese tipo de validacion segun el criterio del proyecto.
// ============================================================

htmlDocument
    : DOCTYPE? content* EOF
    ;

content
    : element
    | comment
    | TEXT
    ;

element
    : TAG_OPEN VOID_NAME attribute* (TAG_SELFCLOSE | TAG_CLOSE)                                               # voidElement
    | TAG_OPEN tagName attribute* (TAG_SELFCLOSE | TAG_CLOSE content* TAG_OPEN_SLASH closeTagName TAG_CLOSE)  # normalElement
    ;

tagName
    : NAME
    ;

closeTagName
    : NAME
    ;

comment
    : COMMENT
    ;

attribute
    : attrName (EQUALS attrValue)?
    ;

attrName
    : NAME
    | VOID_NAME
    ;

attrValue
    : STRING
    | NAME
    | VOID_NAME
    ;
