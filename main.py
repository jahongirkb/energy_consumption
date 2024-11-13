import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


# Generate data for the line graph
date_range = pd.date_range(start="2024-11-12", end=pd.to_datetime("now"), freq='H')  # Hourly data from 01.01.2024 to now


kuch_values = np.random.randint(0, 81, len(date_range))  # Random voltage values between 0 and 80
tok_values = np.random.randint(0, 16, len(date_range))  # Random voltage values between 0 and 15
radiatsiya = np.random.randint(0, 151, len(date_range))
harorat = np.random.randint(25, 27, len(date_range))
# Create DataFrame
data = pd.DataFrame({"Vaqt": date_range, "Kuchlanish": kuch_values, "Tok kuchi": tok_values, "Radiatsiya":radiatsiya, "Harorat": harorat})

fig_solar_kuch = px.line(data, x="Vaqt", y="Kuchlanish", title="Kuchlanishning qiymatlari o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Kuchlanish": "Kuchlanish (V)"})
fig_solar_kuch.update_xaxes(rangeslider_visible=True)  # Adds a range slider for zooming in/out on the x-axis

fig_solar_tok = px.line(data, x="Vaqt", y="Tok kuchi", title="Vaqt birligida tok kuchining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Tok kuchi": "Tok kuchi (A)"})
fig_solar_tok.update_xaxes(rangeslider_visible=True)  # Adds a range slider for zooming in/out on the x-axis

fig_solar_rad = px.line(data, x="Vaqt", y="Radiatsiya", title="Vaqt birligida radiatsiyaning o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Radiatsiya": "Radiatsiya (W/m.kv)"})
fig_solar_rad.update_xaxes(rangeslider_visible=True)

fig_solar_har = px.line(data, x="Vaqt", y="Harorat", title="Vaqt birligida haroratning o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Harorat": "Harorat (C)"})
fig_solar_har.update_xaxes(rangeslider_visible=True)

kuch_shamol = np.random.randint(0, 61, len(date_range))
tok_shamol= np.random.randint(0, 11, len(date_range))
tezlik_shamol= np.random.randint(0, 31, len(date_range))
data_shamol = pd.DataFrame({"Vaqt": date_range, "Kuchlanish": kuch_shamol, "Tok kuchi": tok_shamol, "Shamol tezligi": tezlik_shamol})


fig_shamol_kuch = px.line(data_shamol, x="Vaqt", y="Kuchlanish", title="Vaqt birligida kuchlanishnig o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Kuchlanish": "Kuchlanish (v)"})
fig_shamol_kuch.update_xaxes(rangeslider_visible=True)


fig_shamol_tez = px.line(data_shamol, x="Vaqt", y="Shamol tezligi", title="Vaqt birligida shamol tezligining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Shamol tezligi": "Shamol tezligi (m/s)"})
fig_shamol_tez.update_xaxes(rangeslider_visible=True)


fig_shamol_tok = px.line(data_shamol, x="Vaqt", y="Tok kuchi", title="Vaqt birligida tok kuchining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Tok kuchi": "Tok kuchi (A)"})
fig_shamol_tok.update_xaxes(rangeslider_visible=True)

kuch_dg = np.random.randint(0, 241, len(date_range))
tok_dg= np.random.randint(0, 31, len(date_range))
yoqilgi_dg= np.random.randint(0, 101, len(date_range))
data_dg = pd.DataFrame({"Vaqt": date_range, "Kuchlanish": kuch_dg, "Tok kuchi": tok_dg, "Yoqilg'i": yoqilgi_dg})


fig_dg_kuch = px.line(data_dg, x="Vaqt", y="Kuchlanish", title="Vaqt birligida kuchlanishnig o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Kuchlanish": "Kuchlanish (v)"})
fig_dg_kuch.update_xaxes(rangeslider_visible=True)


fig_dg_yoq = px.line(data_dg, x="Vaqt", y="Yoqilg'i", title="Vaqt birligida yoqilg'ining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Yoqilg'i": "Yoqilg'i (L)"})
fig_dg_yoq.update_xaxes(rangeslider_visible=True)


fig_dg_tok = px.line(data_dg, x="Vaqt", y="Tok kuchi", title="Vaqt birligida tok kuchining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Tok kuchi": "Tok kuchi (A)"})
fig_dg_tok.update_xaxes(rangeslider_visible=True)


kuch_ab = np.random.randint(10, 15, len(date_range))
tok_ab= np.random.randint(0, 21, len(date_range))
# k = date_range
# zaryad_ab = sorted(np.random.randint(0, 101, k), reverse=True)
zaryad_ab= sorted(np.random.randint(0, 101, len(date_range)), reverse=True)
data_ab = pd.DataFrame({"Vaqt": date_range, "Kuchlanish": kuch_ab, "Tok kuchi": tok_ab, "Zaryad miqdori": zaryad_ab})


fig_ab_kuch = px.line(data_ab, x="Vaqt", y="Kuchlanish", title="Vaqt birligida kuchlanishnig o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Kuchlanish": "Kuchlanish (v)"})
fig_ab_kuch.update_xaxes(rangeslider_visible=True)


fig_ab_zar = px.line(data_ab, x="Vaqt", y="Zaryad miqdori", title="Vaqt birligida zaryad miqdorining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Zaryad miqdori": "Zaryad miqdori (%)"})
fig_ab_zar.update_xaxes(rangeslider_visible=True)


fig_ab_tok = px.line(data_ab, x="Vaqt", y="Tok kuchi", title="Vaqt birligida tok kuchining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Tok kuchi": "Tok kuchi (A)"})
fig_ab_tok.update_xaxes(rangeslider_visible=True)


kuch_c = np.random.randint(0, 381, len(date_range))
tok_c = np.random.randint(0, 201, len(date_range))
data_c = pd.DataFrame({"Vaqt": date_range, "Kuchlanish": kuch_c, "Tok kuchi": tok_c})


fig_c_kuch = px.line(data_c, x="Vaqt", y="Kuchlanish", title="Vaqt birligida kuchlanishnig o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Kuchlanish": "Kuchlanish (v)"})
fig_c_kuch.update_xaxes(rangeslider_visible=True)

fig_c_tok = px.line(data_c, x="Vaqt", y="Tok kuchi", title="Vaqt birligida tok kuchining o'zgarishi", labels={"Vaqt": "Vaqt (soat)", "Tok kuchi": "Tok kuchi (A)"})
fig_c_tok.update_xaxes(rangeslider_visible=True)

# Sidebar navigation
st.sidebar.title("Dashboard")
page = st.sidebar.selectbox("Viloyatni tanlang", ["Bosh sahifa", "1. Andijon", "2. Buxoro", "3. Farg'ona", 
                            "4. Jizzax", "5. Xorazm", "6. Namangan", "7. Navoiy", "8. Qashqadaryo", "9. Qoraqalpog'iston Respublikasi",
                            "10. Samarqand", "11. Sirdaryo", "12. Surxondaryo", "13. Toshkent viloyati", "14. Toshkent shahri"])

# Bosh sahifa
if page == "Bosh sahifa":
    st.title("Bosh sahifa")
    st.write("Viloyatni tanlash uchun yuqoridagi menyudan foydalaning.")

# Andijon Page
elif page == "1. Andijon":
    st.title("Andijon viloyati tumanlari")
    main_category = st.selectbox("Tumanni tanlang", ["Tumanni kiriting", "1. Andijon tumani", "2. Asaka", "3. Baliqchi",
                                "4. Bo'ston", "5. Buloqboshi", "6. Izboskan", "7. Jalaquduq", "8. Marhamat",
                                "9. Oltinko'l", "10. Paxtaobod", "11. Qo'rg'ontepa", "12. Shahrixon", "13. Ulug'nor", "14. Xo'jaobod"])
    
    if main_category == "1. Andijon tumani":
        st.title("Andijon tumani")
        page = st.selectbox("Obektni tanlang", ["Obektni kiriting", "Obekt 1", "Obekt 2", "Obekt 3"])
        if page == "Obekt 1":
            st.header("Obekt 1")
            d1 = st.selectbox("Quyosh (solar)", ["Tanlang", "Tok kuchi", "Kuchlanish", "Radiatsiya", "Harorat"])
            if d1 == "Tok kuchi":
                st.plotly_chart(fig_solar_tok)
            if d1 == "Kuchlanish":
                st.plotly_chart(fig_solar_kuch)
            if d1 == "Radiatsiya":
                st.plotly_chart(fig_solar_rad)
            if d1 == "Harorat":
                st.plotly_chart(fig_solar_har)
            d2 = st.selectbox("Shamol", ["Tanlang", "Tok kuchi", "Kuchlanish", "Shamol tezligi"])
            if d2 == "Tok kuchi":
                st.plotly_chart(fig_shamol_tok)
            if d2 == "Kuchlanish":
                st.plotly_chart(fig_shamol_kuch)
            if d2 == "Shamol tezligi":
                st.plotly_chart(fig_shamol_tez)
            d3 = st.selectbox("Dizel generatori", ["Tanlang", "Tok kuchi", "Kuchlanish", "Yoqilg'i"])
            if d3 == "Tok kuchi":
                st.plotly_chart(fig_dg_tok)
            if d3 == "Kuchlanish":
                st.plotly_chart(fig_dg_kuch)
            if d3 == "Yoqilg'i":
                st.plotly_chart(fig_dg_yoq)
            d4 = st.selectbox("Akkumlyator batarekasi", ["Tanlang", "Tok kuchi", "Kuchlanish", "Zaryad miqdori"])
            if d4 == "Tok kuchi":
                st.plotly_chart(fig_ab_tok)
            if d4 == "Kuchlanish":
                st.plotly_chart(fig_ab_kuch)
            if d4 == "Zaryad miqdori":
                st.plotly_chart(fig_ab_zar)
            d5 = st.selectbox("Markazlashgan energiya ta'minoti", ["Tanlang", "Tok kuchi", "Kuchlanish"])
            if d5 == "Tok kuchi":
                st.plotly_chart(fig_c_tok)
            if d5 == "Kuchlanish":
                st.plotly_chart(fig_c_kuch)
    elif main_category == "Asaka":
        st.header("Asaka")
        st.write("Asaka tumaniga xush kelibsiz!")

# Buxoro Page
elif page == "2. Buxoro":
    st.title("Buxoro Viloyati")
    st.write("Buxoro viloyati sahifasiga xush kelibsiz.")

# Farg'ona Page
elif page == "3. Farg'ona":
    st.title("Farg'ona Viloyati")
    st.write("Farg'ona viloyati sahifasiga xush kelibsiz.")




