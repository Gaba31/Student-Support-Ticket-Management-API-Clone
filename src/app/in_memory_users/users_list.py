from app.schemas.user import Users
u1 = Users(

    user_id= "EC089",
    user_name="SID",
    password="sid1234"
)

u2 = Users(
    user_id= "CS058",
    user_name="AVI",
    password="avi1234"
)

a1 = Users(
    user_id = "BS012",
    user_name = "SAM",
    password =  "sam4321"
)

a2 = Users(
    user_id ="GB892",
    user_name = "JAM",
    password = "Jam8900"
)


def get_admin_user_list():
    return a1,a2

def get_user_list():
    return u1,u2

if __name__=="__main__":
    
    for u in get_user_list():
        print("="*30)
        print(u.user_id)
        print(u.user_name)
        print(u.password)

