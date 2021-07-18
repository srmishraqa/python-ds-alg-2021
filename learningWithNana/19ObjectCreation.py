#  we are creating Object of the class in different file
#  we need to call the name of the class like functions with passing params
# we need to call the constructor and need to assign a obj ref variable

from user import User
from post import Post

app_user_one = User("soumya.mishra@email.com", "Soumya Mishra", "TestPassword", "Senior Test Engineer")
app_user_one.get_user_info()
print("-------------------")
app_user_one.change_job_title("Lead Test Engineer")

# print(type(app_user_one))
app_user_one.get_user_info()
print("-------------------")

app_user_two = User("raman.raghav@email.com", "Raman Raghav", "pwd1", "Associate Test Manager")
app_user_two.get_user_info()
print("-------------------")

# here we have assigned one object prop as a param to another constructor
first_post = Post('"Secret Mission to Mars"', app_user_two.name)
first_post.get_post_info()

# every data type in python is an object
# like <class 'str'> for string
