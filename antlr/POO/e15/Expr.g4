grammar Expr;

options {
  caseInsensitive = true;
}

program: commandLine* EOF;

commandLine: command SEMICOLON?;

command:
    sudo? baseCommand arg*;

sudo: SUDO;

baseCommand:
    NMAP
    | SS
    | TCPDUMP
    | CURL
    | DIG
    | JOURNALCTL
    | GREP
    | UFW;

arg:
    OPTION
    | IP_CIDR
    | IP_ADDR
    | HOSTNAME
    | STRING
    | WORD;

SUDO: 'sudo';
NMAP: 'nmap';
SS: 'ss';
TCPDUMP: 'tcpdump';
CURL: 'curl';
DIG: 'dig';
JOURNALCTL: 'journalctl';
GREP: 'grep';
UFW: 'ufw';

OPTION: '--' [a-zA-Z-]+ | '-' [a-zA-Z]+;
IP_CIDR: [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ '/' [0-9]+;
IP_ADDR: [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+;
HOSTNAME: [a-zA-Z0-9.-]+;
STRING: '\'' (~['\r\n])* '\'' | '"' (~["\r\n])* '"';
WORD: [a-zA-Z0-9_./-]+;
SEMICOLON: ';';
WS: [ \t\r\n]+ -> skip;
