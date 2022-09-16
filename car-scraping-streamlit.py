import pandas as pd 
import streamlit as st 


df = pd.read_csv('C:/Users/qvinh/OneDrive/Desktop/Documents/pythoncode/output_final.csv', skipinitialspace=True )

st.set_page_config(page_title= 'carproject')
st.header('Welcome to Vietnamese Vehicle Market project')
st.markdown('Author: Quoc Vinh')
st.caption('Library used: Pandas, Matplotlib, Seaborn, Scrapy')

# Original dataframe
st.subheader('Original dataframe')
st.caption('This dataframe has been scraped by using Scrapy')
st.caption('Source: bonbanh.com')
st.write(df.sample(10))


# Extract Year and Car name
df2  = df.copy()
new = df2['Name'].str.split("-",n=1,expand=True)
df2['Year'] = new[1]
df2['Car'] = new[0]
df2.drop(columns=['Name'],inplace=True)

# Car URL
df2['Final_link'] = "bonbanh.com/" + df['Link']
df2.drop(columns=['Link'],inplace=True)

st.subheader('Car brand based on Name')

# Car brand classification
def car_classified(name):
    if 'Kia' in name:
        result = 'Kia'
    elif 'Toyota' in name:
        result = 'Toyota'
    elif 'Lexus' in name:
        result = 'Lexus'
    elif 'Volkswagen' in name:
        result = 'Toyota'
    elif 'BMW' in name:
        result = 'BMW'
    elif 'Rolls Royce' in name:
        result = 'Rolls Royce'
    elif 'Honda' in name:
        result = 'Honda'
    elif 'Ford' in name:
        result = 'Ford'
    elif 'Hyundai' in name:
        result = 'Hyundai'
    elif 'Nissan' in name:
        result = 'Nissan'
    elif 'Peugeot' in name:
        result = 'Peugeot'
    elif 'Suzuki' in name:
        result = 'Suzuki'
    elif 'Mercedes' in name:
        result = 'Mercedes Benz'
    elif 'Chevrolet' in name:
        result = 'Chevrolet'
    elif 'Mazda' in name:
        result = 'Mazda'
    elif 'Range Rover' in name:
        result = 'Range Rover'
    elif 'Mitsubishi' in name:
        result = 'Mitsubishi'
    elif 'VinFast' in name:
        result = 'VinFast'
    elif 'Porsche' in name:
        result = 'Porsche'
    elif 'Jaguar' in name:
        result = 'Jaguar'
    elif 'Volvo' in name:
        result = 'Volvo'
    elif 'Audi' in name:
        result = 'Audi'
    elif 'Bentley' in name:
        result = 'Bentley'
    elif 'Lamborghini' in name:
        result = 'Lamborghini'
    elif 'Ferrari' in name:
        result = 'Ferrari'
    else:
        result = 'Others'
    return result
df2['Brand'] = df2['Car'].apply(car_classified)

st.write(df2[['Car','Brand']].sample(5))

# Most popular car Brand

st.subheader('Most popular cars')
number_ranking = df2.groupby(df2.Brand).size().sort_values(ascending=False)
st.bar_chart(number_ranking)

# Number of cars by Location 

df3 = df2.copy()
st.subheader('Number of cars by LOCATION')
location_ranking = df3.groupby(df3.Location).size().sort_values(ascending=False)
st.write(location_ranking.head(5))

# Convert VND to USD

def convert2pirce(text):
    if 'Tỷ' in text:
        num_bil = text.split(' Tỷ')[0]
        price = int(num_bil)*10e8 
        if 'Triệu' in text:
            num_mil = text.split(' Tỷ ')[1].split(' ')[0]
            price += int(num_mil)*10e5
        return str(price)
    else:
        return str(int(text.split(' ')[0])*10e5)

df3['Price'] = df3['Price'].apply(lambda x: f'{float(convert2pirce(x)):.3f}')
## Remove dot 

df3['Price'] = df3['Price'].str.split(".", n=1).str[0]
df3['Price'] = df3['Price'].astype(float)

## Covert to USD
df3.Price = df3.Price / 23630
df3['Price'] = df3['Price'].round()
df3['Price (USD)']  = df3['Price'] 
df3.drop('Price',axis=1,inplace=True) 

st.subheader("Convert VND into USD")
st.write(df3[['Car','Price (USD)']])

# Average price by Brand
df4 = df3.copy()

avg_price = df4.groupby('Brand')['Price (USD)'].mean().to_frame(name='Average price').reset_index()
avg_price['Average price']  = avg_price['Average price'].apply(lambda x: '%.2f' %x)
avg_price['Average price'] = avg_price['Average price'].astype(float)

st.subheader("Top 5 most expensive car brand")
st.write(avg_price.nlargest(5,'Average price'))

st.subheader("Top 5 least expensive car brand")
st.write(avg_price.nsmallest(5,'Average price'))

# Top 10 most popular cars 

df5 = df4.copy()

popular_cars = df5.groupby(df5.Car).size().sort_values(ascending=False).to_frame('Count').reset_index()

st.subheader("Top 10 most popular cars")
st.write(popular_cars.nlargest(10,'Count'))


