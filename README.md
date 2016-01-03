# ULFTP
This a beta ftp written in python. 

to execute it

type on command- line

$ python ulftp.py 

Beta version 001

   usage: ulftp.py -u <user> -p <password> -s <server> -r <port>[optional]


=============================
-h => show help<br>
-u => user to connect<br>
-p => password to connect<br>
-s => FTP server<br>
-r => port optional default 21<br>

=============================

After login a prompt mode appears, there are some commands to operate it:

help      => show help <br>
cwd       => access ftp directory <br>
localdel => delete local files in a directory<br>
localdir  => access local directory<br>
ls        => list ftp directory  or files inside it<br>
mdelete   => delete ftp files<br>
mget      => get ftp files to local directory<br>
mode      => enable or disable passive mode (default passive mode is true)<br>
mput      => put local files on ftp<br>
quit      => quit ftp<br>

