# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 23:41:50 2022

@author: ASUS
"""

import streamlit as st
import pickle
model=pickle.load(open('Random_Forest.pkl','rb'))
st.title('Selling Price Predictor')
st.markdown("### Are you planning to sell your car !?\n### So lets try evaluating the price..")
def main():
    
    # @st.cache(allow_output_mutation=True)
    #def get_model():
        
        # model=pickle.load(open('Random_Forest.pkl','rb'))
    #return model
        
       # st.write()
        Year=st.number_input('In which year car was purchased',1990,2022,step=1,key='year')
        No_years=2022-Year
        

        PP=st.number_input('What is the current ex-showroom price of the car ? (In ₹lakhs)',0.00,50.00,step=0.5,key='present_price')
        Kms_Driven=st.number_input('What is the distance completed in kms?',0.00,500000.00,step=500.00,key='drived')
        Owner=st.radio('The number of owners?',(0,1,3),key='owner')
        Fuel_Type_Petrol=st.selectbox('What is the fuel type of car?',('Petrol','Diesel','CNG'),key='fuel')
        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol=1
            Fuel_Type_Desiel=0
        elif(Fuel_Type_Petrol=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
        Seller_Type_Individual=st.selectbox('Are you a dealer or an individual?',('Dealer','Individual'),key='dealer') 
        
            
            
        Transmission_Mannual=st.selectbox('What is Transmission Type?',('Manual','Automatic'),key='manual')
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
            
     
        if st.button('Estimate Price',key='predict'):
            try:
                Model=model  #get model()
                prediction=Model.predict([[PP,Kms_Driven,Owner,No_years,Fuel_Type_Desiel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
                output=round(prediction[0],2)
                if output<0:
                    st.warning('You will be not able to sell this car!')
                else:
                    st.success('You can cell the car for {}lakhs'.format(output))
            except:
                st.warning("Opps!! Something went wrong\nTry again")
                
if __name__ == "__main__":
    main()
                
            
          
          
