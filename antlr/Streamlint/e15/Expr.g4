grammar Expr;

// ----------------------------------------------------------------------
// Regla inicial del parser (se conserva para que ANTLR genere el parser).
// El analizador lexico solo usa el lexer, pero mantenemos una regla raiz
// para conservar la estructura del proyecto.
//
// Lenguaje: comandos de shell (herramientas de red y seguridad).
// ----------------------------------------------------------------------
programa: elemento* EOF ;

elemento
    : COMANDO
    | OPCION
    | IP
    | RUTA
    | DOMINIO
    | CADENA
    | NUMERO
    | IDENTIFICADOR
    ;

// ---------- Comandos reconocidos ----------
COMANDO
    : 'nmap' | 'ss' | 'sudo' | 'tcpdump' | 'curl'
    | 'dig' | 'journalctl' | 'grep' | 'ufw'
    ;

// ---------- Opciones / flags (-i, -sV, --since) ----------
OPCION : '-' '-'? [a-zA-Z]+ ;

// ---------- Cadenas entre comillas dobles ----------
CADENA : '"' (~["\r\n])* '"' ;

// ---------- Direccion IPv4 con mascara CIDR opcional ----------
IP : [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ ('/' [0-9]+)? ;

// ---------- Rutas absolutas (/var/log/auth.log) ----------
RUTA : ('/' [a-zA-Z0-9_.-]+)+ ;

// ---------- Dominios (ejemplo.com) ----------
DOMINIO : [a-zA-Z0-9_]+ ('.' [a-zA-Z0-9_]+)+ ;

// ---------- Numeros y palabras sueltas ----------
NUMERO        : [0-9]+ ;
IDENTIFICADOR : [a-zA-Z_] [a-zA-Z0-9_]* ;

// ---------- Espacios en blanco (ignorados) ----------
WS : [ \t\r\n]+ -> skip ;
