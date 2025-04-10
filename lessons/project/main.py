import pandas as pd
from mailer import connect_to_smtp, send_email
from plot import plot_age_income_purchase_scatter
from prediction import predict_for_new_customer, tranform_new_customer

# load data
filepath = "./lessons/files/insurance_data.csv"
df = pd.read_csv(filepath)

# plot
save_to_path = "./lessons/files/insurance_data_plot.png"
plot_age_income_purchase_scatter(df, save_to_path)

# prediction
new_customer = {
    "Age": 34,
    "Income": 75000,
    "JobType": "Employee",
    "ExistingInsurance": "No",
}
tranformed_new_customer = tranform_new_customer(
    new_customer,
    job_encoder=job_encoder,
    insurance_encoder=insurance_encoder,
)
prediction_result = predict_for_new_customer(new_customer)

# send mail
sender_email = "your_email@gmail.com"
sender_password = "your_app_password"
smtp_server = "smtp.gmail.com"
smtp_port = 587
server = connect_to_smtp(smtp_server, smtp_port, sender_email, sender_password)

send_email(
    server=server,
    sender_email=sender_email,
    to_emails=["recipient@example.com"],
    subject="Test Email with Attachments",
    body_text="This is a test email with attachments.",
    body_html="<html><body><h1>Test Email</h1><p>This is a <b>test email</b>.</p></body></html>",
    cc_emails=["cc_recipient@example.com"],
    bcc_emails=["bcc_recipient@example.com"],
    attachments=["path/to/your/file.pdf"],
)
server.quit()
