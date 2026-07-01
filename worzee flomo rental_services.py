import streamlit as st
import pandas as pd

# This website was build by Vesselee G. Flomo###
# PAGE CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="Worzee Flomo's Rental Services",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------
st.markdown("""
<style>
.main-title{
    font-size:40px;
    color:#1E3A8A;
    font-weight:bold;
    text-align:center;
}
.subtitle{
    font-size:18px;
    color:#555;
    text-align:center;
    margin-bottom:20px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------
st.markdown(
    "<div class='main-title'>🏠 Worzee Flomo's Rental Services</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>"
    "Lorma Quarter, Johnsonville, Montserrado County<br>"
    "Contact: 0776786247 | 0886169045"
    "</div>",
    unsafe_allow_html=True,
)

st.divider()

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------
with st.sidebar:
    st.image(
        "https://img.icons8.com/clouds/100/000000/home.png",
        width=100,
    )

    st.header("About")

    st.write(
        """
        Welcome to **Worzee Flomo's Rental Services**.

        This dashboard helps manage:

        - Rental Records
        - Tenant Information
        - Active Projects
        - Financial Overview
        """
    )

    st.info("Use the tabs to navigate.")

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------
@st.cache_data
def load_data():

    acct1_data = {
        "No.": [1,2,3,4,5,6,7,8,9,10,11],
        "Tenant's Name":[
            "Korto Lepowoe",
            "Prince Flomo",
            "James Phillip",
            "Diamond Cooper",
            "Michael Johnson",
            "Luke J. Topoe",
            "George F. Tamba",
            "Mamie Heabetus",
            "Annie Duzoe",
            "Sauliama Lewis",
            "Abel Kollie"
        ],
        "Duration":[
            "1 Month",
            "6 Months",
            "6 Months",
            "6 Months",
            "6 Months",
            "6 Months",
            "6 Months",
            "6 Months",
            "6 Months",
            "12 Months",
            "9 Months"
        ],
        "Amount ($US)":[
            20,120,120,90,120,120,120,0,120,0,180
        ],
        "Timeline":[
            "Jan 1 - Jun 30, 2026",
            "Feb 16 - Aug 16, 2026",
            "Mar 21 - Sep 21, 2026",
            "Apr 13 - Oct 13, 2026",
            "Jun 1 - Nov 3, 2026",
            "May 2 - Nov 2, 2026",
            "May 1 - Oct 31, 2026",
            "Jan 7 - Jul 7, 2026",
            "Jun 18 - Dec 18, 2026",
            "Aug 1, 2026 - Jul 31, 2027",
            "Jun 24, 2026 - Mar 24, 2027",
        ],
    }

    acct2_data = {
        "No.":[1,2],
        "Tenant's Name":[
            "George Hammond",
            "Cleaphus Dawolo",
        ],
        "Duration":[
            "6 Months",
            "1 Year",
        ],
        "Amount ($US)":[210,360],
        "Timeline":[
            "Jan 2 - Jul 2, 2026",
            "May 16, 2026 - May 16, 2027",
        ],
    }

    bio_data = {
        "No.":[1,2,3,4,5,6,7,8,9,10,11],
        "Name":[
            "Korto Lepowoe",
            "Prince Flomo",
            "James Phillip",
            "Diamond Cooper",
            "Michael Johnson",
            "Luke J. Topoe",
            "George F. Tamba",
            "Mamie Heabetus",
            "Annie Duzoe",
            "Sauliama Lewis",
            "Abel Kollie",
        ],
        "Room":[1,1,1,1,1,1,1,1,1,1,1],
        "Rental Date":[
            "Jan 1, 2026",
            "Feb 16, 2026",
            "Mar 21, 2026",
            "Apr 13, 2026",
            "Jun 1, 2026",
            "May 2, 2026",
            "May 1, 2026",
            "Jan 7, 2026",
            "Jun 18, 2026",
            "Aug 1, 2026",
            "Jun 24, 2026",
        ],
        "Emergency Contact":[
            "?",
            "Prince Flomo",
            "Thomas T. Kpando / Naomi",
            "Jesse Cooper",
            "Bill Wonyeh",
            "?",
            "Tamba Sakillah",
            "Fatu Heabetus",
            "Ruth Duzoe",
            "?",
            "Ben Kollie",
        ],
        "Relationship":[
            "?",
            "Husband",
            "Brother & Wife",
            "Father",
            "Brother",
            "?",
            "Relative/Brother",
            "Sister",
            "Sister",
            "?",
            "Father",
        ],
    }

    project_data = {
        "Item":[
            "Zinc (32 gauge moroon color)",
            "Wood (2x4)",
            "Wood (2x2)",
            "Wood (2x6)",
            "Zinc Nails",
            "Wire Nails",
        ],
        "Quantity":[
            "4 bundles",
            "31 pcs",
            "32 pcs",
            "16 pcs",
            "10 boxes",
            "2 cartons",
        ],
        "Total Cost ($US)":[
            340.00,
            None,
            62.21,
            None,
            None,
            None,
        ],
    }

    return (
        pd.DataFrame(acct1_data),
        pd.DataFrame(acct2_data),
        pd.DataFrame(bio_data),
        pd.DataFrame(project_data),
    )


df_acct1, df_acct2, df_bio, df_project = load_data()

# ----------------------------------------------------
# TABS
# ----------------------------------------------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Account 1",
    "🏢 Account 2",
    "👥 Tenant Bio",
    "🛠 Projects",
])

with tab1:

    st.subheader("Account 1 Rental Records")

    col1, col2 = st.columns(2)

    col1.metric("Active Leases", len(df_acct1))
    col2.metric(
        "Total Revenue",
        f"${df_acct1['Amount ($US)'].sum():,.2f}",
    )

    st.dataframe(df_acct1, use_container_width=True)

with tab2:

    st.subheader("Apartment 2 Rental Records")

    col1, col2 = st.columns(2)

    col1.metric("Leases", len(df_acct2))
    col2.metric(
        "Total Revenue",
        f"${df_acct2['Amount ($US)'].sum():,.2f}",
    )

    st.dataframe(df_acct2, use_container_width=True)

with tab3:

    st.subheader("Tenant Information")

    st.dataframe(df_bio, use_container_width=True)

with tab4:

    st.subheader("Active Projects")

    st.info("Roofing project for three rooms (July 2026).")

    st.dataframe(df_project, use_container_width=True)

    total_budget = df_project["Total Cost ($US)"].fillna(0).sum()

    st.metric(
        "Current Budget",
        f"${total_budget:,.2f}",
    )

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------
st.divider()

st.caption(
    "© 2026 Worzee Flomo's Rental Services | All Rights Reserved."
)
