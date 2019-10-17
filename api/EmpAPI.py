"""
    封装员工的增删改查请求实现
"""
import app


class EmpCRUD:

    # 函数1:增
    def add(self,session,username,mobile,workNumber):
        # return session对象.post("新增的URL",json=提交的数据)
        myAddEmp = {"username": username,
                    "mobile": mobile,
                    "workNumber":workNumber
                    }
        return session.post(app.BASE_URL + "user",
                            json=myAddEmp,
                            headers={ "Authorization":"Bearer " + app.TOKEN})


    # 函数2:改
    def update(self, session, username,userId):
        # session对象.put("修改的URL,后缀ID",json={"username":账号})
        myUpdateEmp = {"username": username,

                       }
        userId1 = "".join(userId)  # 传过来的员工id是个列表，要转成字符串
        print("*" * 100)
        print("**********************id = %s" % userId1)
        return session.put(app.BASE_URL + "user/" + userId1, json=myUpdateEmp,
                           headers={"Authorization": "Bearer " + app.TOKEN}
                           )

    # 函数3:查
    def get(self,session,userId):
        userId1 = "".join(userId)  # 传过来的员工id是个列表，要转成字符串
        return session.get(app.BASE_URL + "user/" + userId1,
                           headers={ "Authorization":"Bearer " + app.TOKEN})


    # 函数4:删
    def delete(self,session,userId):
        userId1 = "".join(userId)  # 传过来的员工id是个列表，要转成字符串
        return session.delete(app.BASE_URL + "user/" + userId1,
                              headers={ "Authorization":"Bearer " + app.TOKEN})
