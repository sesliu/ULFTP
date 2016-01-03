from ftplib import FTP
from Prompt import Prompt

import sys, getopt



            

def main(argv):
   
    parametro = '   usage: ulftp.py -u <user> -p <password> -s <server> -r <port>[optional]'   
    diretorioAtual = ''
    usuario = ''
    senha = ''
    servidor =''
    porta = 21
    ftpDados = FTP()
    
    
    try:
        opts, args = getopt.getopt(argv,"hu:p:s:c:r:")
    except getopt.GetoptError:
        print 'there are invalid parameters'
        print''
        print parametro   
        print ''
        sys.exit(2)
    for opt,arg in opts:
         if opt == '-h':
            print '' 
            print '2015 -  Software developed by Ulisses de Castro'
            print 'this is a basic ftp client'
            print ''
            print 'beta version 001'
            print ''
            print parametro
            print ''
            print 'This help'
            print '==============================='
            print '-u => user to connect'
            print '-p => password to connect'
            print '-s => FTP server'
            print '-r => port optional default 21'
            print '==============================='
            print ''
            sys.exit()
         elif opt in ("-u"):
            usuario = arg
            
         elif opt in ("-p"):
             senha = arg
           
         elif opt in ("-s"):
             servidor = arg
         elif opt in("-c"):
                 diretorioAtual = arg    
         elif opt in("-r"):
             
             if arg != '':
                porta = arg
         else:  
            print 'there are invalid parameters'
            print''
            print parametro    
            print ''

   
           
   
   
         if usuario !='' and senha !='' and servidor !='':
       
          try:
            
            
            
            print ''
            prompt = Prompt()
            prompt.open(servidor,porta,usuario,senha)
            prompt.prompt ='>$ '
            prompt.cmdloop('Starting prompt...')
            
            
            
            
          except Exception, e:
             print str(e)
             sys.exit(2)
             
    print parametro       

if __name__ =='__main__':
    
    main(sys.argv[1:])
  
    