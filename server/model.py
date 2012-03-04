import web
import config

if config.is_local:
  db = web.database(dbn='sqlite', db=config.db_name)
else:
  print "NOT RUNNING LOCALLY"
  db = web.database(dbn='mysql', \
      db=config.db_name, \
      user=config.mysql_db_user, \
      pw=config.mysql_db_password)

def get_todos():
  return db.select('todo', order='id')

def new_todo(text):
  db.insert('todo', title=text)

def del_todo(id):
  db.delete('todo', where="id=$id", vars=locals())
