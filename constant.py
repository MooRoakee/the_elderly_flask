# 设置连接数据库的URL
user = 'root'
password = 'Mfzr123#'
database = 'the_elderly'
CONNECT_URL = 'mysql://%s:%s@localhost:3306/%s' % (user,password,database)

WRONG_PASSWORD = {'result': 'failed', 'reason': 'wrong password'} 
NO_SUCH_USER = {'result': 'failed', 'reason': 'no such user'} 