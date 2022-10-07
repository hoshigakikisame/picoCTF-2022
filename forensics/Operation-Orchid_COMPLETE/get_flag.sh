openssl aes256 -salt -d -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567;
cat flag.txt
