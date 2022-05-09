from pymysql import *

class Database(object):
    def __init__(self):
        self.conn = connect(host='',port = 3306,user='user1',
                            password='',database='',charset='utf8')
        
        #获取游标对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    #table_name:donator_info 或 donation_info 或 account
    #info为元组类型，如果插入到account，则info为(id,password),用于用户注册
    def Insert_info(self,table_name,info):
        #插入数据
        sql = "insert into %s values %s" % (table_name,info)
        self.cursor.execute(sql)
        self.conn.commit()
    
    #用于更新物资数量
    #id为用户id
    #goods_name为物资名称
    #new_quantity为新的数量
    def Update_info(self,id,goods_name,new_quantity):
        #首先查找到该id对应的num序号
        sql = "select num from donator_info where id = %s;" % id
        self.cursor.execute(sql)
        num = self.cursor.fetchone()[0]

        #更新数据
        sql = "update donation_info set quantity = %s where num_to_donator = %s and materials = '%s';" % (new_quantity,num,goods_name)
        self.cursor.execute(sql)
        self.conn.commit()

    #每页显示N个，第M个页面的数据
    #返回的数据类型为元组套元组
    #内部元组为 （id,name,area,phone_num,materials,quantity）
    #如果为空，则返回空元组
    def Show_goods(self,N,M):
        sql = "select donator_info.id,donator_info.name,donator_info.area,donator_info.phone_num,\
                donation_info.materials,donation_info.quantity from donator_info inner join \
                donation_info on donator_info.num = donation_info.num_to_donator limit %s,%s;" % (N*(M-1),N)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #查找特定信息
    #比如用户登录时查询是否有该id，如果没有，则提示注册
    #比如注册时，先查询该id是否已经存在
    #比如登录时，查询id对应的password是否正确
    #比如发布物资时，先查询该发布人是否存在于donator_info表中
    #比如发布物资时，先用该函数查询该发布人对应的num，将其作为物资的num_to_donator
    #target_field为目标字段，为需要查找的内容。table_name为要查找的信息所在的表，limit_field为查找的条件
    #返回值为元组，如果没有则返回None
    #例 ：Search_info('id','account','id',1)   查询account表中是否存在id为1的id
    def Search_info(self,target_field,table_name,limit_field,limit_value):
        sql = "select %s from %s where %s = %s;" % (target_field,table_name,limit_field,limit_value)
        self.cursor.execute(sql)
        return self.cursor.fetchone()




""" def testInsert():
    db = Database()
    db.Insert_info('account',("154654787","sdff41454"))

testInsert()  

def testUpdate():
    db = Database()
    db.Update_info(8540905598,'帐篷',10)

testUpdate()
 

def testShow():
    db = Database()
    return db.Show_goods(5,10)

print(testShow())

def testSearch():
    db = Database()
    return db.Search_info('id','account','id','8540905598')

print(testSearch())
"""