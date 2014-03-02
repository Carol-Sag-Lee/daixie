INSERT INTO mysql.user(HOST,USER,PASSWORD) VALUES('localhost','daixie',password('daixie2014'));
FLUSH PRIVILEGES;

GRANT ALL PRIVILEGES ON daixie.* TO daixie@localhost IDENTIFIED BY 'daixie2014';
FLUSH PRIVILEGES;