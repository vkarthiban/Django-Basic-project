from django.db import models

# Create your models here.
class travelPlaces1(models.Model):
    
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    imgurl = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class info(models.Model):
    
    pintrest = models.CharField(max_length=100)
    twitter = models.CharField(max_length=250)
    fb = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    mail = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    landline = models.CharField(max_length=250)
    mobileno = models.CharField(max_length=250)
    offmail = models.CharField(max_length=250)
    dribbble = models.CharField(max_length=250)
    behance = models.CharField(max_length=250)

class subscribe(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)

class message(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()


class trip(models.Model):
    placeimg = models.ImageField(default="")
    city = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    budget =models.IntegerField()

class aboutus(models.Model):
    #few words about us
    content = models.TextField()
    subcontent = models.TextField()
    about_image = models.ImageField()
    #####
    onlinecourses = models.IntegerField()
    student = models.IntegerField()
    teachers = models.IntegerField()
    countries = models.IntegerField()
    ########meet the team######
class team(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    descripition = models.CharField(max_length=100)

class news(models.Model):
    imagesrc = models.ImageField()
    date = models.DateField()
    aboutlink = models.TextField(default="")
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()



#     def total(self):
#         val = {
#             'title' :'ketharnath',
#             'subtitle' : 'shivantemple',
#             'imgurl' : 'destination_3.jpg',
#             'price' :'7000'
#         }
#         # print("................................",val)
#         return val
#     def info(self):
#         data = {
#             'pintrest':'https://in.pinterest.com/',
#             'twitter' : 'https://twitter.com/',
#             'fb':'https://www.facebook.com/',
#             'linkedin':'https://www.linkedin.com/',
#             'mail':'www.gmail.com',
#             'address':'jio flat,mubai street india',
#             'landline':'+44 5567 32 664 567',
#             'mobileno':'+44 5567 89 3322 332',
#             'offmail':'Office@yourbusinessname.com',
#             'dribbble':'https://dribbble.com/',
#             'behance':'https://www.behance.net/',
#         }
#         return data

# class travelPlaces2(models.Model):

#     title = 'thiruvanamali'
#     subtitle = 'shivan temple'
#     imgurl = 'destination_2.jpg'
#     price = '7000'
    

# class travelPlaces3(models.Model):
    
#     title = 'combodia'
#     imgurl = 'destination_1.jpg'
#     subtitle = 'angkor wat'
#     price = '700'