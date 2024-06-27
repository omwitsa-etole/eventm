
class Model_Category:
    def __init__(self,id,name,slug,image,status,created_at,deleted_at):
        self.id = id
        self.name = name
        self.status = 'Enabled' if status == 1 else 'Disabled'
        self.image = image
        self.created_at = created_at
        self.slug = slug
    def to_dict(self):
        return self.__dict__

class Model_Venue:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__
class Model_Commission:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_Tax:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_Contact:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_Banner:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.sub_title = args[2]
        self.image = args[3]
    def to_dict(self):
        return self.__dict__

class Model_Page:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_Tag:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__


class Model_Booking:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_Event:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_Post:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_User:
    def __init__(self,id,company,username,mobile,password,login_code,group,email,last_login,previous_login,login_hash,user_id,created_at,updated_at,deleted):
        self.id = id
        self.username = username
        self.mobile = mobile
        self.password = password
        self.group = group
        self.email = email
    def to_dict(self):
        return self.__dict__

class Payments:
    def __init__(self,id,code,name,enabled,company,default,created_at,updated,deleted,user):
        self.id = id
        self.code = code
        self.name = name
        self.enabled = bool(enabled)
        self.company = company
        self.user = user
    def to_dict(self):
        return self.__dict__

class Profile:
    def __init__(self,id,user_id,fullname,age,gender,address,avatar,language,payment,intersets,price_range,created,updated,delivery_address,payment_methods=None,companies=None):
        self.id = id
        self.user_id = user_id
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.address = address
        self.created_at = created
        self.avatar = avatar
        self.default_payment = payment
        self.language = language
        self.intersets = intersets.split(",")
        self.price_range = price_range.split(",")
        self.delivery_address = delivery_address
        self.delivery_company = int(delivery_address) if  delivery_address else None
        if companies:
            for c in companies:
                if c['company'] == self.delivery_company or c['id'] == self.delivery_company:
                    self.delivery_company = c['name']
        if payment_methods:
            for i in payment_methods:
                if i['id'] == self.default_payment:
                    self.default_payment = i['name']
    def to_dict(self):
        return self.__dict__
