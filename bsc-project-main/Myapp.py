import streamlit as st
from visual_analysis import *
from PIL import Image
from data import *
dataframe = dataset()
st.set_page_config(page_title="sales dashboard", page_icon=":bar_chart:", layout="wide")
image = Image.open('BSC-High-res.-vector-logo-01.png')

#---main page---
st.title(":bar_chart: sales Dashboard")
st.markdown("##")

#--- top kpi's ---
total_orders = dataframe.sales.groupby('OrderNumber').sum()
dataframe.sales.OrderNumber = dataframe.sales.OrderNumber.astype('string')





#---side bar---
SIDEBAR_OPTION_PROJECT_WIKI = "Project Wiki"
SIDEBAR_OPTION_ANALYSIS = "Data Analysis & Visualisation"
SIDEBAR_OPTION_TEAM = "Meet the Team"
SIDEBAR_OPTION_FORECAST = "Predict"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_WIKI, SIDEBAR_OPTION_ANALYSIS, SIDEBAR_OPTION_FORECAST, SIDEBAR_OPTION_TEAM]


def wiki_section():
    left_column, middel_column, right_column = st.columns(3)
    with left_column:
        st.subheader("Total Orders")
        st.metric(label="", value="{:,}".format(dataframe.sales.OrderNumber.count()))
        st.markdown("""---""")
    with middel_column:
        st.subheader("Total Revenue")
        st.metric(label="", value="{:,} RWF".format(dataframe.sales.Total.sum()))
        st.markdown("""---""")
    with right_column:
        st.subheader("Total Profit")
        st.metric(label="", value="{:,} RWF".format(dataframe.sales.Profit.sum()))
        st.markdown("""---""")
    #st.subheader(f"US $ {total_orders:,}")
    #scope of project
    st.subheader("scope of project")
    st.text("Broadband Systems Corporation has been at the forefront of" )
    st.text("ICT services in Rwanda with its mission of providing world-class broadband connectivity and solutions to empower citizens,") 
    st.text("communities, government, and businesses in Rwanda and the region, However, Bsc logistics and sales are not data-driven,")
    st.text("this can reduce the delivery services and increase the wastage.")
    st.text(" This project is designed with the capacity of making their business model more data-driven by  making the balance between Bsc’s demands and supply.")
   
    st.markdown("""---""")    
    #Project Goals
    st.subheader("Project Goals")
    st.text("To implement a model that helps to meet the business requirements by giving clearer solutions to make good decisions ")
    st.text("The optimize this model by avoiding unexpected burdens on production ")
    st.text("To provide a user interface that visualizes our model well.")
    st.markdown("""---""")
    # #trends
    st.subheader("Trends")
    

def visual_analysis_section():

    #Defining SUB-SIDEBAR OPTIONS in the Visualisation section
    VIZ_SIDEBAR_OPTION_SALES = "SALES"
    VIZ_SIDEBAR_OPTION_CUSTOMERS = "CUSTOMERS"
    VIZ_SIDEBAR_OPTION_PRODUCTS = "PRODUCTS"
    VIZ_SIDEBAR_OPTION_SITE = "SITE"
    VIZ_SIDEBAR_OPTION_SALES_TEAM = "SALES TEAM"

    VIZ_SIDEBAR_OPTIONS = [VIZ_SIDEBAR_OPTION_SALES, VIZ_SIDEBAR_OPTION_CUSTOMERS, VIZ_SIDEBAR_OPTION_PRODUCTS, VIZ_SIDEBAR_OPTION_SITE, VIZ_SIDEBAR_OPTION_SALES_TEAM]

    VIZ_SIDEBAR_STATUS = st.sidebar.selectbox('Visualisation Section', VIZ_SIDEBAR_OPTIONS)

    if VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_SALES:
        sales_section()
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_CUSTOMERS:
        st.text("Customers")
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_PRODUCTS:
        st.text("Product")
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_SITE:
        st.text("Site Data")
    elif VIZ_SIDEBAR_STATUS == VIZ_SIDEBAR_OPTION_SALES_TEAM:
        st.text("Sales team")
    else:
        pass



def main():
    st.sidebar.success("Please choose an option bellow.")
    SIDEBAR_STATUS = st.sidebar.selectbox('Menu Option', SIDEBAR_OPTIONS)

    if SIDEBAR_STATUS == SIDEBAR_OPTION_PROJECT_WIKI:
        st.image(image, caption='BSC-High-res.-vector-logo-01.png')
        st.title("BCS Sales Forecasting Project")
        wiki_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_ANALYSIS:
        visual_analysis_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_FORECAST:
        st.text("Welcome to the model prediction")
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_TEAM:
        st.text("Meet the team")
    else:
        pass



main()