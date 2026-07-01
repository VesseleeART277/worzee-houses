import streamlit as st
import pandas as pd

# Set page configuration for a modern web look
st.set_page_config(
    page_title="Worzee Flomo's Rental Services",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS to inject styling (Clean, modern look)
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        color: #1E3A8A;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 18px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #1E3A8A;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown('<div class="main-title">🏠 Worzee Flomo\'s Rental Services</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Lorma Quarter, Johnsonville, Montserrado Co. | Cont. 0776786247 / 0886169045</div>', unsafe_allow_html=True)
st.divider()  # Fixed: Replaced st.hr() with the valid Streamlit divider

# --- SIDEBAR / ABOUT ---
with st.sidebar:
    st.image("https://img.icons8.com/clouds/100/000000/home.png", width=100)
    st.header("About Our Services")
    st.write("""
        Welcome to Worzee Flomo's Rental Services dashboard. 
        This portal manages rental records, tenant information, 
        and upcoming project expenditures seamlessly.
    """)
    st.info("💡 Use the tabs on the right to navigate through the official logs.")

# --- DATA LOADING (Mocking the structure of your uploaded sheets) ---
@st.cache_data
def load_data():
    # Account 1 Data
    acct1_data = {
        "No.": [1, 2, 3, 4, 5, 6],
        "Tenant's Name": ["Korto", "Prince Flomo", "James Phillip", "Diamond Cooper", "Michael Johnson", "Luke J. Topoe"],
        "Duration": ["1 Month", "6 Months", "6 Months", "6 Months", "6 Months", "6 Months"],
        "Amount ($US)": [20, 120, 120, 90, 120, 120],
        "Timeline": ["Jan 1, 2025 - June 30, 2026", "Feb 16 - Aug 16, 2026", "March 21 - Sept 21, 2026", "Apr 13 - Oct 13, 2026", "June 1 - Nov 3, 2026", "May 2 - Nov 2, 2026"]
    }
    
    # Account 2 Data
    acct2_data = {
        "No": [1, 2],
        "Tenant's Name": ["George Hammond", "Cleaphus Dawolo"],
        "Duration": ["6 Months", "1 Year"],
        "Amount ($US)": [210, 360],
        "Timeline": ["Jan 2 - July 2, 2026", "May 16, 2026 - May 16, 2027"]
    }

    # Bio Data
    bio_data = {
        "No.": [1, 2, 3, 4],
        "Name": ["Annie Duzoe", "Abel Kollie", "Mamie C. Heabetus", "Diamond Cooper"],
        "Room": [1, 1, 1, 1],
        "Rental Date": ["Dec 18, 2025", "June 24, 2026", "Jan 7, 2026", "Apr 13, 2026"],
        "Emergency Contact": ["Ruth Duzoe", "Ben Kollie", "Fatu Chayee", "Jesse Cooper"],
        "Relationship": ["Sister", "Father", "Sister & Husband", "Father"]
    }
    
    # Projects
    project_data = {
        "Item": ["Zinc (Monron)", "Wood (2x4)", "Wood (2x2)", "Wood (2x6)", "Zinc Nails", "Wire Nails"],
        "Quantity": ["4 bundles", "31 pcs", "32 pcs", "16 pcs", "10 boxes", "2 cartons"],
        "Total Cost ($US)": [340.00, None, 62.21, None, None, None]
    }

    return pd.DataFrame(acct1_data), pd.DataFrame(acct2_data), pd.DataFrame(bio_data), pd.DataFrame(project_data)

df_acct1, df_acct2, df_bio, df_project = load_data()


# --- MAIN INTERFACE TABS ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 Account 1 Overview", "🏢 Account 2 Overview", "👥 Tenant Bio Data", "🛠️ Active Projects"])

with tab1:
    st.subheader("Worzee Flomo's Rental Records (Main)")
    
    # High-level metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Active Leases Listed", value=len(df_acct1))
    with col2:
        st.metric(label="Total Logged Revenue (Account 1)", value=f"${df_acct1['Amount ($US)'].sum():,.2f}")
        
    st.dataframe(df_acct1, use_container_width=True)

with tab2:
    st.subheader("Vesselee's Lone Apartment (2 Rooms)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Apartment Leases", value=len(df_acct2))
    with col2:
        st.metric(label="Total Logged Revenue (Account 2)", value=f"${df_acct2['Amount ($US)'].sum():,.2f}")
        
    st.dataframe(df_acct2, use_container_width=True)

with tab3:
    st.subheader("Verified Tenant Emergency & Information Logs")
    st.write("Authorized Emergency and landlord verification logs.")
    st.dataframe(df_bio, use_container_width=True)

with tab4:
    st.subheader("Project Expenditures & Logistics")
    st.info("⚡ Current Focus: Expenditure for roofs of three (3) rooms project (July 2026)")
    
    st.dataframe(df_project, use_container_width=True)
    st.metric(label="Grand Total Projected Budget Allocated", value="$402.21")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2026 Worzee Flomo Rental Services. All internal records secured under VGF signatures.")