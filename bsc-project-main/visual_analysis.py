import streamlit as st
from data import dataset


dataframe = dataset()

def sales_section():
    st.text('Bellow is a sneak peak on to our dataset')
    st.dataframe(dataframe.sales.head())
    st.markdown("""---""") 
    st.text('Bellow we analyse best months for sales and worst months for sales')
    st.line_chart(dataframe.best_months_df)
    st.markdown("""---""") 
    st.text('Bellow we analyse best district for sales')
    st.line_chart(dataframe.best_district_df)
    st.markdown("""---""") 
    st.text("Given that the best selling site has the id 284 from the district of Rwamagana.")
    #st.text('Given that the best selling site has the id: {0} from the distric of {1}'.format(dataframe.best_district_df.idxmax(), dataframe.sites.iloc[dataframe.best_district_df.idxmax()]))
    st.text("Bellow is the are best selling product from the best site")
    st.dataframe(dataframe.best_district_products)
    st.markdown("""---""") 
    # st.text("shows products that sold on same date")
    # st.dataframe(dataframe.daf.head())
    
def customers_section():

    pass

def products_section():
    pass