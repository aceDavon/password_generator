import smtplib


def send_mail(username, password, host, destination, subj, msg):
    try:
        with smtplib.SMTP(host) as connection:
            connection.starttls()
            connection.login(username, password)
            connection.sendmail(from_addr=username,
                                to_addrs=destination,
                                msg=f"Subject:{subj} \n\n {msg}")
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")
