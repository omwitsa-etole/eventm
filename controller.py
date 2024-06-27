from db import *
import random
from datetime import date, timedelta

from models import * 

class Category:
    @staticmethod
    async def create(name,slug,thumb,status):
        query = DatabaseManager.insert(f"insert into categories (name,slug,image,status) values('%s','%s','%s','%s')"%(name,slug,thumb,status))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def get(id):
        query = await DatabaseManager.query(f"select * from categories where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        category = Model_Category(*query[0])

        return category.to_dict()
    
    @staticmethod
    async def get_all():
        categories = []
        query = await DatabaseManager.query(f"select * from categories order by id desc")
        if query == None or len(query) == 0:
            return categories

        for c in query:
            ctg = Model_Category(*c)
            categories.append(ctg.to_dict())
        return categories

class Venue:
    @staticmethod
    async def create(name,slug,thumb,status,*args):
        query = DatabaseManager.insert(f"insert into venues (name,slug,images,status) values('%s','%s','%s','%s')"%(name,slug,thumb,status))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from venues where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        category = Model_Venue(*query[0])

        return category.to_dict()
    
    @staticmethod
    async def get_all():
        venues = []
        query = await DatabaseManager.query(f"select * from venues order by id desc")
        if query == None or len(query) == 0:
            return venues

        for c in query:
            ctg = Model_Venue(*c)
            venues.append(ctg.to_dict())
        return venues


class Commission:
    @staticmethod
    async def create(name,*args):
        query = DatabaseManager.insert(f"insert into commissions (name) values('%s')"%(name))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from commissions where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        tax = Model_Commission(*query[0])

        return tax.to_dict()
    
    @staticmethod
    async def get_all():
        commissions = []
        query = await DatabaseManager.query(f"select * from commissions order by id desc")
        if query == None or len(query) == 0:
            return commissions

        for c in query:
            ctg = Model_Commission(*c)
            commissions.append(ctg.to_dict())
        return commissions

class Tax:
    @staticmethod
    async def create(name,rate_type,rate,net_price,status,admin_tax):
        query = DatabaseManager.insert(f"insert into taxes (name,rate_type,rate,net_price,status,admin_tax) values('%s','%s','%s','%s','%s','%s')"%(name,rate_type,rate,net_price,status,admin_tax))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from taxes where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        tax = Model_Tax(*query[0])

        return tax.to_dict()
    
    @staticmethod
    async def get_all():
        taxes = []
        query = await DatabaseManager.query(f"select * from taxes order by id desc")
        if query == None or len(query) == 0:
            return taxes

        for c in query:
            ctg = Model_Tax(*c)
            taxes.append(ctg.to_dict())
        return taxes


class Contact:
    @staticmethod
    async def create(name,*args):
        query = DatabaseManager.insert(f"insert into contacts (name) values('%s')"%(name))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from contacts where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        tax = Model_Contact(*query[0])

        return tax.to_dict()
    
    @staticmethod
    async def get_all():
        contacts = []
        query = await DatabaseManager.query(f"select * from contacts order by id desc")
        if query == None or len(query) == 0:
            return contacts

        for c in query:
            ctg = Model_Contact(*c)
            contacts.append(ctg.to_dict())
        return contacts


class Banner:
    @staticmethod
    async def create(name,sub_title,thumb,button_url,button_title,order_no,status):
        query = DatabaseManager.insert(f"insert into banners (name,sub_title,image,button_url,button_title,order_no,status) values('%s','%s','%s','%s','%s','%s','%s')"%(name,sub_title,thumb,button_url,button_title,order_no,status))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from banners where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        tax = Model_Banner(*query[0])

        return tax.to_dict()
    
    @staticmethod
    async def get_all():
        banners = []
        query = await DatabaseManager.query(f"select * from banners order by id desc")
        if query == None or len(query) == 0:
            return banners

        for c in query:
            ctg = Model_Banner(*c)
            banners.append(ctg.to_dict())
        return banners


class Post:
    @staticmethod
    async def create(name,slug,thumb,body,excerpt,status,category_id,featured,meta_description,meta_keywords,seo_title):
        query = DatabaseManager.insert(f"insert into posts (name,slug,iamge,body,excerpt,status,category_id,featured,meta_description,meta_keywords,seo_title) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,slug,thumb,body,excerpt,status,category_id,featured,meta_description,meta_keywords,seo_title))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from posts where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        tax = Model_Post(*query[0])

        return tax.to_dict()
    
    @staticmethod
    async def get_all():
        posts = []
        query = await DatabaseManager.query(f"select * from posts order by id desc")
        if query == None or len(query) == 0:
            return posts

        for c in query:
            ctg = Model_Post(*c)
            posts.append(ctg.to_dict())
        return posts


class Page:
    @staticmethod
    async def create(name,slug,thumb,excerpt,body,meta_description,meta_keywords,status):
        query = DatabaseManager.insert(f"insert into pages (name,slug,image,excerpt,body,meta_description,meta_keywords,status) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(name,slug,thumb,excerpt,body,meta_description,meta_keywords,status))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from pages where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        tax = Model_Page(*query[0])

        return tax.to_dict()
    
    @staticmethod
    async def get_all():
        pages = []
        query = await DatabaseManager.query(f"select * from pages order by id desc")
        if query == None or len(query) == 0:
            return pages

        for c in query:
            ctg = Model_Page(*c)
            pages.append(ctg.to_dict())
        return pages


class Tag:
    @staticmethod
    async def create(name,thumb,type,sub_title,website,is_page,description,phone,email,status):
        query = DatabaseManager.insert(f"insert into tags (name,image,type,sub_title,website,is_page,description,phone,email,status) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,thumb,type,sub_title,website,is_page,description,phone,email,status))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from tags where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        tag = Model_Tag(*query[0])

        return tag.to_dict()
    @staticmethod
    async def find_slug(title):
        query = await DatabaseManager.query(f"select * from tags where slug like '%s'"%("%"+title+"%"))
        if query == None or len(query) == 0:
            return None
        tag = Model_Tag(*query[0])

        return tag.to_dict()
    
    @staticmethod
    async def get_all():
        tags = []
        query = await DatabaseManager.query(f"select * from tags order by id desc")
        if query == None or len(query) == 0:
            return tags

        for c in query:
            ctg = Model_Tag(*c)
            tags.append(ctg.to_dict())
        return tags


class Booking:
    @staticmethod
    async def create(name,*args):
        query = DatabaseManager.insert(f"insert into bookings (name) values('%s')"%(name))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from bookings where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        booking = Model_Booking(*query[0])

        return booking.to_dict()
    
    @staticmethod
    async def get_all():
        bookings = []
        #return []
        query = await DatabaseManager.query(f"select * from bookings order by id desc")
        if query == None or len(query) == 0:
            return bookings

        for c in query:
            ctg = Model_Booking(*c)
            bookings.append(ctg.to_dict())
        return bookings

class Event:
    @staticmethod
    async def create(name,*args):
        query = DatabaseManager.insert(f"insert into events (name) values('%s')"%(name))
        if query and query == True:
            return True
        return None
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from events where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        event = Model_Event(*query[0])

        return event.to_dict()
    
    @staticmethod
    async def find_slug(title):
        query = await DatabaseManager.query(f"select * from events where slug like '%s'"%("%"+title+"%"))
        if query == None or len(query) == 0:
            return None
        event = Model_Event(*query[0])

        return event.to_dict()
    
    @staticmethod
    async def get_all():
        events = []
        query = await DatabaseManager.query(f"select * from events order by id desc")
        if query == None or len(query) == 0:
            return events

        for c in query:
            ctg = Model_Event(*c)
            events.append(ctg.to_dict())
        return events

class User:
    @staticmethod
    async def find(id):
        query = await DatabaseManager.query(f"select * from users where id=%d"%(id))
        if query == None or len(query) == 0:
            return None
        user = Model_User(*query[0])

        return user.to_dict()
    @staticmethod
    async def get_all():
        users = []
        query = await DatabaseManager.query(f"select * from users order by id desc")
        if query == None or len(query) == 0:
            return users

        for c in query:
            ctg = Model_User(*c)
            users.append(ctg.to_dict())
        return users
    @staticmethod
    async def get_orders(user_id):
        return await Order.get_orders(user_id)
    @staticmethod
    async def update_profile(user_id,keys,values):
        query = await DatabaseManager.update(f"update user_profile set (%s) values(%s) where user_id=%d"%(keys,values,user_id))
        if newquery:
            profile = await User.get_profile(user_id)
            return profile
        else:
            return None
    @staticmethod
    async def get_profile(user_id,payment_methods=None,companies=None,count=1):
        if count > 2:
            return None
        query = await DatabaseManager.query(f"SELECT * from user_profile where user_id=%s"%user_id)
        if query:
            profile = Profile(*query[0],payment_methods=payment_methods,companies=companies)
            profile = profile.to_dict()
            return profile
        else:
            query = DatabaseManager.insert(f"INSERT INTO user_profile (user_id,interests) VALUES (%d, 'all')"%user_id)
            profile = await User.get_profile(user_id,payment_methods=payment_methods,companies=companies,count=count+1)
            return profile
            
    @staticmethod
    async def create(name,email,password):
       
        query = await DatabaseManager.query(f"select * from users where email='%s'"%email)
        if query and len(query) > 0:
            return {'message':'User with email already exists','status': 1}
        
        new = DatabaseManager.insert(f"insert into users (name,email,password,group_id,user_id) values('%s','%s','%s',%d,'0')"%(name,email,password,3))
        if new and new == True:
            
            #profile = DatabaseManager.insert(f"insert into user_profile (user_id,address,fullname,gender,language,interests) values('%s','%s','%s','%s','English','all')"%(new[0],address,fullname,gender))
            return {'message':'New User account created, login to continue','status': 0} 
        else:
            return {'message':'Error inserting record, try again','status': 1}
    @staticmethod
    async def validate(username,password):
        code = random.randint(1001,9999)
        query = await DatabaseManager.query(f"SELECT * from users where email='%s'" % (username))
        if query == None or len(query) == 0:
            return None
        user = query[0]
        profile = None
        if user[0]:
            profile = await DatabaseManager.query(f"SELECT * from user_profile where user_id=%d"%user[0])
            if profile == None or len(profile) == 0:
                new_profile = DatabaseManager.insert(f"INSERT INTO user_profile (user_id,interests) VALUES (%d,'all')"%user[0])
                if new_profile:
                    profile = await DatabaseManager.query(f"SELECT * from user_profile where user_id=%d"%user[0])
                    if profile:
                        profile = profile[0] if isinstance(profile,tuple) else ()
        #newquery = DatabaseManager.update(f"UPDATE users set login_code='%s' where id=%d"%(code,user[0]))
        #if newquery == None or newquery == False:
        #    return None
        #if profile:
        #    profile = Profile(*profile)
        #    profile = profile.to_dict()
            print("validate",password==str(user[5]),str(user[4])==password,password,user[5])
            if str(user[5]) == str(password) or str(user[4]) == str(password):
                result = Model_User(*user)
                return result.to_dict()
            else:
                return {'user_id':None,'message':'Invalid Credentials passed'}
        else:
            return {'user_id':None,'message':'User not found'}
    @staticmethod
    async def getCode(user_id):
        query = await DatabaseManager.query(f"SELECT login_code,mobile,email,id from users where email='%s' or mobile='%s' or username='%s'" % (user_id,user_id,user_id))
        if query == None or len(query) == 0:
            return None
        query = query[0]
        code = query[0]
        if query:
            new_code = random.randint(1001,9999)
            newquery = DatabaseManager.update(f"UPDATE users set login_code='%s' where id=%d"%(new_code,query[3]))
            print("update",newquery)
            if newquery == None:
                return None
            code = new_code
        mobile = query[1]
        email = query[2]
        newcode = ''
        for i in str(code):
            newcode = ""+i
        return {'code':code,'mobile':mobile,'email':email}
    @staticmethod
    async def set_pickup(user_id,company):
        query = DatabaseManager.update(f"update user_profile set delivery_company='%s' where user_id=%d"%(company['company'],user_id))
        if query == None:
            return None
        return query


class Settings:
    @staticmethod
    async def create(bg_image=None,loader=None,icon_image=None,logo=None,site_favicon=None):
        query = await DatabaseManager.query(f"select from settings where id=1")
        if query == None or len(query) == 0:
            new_q = DatabaseManager.insert("insert into settings (id,company_name) values(1, 'EVENT')")
            if new_q and new_q != True:
                return None
        if bg_image:
            query = DatabaseManager.update(f"update settings set bg_image = '%s' where id=1"%(bg_image))
            if query and query != True:
                return None
        if loader:
            query = DatabaseManager.update(f"update settings set loader = '%s' where id=1"%(loader))
            if query and query != True:
                return None
        if icon_image:
            query = DatabaseManager.update(f"update settings set icon_image = '%s' where id=1"%(icon_image))
            if query and query != True:
                return None
        if logo:
            query = DatabaseManager.update(f"update settings set logo = '%s' where id=1"%(logo))
            if query and query != True:
                return None
        if site_favicon:
            query = DatabaseManager.update(f"update settings set site_favicon = '%s' where id=1"%(site_favicon))
            if query and query != True:
                return None

        return True
        