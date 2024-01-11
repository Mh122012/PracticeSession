# Deadlock is a long Waiting State
# its is occures due to  Holding the process by one or other Device for a while at the time of DB connections ,API creation like this
#Finally close the opened resource or connections of DB after exxeption occure during session
# Syntax:
'''def FunctionName():
     try:
         risky code
     except:
         Handling code
     finally:
         cleanup code'''

class Naamkaran():
    def __init__(self,fname,lname,domain):
        self.fname=fname
        self.lname=lname
        self.domain=domain
    def show(self):
        try:
            if self.domain == "@gmail.com":
                name = (("{}_{}.{}").format(self.fname, self.lname, self.domain))
                print(name)
            else:
                raise Exception("Domain must be @gmail.com")

        except Exception as msg:

                print('ValueError::',msg)

        finally:
                print("Thank you to visit")

obj=Naamkaran("Hemant","Mali","@gmail.com")
obj.show()

