# ULFTP
This a beta ftp written in python. 

to execute it

type on command- line

$ python ulftp.py 

Beta version 001

   usage: ulftp.py -u <user> -p <password> -s <server> -r <port>[optional]


=============================
-h => show help
-u => user to connect
-p => password to connect
-s => FTP server
-r => port optional default 21

=============================

After login a prompt mode appears, there are some commands to operate it:

help      => show help 
cwd       => access ftp directory 
local del => delete local files in a directory
localdir  => access local directory
ls        => list ftp directory  or files inside it
mdelete   => delete ftp files
mget      => get ftp files to local directory
mode      => enable or disable passive mode (default passive mode is true)
mput      => put local files on ftp
quit      => quit ftp


