from ftplib import FTP
from cmd import Cmd

import sys,os,glob


ftp = FTP() 
diretorioLocal = ''
diretorioFTP = ''

class Prompt(Cmd):
    
   
   
   def open(self,servidor,porta,usuario,senha):
      
   
    ftp.connect(servidor,porta,200)
    ftp.login(usuario,senha)
    ftp.set_pasv('true')
    print ftp.getwelcome()
    
    return ftp
   
   
   def do_mode(self,args):
       
       
       if(args != "true" and args != "false"):
           print "parameter invalid"
           return
       
       ftp.set_pasv(args)
       
       if(args == "true"):
            print "passive mode enabled"
       else:
            print "passive mode disabled"
   
   def do_quit(self,args):
        
        print "Thanks for using"
        print "Quiting..."
        ftp.quit()
        sys.exit(2)
        
    
   def do_cwd(self,args):
          
          diretorioFTP = ftp.cwd(args)
          print diretorioFTP
   
   def do_ls(self,args):
          ftp.dir()  
          
   def do_localdir(self,args):
        
        if args == '':
           diretorioLocal = os.getcwd() 
           print diretorioLocal
        else:
           
           try: 
                os.chdir(args)
                diretorioLocal = os.getcwd()
                print diretorioLocal
           except Exception,e:
               print str(e)
          
   def do_mget(self,args):
        
        for arquivo in ftp.nlst(args):
            getArquivo = open(arquivo,'wb')
            print 'Getting '+ arquivo
            ftp.retrbinary('RETR '+arquivo,getArquivo.write)
            getArquivo.close()
            print "done"
        
   def do_mput(self,args):
   
    try:
         
        for arquivos in glob.glob(args):
         
           arquivos.lower()
           getArquivo = open(arquivos,'rb')
           print 'sending ' +arquivos
           ftp.storbinary('STOR  '+arquivos, getArquivo)
           getArquivo.close() 
           print "done"
      
    except Exception,e:
        print str(e)
        
   def do_mdelete(self,args):
      try:
          for arquivo in ftp.nlst(args):
            print "Deleting "+arquivo
            ftp.delete(arquivo)
      except Exception,e:
        print str(e)   
   
        
   
        
   def do_localdel(self,args):
      try:
         
        for arquivos in glob.glob(args):
         
           print 'deleting ' +arquivoslocal
           os.remove(arquivos)
      
      except Exception,e:
            print str(e)     
        
        