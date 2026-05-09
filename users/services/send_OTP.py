import smtplib
from email.message import EmailMessage
import secrets
from celery import shared_task

@shared_task
def send_otp_service(email,username,request):

    msg = EmailMessage()
    msg["Subject"] = "OTP to reset password"
    msg["From"] = "amalskumarofficialz@gmail.com"
    msg["To"] = email

    otp = secrets.randbelow(900000) + 100000

    html = """<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Reset Your Velora Password</title>
                <!-- We link the fonts, though some email clients will fallback to Arial/sans-serif -->
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Caveat+Brush&family=Plus+Jakarta+Sans:wght@500;700;900&display=swap" rel="stylesheet">
                <style>
                    /* Base resets for email clients */
                    body, table, td, a { -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }
                    table, td { mso-table-lspace: 0pt; mso-table-rspace: 0pt; }
                    img { -ms-interpolation-mode: bicubic; border: 0; height: auto; line-height: 100%; outline: none; text-decoration: none; }
                    body { margin: 0; padding: 0; width: 100% !important; }
                </style>
            </head>
            <body style="background-color: #fffdf8; margin: 0; padding: 40px 20px; font-family: 'Plus Jakarta Sans', Arial, sans-serif; color: #000000;">

                <!-- Wrapper Table for centering -->
                <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; margin: 0 auto;">
                    <tr>
                        <td align="center">
                            
                            <!-- Neo-Brutalist Card -->
                            <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #ffffff; border: 4px solid #000000; border-radius: 24px; box-shadow: 8px 8px 0px 0px #000000; overflow: hidden;">
                                
                                <!-- Header Area (Yellow) -->
                                <tr>
                                    <td align="center" style="background-color: #ffc86b; border-bottom: 4px solid #000000; padding: 30px 20px;">
                                        <h1 style="margin: 0; font-family: 'Caveat Brush', cursive, Arial, sans-serif; font-size: 36px; font-weight: normal; letter-spacing: 2px; color: #000000;">
                                            VELORA
                                        </h1>
                                    </td>
                                </tr>

                                <!-- Body Content -->
                                <tr>
                                    <td align="center" style="padding: 40px 30px;">
                                        
                                        <h2 style="margin: 0 0 15px 0; font-size: 24px; font-weight: 900; color: #000000;">
                                            Password Reset Request
                                        </h2>
                                        
                                        <p style="margin: 0 0 30px 0; font-size: 16px; font-weight: 500; color: #4b5563; line-height: 1.5;"> """

    html = html + f"Hello, {username}"
                                            
    html = html + """<br><br>
                                            We received a request to reset the password for your Velora account. Enter the OTP code below to verify your identity and create a new password.
                                        </p>

                                        <!-- OTP Box -->
                                        <table border="0" cellpadding="0" cellspacing="0" style="margin: 0 auto;">
                                            <tr>
                                                <td align="center" style="background-color: #f9f6f0; border: 3px solid #000000; border-radius: 16px; padding: 20px 40px; box-shadow: 6px 6px 0px 0px #ffc86b;">
                                                    <span style="font-size: 42px; font-weight: 900; letter-spacing: 12px; color: #000000; display: block; margin-right: -12px;">"""
    html = html + f"{otp}"
    
    html = html + """ </span>
                                                </td>
                                            </tr>
                                        </table>

                                        <p style="margin: 30px 0 0 0; font-size: 14px; font-weight: 700; color: #000000;">
                                            This code will expire in 10 minutes.
                                        </p>

                                    </td>
                                </tr>

                                <!-- Footer Warning -->
                                <tr>
                                    <td align="center" style="background-color: #f9f6f0; border-top: 3px solid #000000; padding: 20px 30px;">
                                        <p style="margin: 0; font-size: 12px; font-weight: 500; color: #6b7280; line-height: 1.5;">
                                            If you did not request a password reset, you can safely ignore this email. Your account is secure.
                                        </p>
                                    </td>
                                </tr>

                            </table>

                            <!-- Bottom Copyright -->
                            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                <tr>
                                    <td align="center" style="padding: 20px 0;">
                                        <p style="margin: 0; font-size: 12px; font-weight: 700; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px;">
                                            &copy;2026 Velora Digital Art
                                        </p>
                                    </td>
                                </tr>
                            </table>

                        </td>
                    </tr>
                </table>

            </body>
            </html>"""

    msg.set_content("Fallback text version")
    msg.add_alternative(html, subtype="html")

    # SMTP connection
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    username = "amalskumarofficialz@gmail.com"
    password = "ttki xaro pyao fjfz"   

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()            
        server.login(username, password)
        server.send_message(msg)

    request.session["otp"] = otp