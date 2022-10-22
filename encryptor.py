from tkinter import *
import smtplib, ssl
from tkinter import messagebox

#This fuction encrypts text from window.Tk()
def encrypt():
      T2.delete('1.0', END) #deletes what is in the output box
      start = (str(T.get('1.0', END))).upper() #the input
      key = (str(code.get)).upper() #the key
      end = [] #the output

      #this encrypts each letter of the input
      for i in range(len(start)-1): 
            if ord(start[i]) == 32: #the if-else statements are so it doesn't encrypt symbols
                  end.append(chr(32))
            elif ord(start[i]) == 46:
                  end.append(chr(46))
            elif ord(start[i]) == 44:
                  end.append(chr(44))
            else:
                  letter = (ord(start[i])) + (ord(key[i]))
                  letter = letter % 26
                  letter = letter + 65
                  end.append(chr(letter))
                  letter = 0
 
      result = "" . join(end) #forms result
      T2.insert(END, result) #outputs result

#This fuction decrypts text from window.Tk()
def decrypt():
      T2.delete('1.0', END)#deletes what is in the output box
      start =(str(T.get('1.0', END))).upper()#the input
      key = (str(code.get)).upper()#the key
      end = []#the output

      #this decrypts each letter of the input
      for i in range(len(start)-1): #the if-else statements are so it doesn't decrypt symbols
            if ord(start[i]) == 32:
                  end.append(chr(32))
            elif ord(start[i]) == 46:
                  end.append(chr(46))
            elif ord(start[i]) == 44:
                  end.append(chr(44))
            else:
                  letter = (ord(start[i])) - (ord(key[i]) + 26)
                  letter = letter % 26
                  letter = letter + 65
                  end.append(chr(letter))
                  letter = 0
      result = "" . join(end) #forms result
      T2.insert(END, result)#outputs result

#takes encryption/decryption and sends it over email
def mail():

      def send():
            port = 465  
            smtp_server = "smtp.gmail.com"
            
            #gets data from user
            sender = str(user.get())
            receiver = str(re.get())
            password = str(pw.get())
            

            message = str(T2.get('1.0', END)) #prepares message

            #sends meesage with smtp library
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                  server.login(sender, password)
                  server.sendmail(sender, receiver, message)

                  
            messagebox.showinfo("SENT", "Your Message Was Sent")#tells you message was sent
            email.destroy() #closes eamil window


      #this set up the email window, such as text, entry boxes, buttons, and styles them with fonts, colors, and locations
      email = Tk()
      email.geometry("920x150")
      email.config(background="#dff6f0")
      email.title("SEND EMAIL")
      Label(email, text = 'SEND EMAIL',font=("Helvetica",36,"bold"),background="#dff6f0").grid(row=0, column = 0,columnspan = 4, pady = 10)
      user = Entry(email, width = 50)
      user.grid(row=1, column= 1)
      Label(email, text = 'YOUR EMAIL:',font=("Helvetica",11),background="#dff6f0").grid(row=1, column = 0, sticky = E)
      pw = Entry(email,  width = 50)
      pw.grid(row=2, column= 1)
      Label(email, text = 'YOUR PASSWORD:',font=("Helvetica",11),background="#dff6f0").grid(row=2, column = 0)
      re = Entry(email,  width = 50)
      re.grid(row=1, column=3)
      Label(email, text = 'RECEIVER EMAIL:',font=("Helvetica",11),background="#dff6f0").grid(row=1, column = 2)
      Button(email, text= 'SEND', command = send,font=("Helvetica",11), bg = '#46b3e6', fg = "white",relief = "solid",  bd =1).grid(row=2,column=3)
      
      email.mainloop()      
      
      
#this set up the main window, such as text, entry boxes, buttons, and styles them with fonts, colors, and locations
window = Tk()
window.geometry("700x450")
window.title("ENCRYPTION")
window.config(background="#dff6f0")

Label(window, text = 'Encryption',font=("Helvetica",36,"bold"),background="#dff6f0").grid(row=0, column = 0,columnspan = 5)
Label(window, text = 'INPUT',font=("Helvetica",18),background="#dff6f0").grid(row=2, column = 0,columnspan = 2)
T = Text(window, height=12, width=35)
T.grid(row=3, column= 0, padx=10,pady=10, rowspan=2, columnspan = 2)
Label(window, text = 'OUTPUT',font=("Helvetica",18),background="#dff6f0").grid(row=2, column = 3,columnspan = 2)
T2 = Text(window, height=12, width=35)
T2.grid(row=3, column= 3, padx=10,pady=10,rowspan=2, columnspan = 2)
Button(window, text= 'ENCRYPT', command = encrypt,font=("Helvetica",11), bg = '#46b3e6', fg = "white",relief = "solid",  bd =1).grid(row=3,column=2)
Button(window, text= 'DECRYPT', command = decrypt,font=("Helvetica",11), bg = '#46b3e6', fg = "white",relief = "solid",  bd =1).grid(row=4,column=2)
code = Entry(window)
code.grid(row = 5, column =1, sticky = W)
Label(window, text = 'Encryption Key:',font=("Helvetica",11),background="#dff6f0").grid(row=5, column = 0, sticky = E)
Button(window, text= 'SEND EMAIL', command = mail,font=("Helvetica",11), bg = '#46b3e6', fg = "white",relief = "solid",  bd =1).grid(row=5,column=3,columnspan = 2, pady = 10)
window.mainloop()