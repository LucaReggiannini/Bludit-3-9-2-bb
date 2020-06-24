# Bludit-3-9-2-bb
Bludit 3.9.2 - bruteforce bypass - CVE-2019-17240
\
\
Very simple script based on CVE-2019-17240.
\
Original POC and explanation: https://github.com/bludit/bludit/pull/1090.  
  
  
```
usage: python ./bludit-3-9-2-bb.py -l 'http://sitename.com/admin/login' -u ./usernames_file_list.txt -p ./passwords_file_list.txt
-l : login page (example: http://192.168.1.50/admin/login)
-u : file with usernames list (one by line)
-p : file with passwords list (one by line)
-h : help
-v : verbose (show all tested 'username:password')
```


