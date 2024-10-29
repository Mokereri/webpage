import streamlit as st
import os

# Set page config
st.set_page_config(page_title="My webpage", page_icon=":Chart Increasing", layout="wide")

# CSS for theming
st.markdown(
    """
    <style>
        body {
            background-color: #273346;
            color: #FFFFFF;
            font-family: 'sans-serif';
        }
        .stButton > button {
            background-color: #7792E3;
            color: white;
            border: none;
            border-radius: 5px;
        }
        .stButton > button:hover {
            background-color: #6a82b5;
        }
        .contact-form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            max-width: 400px;
            margin: auto;
        }
        .contact-form input, .contact-form textarea, .contact-form button {
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
        }
        .contact-form button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        .contact-form button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# HEADER SETUP
with st.container():
    st.subheader("Hi, I am Mokereri Kelvin")
    st.title("A Data Analyst From Kenya")
    st.write(" I am a highly skilled data analyst with a proven track record of driving business insights through data analysis and visualization, seeking a challenging position that offers increased responsibility and the opportunity to tackle complex data problems. I am motivated to take on new challenges and leverage my expertise in delivering actionable solutions and achieving measurable results.")
    st.write("[Portfolio >](https://www.datascienceportfol.io/mk)")

# -- WHAT I DO 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write(
            """
            I specialize in analyzing datasets using Excel, Power BI, SQL, and Python to uncover actionable insights that drive business success.

            My focus includes:
            - Creating impactful visualizations and automating reporting processes.
            - Forecasting demand to enhance operational efficiency.
            - Supporting strategic decision-making to help businesses:
              - Increase profits
              - Make informed decisions
              - Cut costs

            I have successfully completed projects centered on:
            - Advertising metrics.
            - Supply chain optimization.
            - Building machine learning models and crafting insightful dashboards.

            If this sounds interesting to you, consider contacting me for collaboration.
            """
        )

    with right_column:
        st.header("Dashboard")
        # Specify the path to your screenshot
        screenshot_path = r"C:\Users\user\Downloads\WhatsApp Image 2024-10-11 at 15.45.06.jpeg" 
        if os.path.exists(screenshot_path):
            st.image(screenshot_path, caption="Sample Dashboard of my work", use_column_width=True)
        else:
            st.write("Screenshot not found. Please check the file path.")

st.write("[My work >](https://www.datascienceportfol.io/mk)")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

# -- Insert video
with image_column:
    st.video("C:\\Users\\user\\Downloads\\WhatsApp Video 2024-10-14 at 20.58.05.mp4")

with text_column: 
    st.subheader("Supply Chain Analysis")
    st.write(
        """
        - Problem: Supply chain losses amounting to 9% of monthly procurement.
        - Solution: Tracking dashboard + alerts to identify areas of loss across the chain (e.g., delays, damages, returns, etc.).
        - Impact: Losses reduced to 3% in 1 month after solution implementation.
        """
    )
    
    st.markdown("[Read Blog...](https://x.com/M10newbie/status/1841844979808850145)")

with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    
    # -- Insert Image
    with image_column:
        st.image("C:\\Users\\user\\Desktop\\Docs\\Tracking.png", caption="Dashboard")

    with text_column: 
        st.subheader("Tracking Facebood Ad Cost")
        st.write(
            """
            • Integrated data from Facebook Ads and Google Ads APIs to extract relevant advertising metrics, including ad spend, impressions, and clicks.  
            • Designed and maintained a MySQL database to store advertising and e-commerce order data, ensuring efficient data retrieval and management.  
            • Created SQL queries and views to calculate total ad spend, cost per order, and sales/order values from various sources. Developed interactive dashboards using Power BI for real-time data visualization and insights.  
            • Implemented cron jobs to automate daily data extraction, updating the database with the latest ad spend and order information.
            """
        )
    st.markdown("[Read Article...](https://medium.com/@mokererikelvin/tracking-facebook-and-google-ad-cost-and-order-analysis-f1f7e3fb845a)")

with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))

# For the next video
with image_column:
    st.video("C:\\Users\\user\\Downloads\\Project vid - Made with Clipchamp.mp4")
    st.caption("Project Management")  # Add caption here

with text_column: 
    st.subheader("Project Management")
    st.write(
        """
        Organizations can find valuable insights that enhance decision-making, allocate resources optimally, and boost project performance by adopting a structured approach to data cleansing, analysis, and visualization. 
        Effectively utilizing data is essential for achieving long-term success in any organization as project management evolves.
        
        In summary, leveraging data in project management can unveil strategies to improve efficacy and efficiency, ensuring that businesses not only meet but exceed their goals.
        """
    )
    st.markdown("[Read Article...](https://medium.com/@mokererikelvin/uncovering-insights-in-project-management-a-data-driven-approach-f3615964be90)")
    
with st.container():
    st.write("---")
    st.header("Contact Me")
    st.write("##")

contact_form = """
<form action="https://formsubmit.co/mokererikelvin2017@gmail.com" method="POST" class="contact-form">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message Here" required></textarea>
    <button type="submit">Send</button>
</form>
"""

# Corrected line
left_column, right_column = st.columns(2)

with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)

with right_column:
    st.empty()
