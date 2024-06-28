
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
        self.name = args[1]
        self.slug = args[2]
        self.images = args[3]
        self.description = args[4]
        self.venue_type = args[5]
        self.seated_guestnumber = args[6]
        self.standing_guestnumber = args[7]
        self.contact_email = args[8]
        self.ammenities = args[9]
        self.neighbourhoods = args[10];self.availability = args[11]
        self.food = args[12];self.country = args[13];self.address = args[14]
        self.city = args[15];self.state = args[16];self.zip_code = args[17]
        self.show_quoteform = True if args[18] == 1 else False
        self.updated_at = args[-3]
        self.created_at = args[-2];self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__
class Model_Commission:
    def __init__(self,*args):
        self.id = args[0]
    def to_dict(self):
        return self.__dict__

class Model_Tax:
    def __init__(self,*args):
        self.id = args[0];self.name = args[1];sel.rate_type = args[2]
        self.rate = args[3];self.net_price = args[4];self.status = True if args[5] == 1 else False
        self.admin_tax = True if args[6] == 1 else False
        self.updated_at = args[-3];self.created_at = args[-2];self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__

class Model_Contact:
    def __init__(self,*args):
        self.id = args[0];self.name =args[1];self.email=args[2]
        self.title = args[3];self.updated_at = args[4];self.created_at=args[6]
        self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__

class Model_Banner:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.sub_title = args[2]
        self.image = args[3]
        self.button_url = args[4]
        self.button_title = args[5]
        self.order_no = args[6]
        self.status = 'Enabled' if args[7] == 1 else 'Disabled'
        self.updated_at = args[8]
        self.created_at = args[9]
        self.deleted = args[-1]
    def to_dict(self):
        return self.__dict__

class Model_Page:
    def __init__(self,*args):
        self.id = args[0];self.name = args[1];self.slug=args[2]
        self.image = args[3];self.excerpt = args[4];self.body =args[5]
        self.meta_description = args[6],self.meta_keywords = args[7],
        self.status = True if args[8] == 1 else False
        self.updated_at = args[-3];self.created_at = args[-2];
        self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__

class Model_Tag:
    def __init__(self,*args):
        self.id = args[0];self.name=args[1];self.image=args[2];self.type=args[3]
        self.sub_title = args[4];self.website=args[6]
        self.is_page = True if args[7] == 1 else False
        self.description = args[8];self.phone=args[9];self.email=args[10]
        self.status = True if args[11] == 1 else False
        self.facebook = args[12];self.instagram=args[13];self.twitter=args[14];self.linkedin=args[15]
        self.updated_at = args[-3];self.created_at = args[-2]
        self.deleted_at = args[-1]  
    def to_dict(self):
        return self.__dict__


class Model_Booking:
    def __init__(self,*args):
        self.id = args[0];self.order_number=args[1]
        self.event_id = args[2];self.ticket_id =args[3];self.quantity=args[4]
        self.net_price = float(args[5]);self.customer_email=args[6]
        self.booking_cancel = True if args[7] == 1 else False
        self.status = True if args[7] == 1 else False
        self.created_at = args[8];self.checked_in = True if args[9] == 1 else False
        self.payment_type = args[10]
        self.is_paid = True if args[11] == 1 else False
        self.expired = True if args[12] == 1 else False
        self.updated_at = args[-2]
        self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__

class Model_EventTicket:
    def __init__(self,*args):
        self.id = args[0]
        self.event_id = args[1]
        self.ticket_name = args[2]
        self.ticket_price = args[3]
        self.ticket_quantity = args[4]
        self.customer_limit = args[5]
        self.ticket_description = args[6]
        self.created_at = args[-3]
        self.updated_at = args[-2]
        self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__
class Model_Event:
    def __init__(self,*args):
        self.id = args[0]
        self.name = args[1]
        self.organiser_id = args[2];self.category_id = args[3];self.slug = args[4]
        self.excerpt = args[5];self.description=args[6];self.faq = args[7];self.offline_payment_instruction = args[8]
        self.featured = args[9];self.status = args[10];self.start_date = args[11];self.start_time=args[12];self.end_date = args[13]
        self.end_time = args[14];self.repetitive = True if args[15] == 1 else False;self.online_event = True if args[16] == 1 else False;self.venue_id = args[17]
        self.video_link = args[18];self.thumb_image=args[19];self.poster_image = args[20]
        self.images  = args[21]
        self.meta_title = args[22];self.meta_description = args[23];self.meta_keywords = args[24];self.tags = args[25]
        self.updated_at = args[-3];self.created_at = args[-2];self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__

class Model_Post:
    def __init__(self,*args):
        self.id = args[0];self.name=args[1];self.slug=args[2]
        self.image = args[3];self.excerpt=args[4];self.category_id = args[5]
        self.featured = args[6];self.body=args[7];self.meta_description = args[8]
        self.meta_keywords = args[9];self.status = args[10];self.seo_title = args[11]
        self.updated_at = args[-3];self.created_at = args[-2];self.deleted_at = args[-1]
    def to_dict(self):
        return self.__dict__

class Model_User:
    def __init__(self,id,company,username,mobile,password,login_code,group,email,last_login,previous_login,login_hash,user_id,created_at,updated_at,deleted):
        self.id = id
        self.name = username
        self.mobile = mobile
        self.password = password
        self.group = group
        self.email = email
        self.created_at = created_at
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
