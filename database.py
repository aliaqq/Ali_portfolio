from sqlalchemy import create_engine,text
import os 
engine = create_engine(os.environ['DB_CONNECTION_STRING' ])

def load_projects_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from Myprojects"))
    projects = []
    for row in result.all():
      projects.append(dict(row._mapping))
  return projects
def load_project_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from Myprojects where id = :val"),{"val":id})
  rows =dict(rows)[0]._mapping