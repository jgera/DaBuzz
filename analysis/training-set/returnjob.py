import cherrypy
import psycopg2

class ReturnJob(object):
  @cherrypy.expose
  @chrrypy.tools.json_out()
  def index(self, paraid, score):
    conn = psycopg2.connect()

    cur = conn.cursor()

    if score not in (-1,0,1):
      return "FAILURE"

    #Get the id and the paragraph for all elements with an empty score
    sql = "UPDATE trainset SET score=%s WHERE id=%s"
    args = score,paraid
    cur.execute(sql, args)

    cur.close()

    return "SUCCESS"