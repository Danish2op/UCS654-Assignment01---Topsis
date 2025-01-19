import streamlit as st
import pandas as pd
from topsis102203633Danishsharma_core.topsis import Topsis
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(receiver_email, file_path):
    """Send email with attachment."""
    sender_email = "advancetopsis@gmail.com"  # Your email
    sender_password = "dsyt zldb djmp mbtr"  # App password (not your main email password)

    # Email setup
    subject = "Your TOPSIS Results"
    body = "Attached is the result of your TOPSIS analysis."

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach file
    filename = os.path.basename(file_path)
    with open(file_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)

    # Connect to Gmail server and send email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            st.success(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

def main():
    st.title("TOPSIS Analysis App")

    st.write("Upload your dataset and configure the parameters below:")

    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded data:")
        st.dataframe(df)

        # User inputs
        weights = st.text_input("Enter weights (comma-separated, e.g., 0.25,0.25,0.25,0.25):")
        impacts = st.text_input("Enter impacts (comma-separated, e.g., +,+,-,+):")

        missing_data_strategy = st.selectbox(
            "Select the method to handle missing data:",
            ("mean", "median", "ffill", "bfill", "interpolate_linear","interpolate_polynomial")
        )

        distance_metric = st.selectbox(
            "Select the distance metric for TOPSIS:",
            ("euclidean", "manhattan", "chebyshev", "minkowski", "cosine")
        )

        show_parameters = st.checkbox("Show all parameters", value=False)

        reverse_rank = st.checkbox("Reverse rank order", value=False)

        email = st.text_input("Enter your email address:")

        # Run TOPSIS and send results
        if st.button("Submit"):
            try:
                # Validate inputs
                if not weights or not impacts:
                    st.error("Please enter valid weights and impacts.")
                    return

                weights = list(map(float, weights.split(',')))
                impacts = impacts.split(',')

                if len(weights) != len(df.columns[1:]) or len(impacts) != len(df.columns[1:]):
                    st.error("The number of weights and impacts must match the number of criteria columns.")
                    return

                # Perform TOPSIS
                topsis = Topsis(
                    df=df,
                    weights=weights,
                    impacts=impacts,
                    distance_metric=distance_metric,
                    missing_data_strategy=missing_data_strategy,
                    show_para=show_parameters,
                    reverse_rank=reverse_rank
                )
                result_df = topsis.calculate()

                # Save result to CSV
                output_file = "topsis_results.csv"
                result_df.to_csv(output_file, index=False)

                st.success("TOPSIS analysis completed successfully!")
                st.write("Preview of results:")
                st.dataframe(result_df)

                # Send results via email
                if email:
                    send_email(email, output_file)
                else:
                    st.error("Please provide a valid email address to send the results.")

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
