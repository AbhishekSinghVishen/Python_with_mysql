from dbhelper import DBhelper
def main():
    while True:
        db=DBhelper()
        print("*************WELCOME*************")
        print()
        print()
        print("Press 1 to insert new user")
        print("Press 2 to fetch details of user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to print csv file")
        print("Press 6 to exit program")

        
        try:
            print()
            print()
            choice=int(input())
            if (choice==1):
                uid=int(input("enter user id: "))
                uname=input("enter username: ")
                uphone=input("enter userphone: ")
                db.insert_user(uid,uname,uphone)
            elif choice==2:
                db.fetch_all()
             
            elif choice==3:
                uid=int(input("enter user id to be deleted: ")) 
                db.delete_user(uid)
            elif choice==4:
                uid=int(input("enter user id to be updated: "))
                uname=input("new name: ")
                uphone=input("new phone: ")
                db.update_user(uid,uname,uphone)
            elif choice==5:
                db.extract_csv()
            elif choice==6:
                break
            else:
                print("Invalid Input Try again")
                print()
                print()
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")
            print()
            print()
if __name__ =="__main__":
    main()