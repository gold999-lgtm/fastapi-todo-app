import sys
sys.path.append("./")
from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode

#create todo
def create_to_do(todo:str)->dict:
    try:
        req=Todo(todo)
        db_session.add(req)
        db_session.commit()
        return {
            "status":"OK",
            "message":"new todo added"
        }
    except Exception as e:
        return {"status":"error",
                "message":str(e)}


#get all todo
def get_all():
    try:
        res=db_session.query(Todo).all()
        docs=decode.decode_todos(res)
        return  {"status":"ok",
                "data":docs}
    except Exception as e:
        return {"status":"error",
                "message":str(e)}
    
def get_one(_id:int):
    try:
        criteria={"_id":_id}
        res=db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res!=None:
            docs=decode.decode_todo(res)
            return  {"status":"ok",
                    "data":docs}
        else:
            return {
                "status":"error","message":f"Record with id{_id} do not Exist"
            }
    except Exception as e:
        return {"status":"error",
                "message":str(e)}
    
#upadate todo

def update_todo(_id:int,title:str):
    try:
        criteria={"_id":_id}
        res=db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res!=None:
            res.todo=title
            db_session.commit()
            return {"status":"ok",
                    "message":"Record updated successfully"}
        else:
            return {
                "status":"error","message":f"Record with id{_id} do not Exist"
            }
    except Exception as e:
        return {"status":"error",
                "message":str(e)}
    
#edlete todo

def delete_todo(_id:int):
    try:
        criteria={"_id":_id}
        res=db_session.query(Todo).filter_by(**criteria).one_or_none()
        if res!=None:
            db_session.delete(res)
            db_session.commit()
            return {"status":"ok",
                    "message":"Record deleted successfully"}
        else:
            return {
                "status":"error","message":f"Record with id{_id} do not Exist"
            }
    except Exception as e:
        return {"status":"error",
                "message":str(e)}

#res=create_to_do("Creating a mern stack block")
#res=get_all()
#res=get_one(1)
#res=update_todo(1,"Developing an ecommerce website")
res=delete_todo(1)
print(res)