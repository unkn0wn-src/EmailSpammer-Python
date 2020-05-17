from threading import Thread
import smtplib

class EmailSpammer:

    def __init__(self, acc_file_name, target_email, subjects, message):
        self.acc_file_name = acc_file_name
        self.target_email = target_email
        self.subjects = subjects
        self.message = message
        self.accounts = []

    def spam(self):
        i = 0
        
        for subject in self.subjects:
            acc_file = open(self.acc_file_name, 'r')
            for line in acc_file.readlines():
                line = line.replace('\n', '')

                user = line.split(";")[0]
                pwd = line.split(";")[1]

                try:
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login(user, pwd)

                    message = 'Subject: {}\n\n{}'.format(subject, self.message)

                    server.sendmail(pwd, self.target_email, message)
                    server.quit()

                    print("[+] Succesfully sent an email")

                    i += 1
                except:
                    print("[-] An error occurred")
                    
            acc_file.close()
        print("[!] Es wurden " + str(i) + " E-Mails gesendet")

if __name__ == "__main__":
    email_spammer = EmailSpammer("Google-Accounts.txt", "TARGET EMAIL", ["SUBJECT1", "SUBJECT2"], "MESSAGE")
    email_spammer.spam()
