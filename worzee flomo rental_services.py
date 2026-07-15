import streamlit as st
import pandas as pd

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------
st.set_page_config(
    page_title="Worzee Flomo's Rental Services",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# This website was built by Vesselee G. Flomo
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
.metric-card{
    background-color:#f8fafc;
    padding:10px;
    border-radius:10px;
    border:1px solid #e5e7eb;
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
        - Expenditure Records
        - Financial Overview
        """
    )

    st.info("Use the tabs to navigate.")

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------
@st.cache_data
def load_data():

    # ==========================
    # ACCOUNT 1 RENTAL RECORDS
    # ==========================
    acct1_data = {
        "No.":[1,2,3,4,5,6,7,8,9,10,11],
        "Tenant's Name":[
            "Korto Lepowoe",
            "Prince Flomo",
            "James Phillip",
            "Diamond Cooper",
            "Michael Johnson",
            "Luke J. Topoe",
            "George F. Tamba",
            "Mamie Heagbetus",
            "Annie Duzoe",
            "Sauliama Lewis",
            "Abel Kollie",
        ],
        "Duration":[
            "6 Month","6 Months","6 Months","6 Months","6 Months",
            "6 Months","6 Months","6 Months","6 Months","12 Months","9 Months",
        ],
        "Amount ($US)":[120,120,120,90,120,120,120,120,120,0,180],
        "Timeline":[
            "July 1, 2026 - Jan 1, 2027",
            "Feb 16 - Aug 16, 2026",
            "Mar 21 - Sep 21, 2026",
            "Apr 13 - Oct 13, 2026",
            "Jun 1 - Nov 3, 2026",
            "May 2 - Nov 2, 2026",
            "May 1 - Oct 31, 2026",
            "Jul 7 - Jan 7, 2027",
            "Jun 18 - Dec 18, 2026",
            "Aug 1, 2025  Jul 31, 2026",
            "Jun 24 - Mar 24, 2027",
        ],
    }

    # ==========================
    # TENANT INFORMATION
    # ==========================
    bio_data = {
        "No.":[1,2,3,4,5,6,7,8,9,10,11],
        "Name":[
            "Annie Duzoe","Abel Kollie","Mamie C. Heabetus","Diamond Cooper",
            "Michael Johnson","Felecia Wehyeh","James Phillip","George Fallah Tamba",
            "Luke J. Topoe","Korto Lepowoe","Sauliama Lewis",
        ],
        "Room":[1]*11,
        "Rental Date":[
            "Dec 18, 2025","Jun 24, 2026","Jan 7, 2026","Apr 13, 2026",
            "Dec 1, 2025","Feb 16, 2026","Mar 21, 2026","May 1, 2026",
            "Nov 2, 2025","Dec 1, 2025","Aug 1, 2021",
        ],
        "Tenant Phone":[
            "0777609651","0779021296","0775791797","077585969",
            "0777329044","0777331883","0775255752","0778691405",
            "0775236950","0777494587","0777488350",
        ],
        "Emergency Contact":[
            "Ruth Duzoe","Ben Kollie","Fatu Chayee & Heabetus","Jesse Cooper",
            "Bill Wonyeh","Prince Flomo","Thomas T. Kpando / Naomi","Tamba Sakillah",
            "Prince Flomo","","",
        ],
        "Emergency Phone":[
            "0777123798","0770397550 / 0888878055","0770903805 / 0887242464","0776250531",
            "0775522081","0770947612","0776700975 / 0772777619","0777668310",
            "0776218125","","",
        ],
        "Address":[
            "New Georgia Community","Palm Farm Community, Johnsonville","Kpelleh Town","New Dowen, Margibi County",
            "Wein Town Community","Ma Kebeh Shop, Johnsonville","Cooper Farm, Fendell","Point Four, Duala",
            "City View, Rehab Community","","",
        ],
        "Relationship":[
            "Sister","Father","Sister & Husband","Father",
            "Brother","Husband","Brother & Wife","Relative/Brother",
            "Brother","","",
        ],
        "Landlord":["Vesselee G. Flomo"]*11,
        "Police Contact":["Michael P.Johnson"]*11,
        "Police Phone":["0770188742"]*11,
    }

    # ==========================
    # EXPENDITURE RECORDS
    # ==========================
    expenditure_data = {
        "No.": list(range(1,14)),
        "Amount ($US)":[20,60,20,80,75.40,20,15,35,5,20,20,8.33,55.55],
        "Purpose":[
            "LEC Recharge","Reimbursement","WAEC","Temptation / Phone",
            "Temptation / Excuse","Transportation","2 pcs of Zinc & Pay",
            "Expenditure & Workmanship","Offer","Offer",
            "High School Documents","WAEC Result & Entrance fee","School fee for Nurse Aide program"
        ],
        "Date":[
            "Feb 2026","Apr-Jun 2026","Apr 2026","May 7, 2026",
            "May 7, 2026","May 17, 2026","May 29, 2026","May 5, 2026",
            "Jun 19, 2026","Jun 19, 2026","Jun 19, 2026","Jun 27, 2026","Jul 9, 2026"
        ],
        "Beneficiary":[
            "LEC","Samuel Paygar","Zazay Y. Flomo","Jerrylyne Quawolo & Praiselious",
            "Jerrylyne Quawolo & Praiselious","Vesselee G. Flomo","Ujay single room / roof",
            "Mamie single room / roof","Zazay Y. Flomo","Vesselee G. Flomo",
            "Yanga Flomo","Yanga Flomo","Yanga Flomo "
        ],
    }

    return (
        pd.DataFrame(acct1_data),
        pd.DataFrame(bio_data),
        pd.DataFrame(expenditure_data),
    )

df_acct1, df_bio, df_exp = load_data()

# ----------------------------------------------------
# SUMMARY VALUES
# ----------------------------------------------------
acct1_total = df_acct1["Amount ($US)"].sum()
exp_total = df_exp["Amount ($US)"].sum()
rent_total = acct1_total
balance = rent_total - exp_total
tenant_total = len(df_bio)

# ----------------------------------------------------
# DASHBOARD METRICS
# ----------------------------------------------------
st.subheader("📌 Dashboard Overview")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Total Tenants", tenant_total)
m2.metric("Rental Income", f"${rent_total:,.2f}")
m3.metric("Expenditures", f"${exp_total:,.2f}")
m4.metric("Net Balance", f"${balance:,.2f}")

st.divider()

# ----------------------------------------------------
# TABS
# ----------------------------------------------------
tab1, tab2, tab3 = st.tabs([
    "📊 Account 1 ",
    "👥 Tenant Bio",
    "💸 Expenditures",
])

# ----------------------------------------------------
# ACCOUNT TAB
# ----------------------------------------------------
with tab1:
    st.subheader("Account 1 Rental Records")

    col1, col2 = st.columns(2)
    col1.metric("Active Leases", len(df_acct1))
    col2.metric("Total Revenue", f"${acct1_total:,.2f}")

    search1 = st.text_input("Search Tenant", key="search_acct1")
    acct1_view = df_acct1[
        df_acct1["Tenant's Name"].str.contains(search1, case=False, na=False)
    ] if search1 else df_acct1

    st.dataframe(acct1_view, use_container_width=True)

# ----------------------------------------------------
# TENANT BIO TAB
# ----------------------------------------------------
with tab2:
    st.subheader("Tenant Information")

    search_bio = st.text_input("Search Tenant Bio", key="search_bio")
    bio_view = df_bio[
        df_bio["Name"].str.contains(search_bio, case=False, na=False)
    ] if search_bio else df_bio

    st.dataframe(bio_view, use_container_width=True)

# ----------------------------------------------------
# EXPENDITURES TAB
# ----------------------------------------------------
with tab3:
    st.subheader("Expenditure Records")

    st.dataframe(df_exp, use_container_width=True)
    st.metric("Total Expenditure", f"${exp_total:,.2f}")

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------
st.divider()
st.caption("© 2026 Worzee Flomo's Rental Services | All Rights Reserved.")
