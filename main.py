import streamlit as st
import pickle



read_1 = pickle.load(open("/mount/src/air_checker/lin_reg_model.pkl,", 'rb')) 




#page title
st.title('Air Checker')

#Welcome text
container_1 = st.container(border=True)
container_1.write("Kita tidak menghargai apa yang kita miliki sampai itu hilang. Kebebasan memang seperti itu. Itu seperti udara. Ketika kamu memilikinya, kamu tidak menyadarinya.") 
container_1.write(" ~~Boris Yeltsin")
container_1.write("Alangkah Baiknya untuk perhatikan udara yang kalian hirup.") 


with st.container(border=True):
    st.link_button("Cek Polutan Sekitar Di Sekitar-mu", "https://waqi.info/#google_vignette")

    co_slide = st.slider("Berapa Index polutan Karbonmoniksida Di Sekitar-mu", 1, 500, 25)
    st.write("Karbonmonoksida Di sekitarmu adalah =", co_slide)
    oz_slide = st.slider("Berapa Index polutan Ozon Di Sekitar-mu", 1, 500, 25)
    st.write("Karbonmonoksida Di sekitarmu adalah =", oz_slide)
    no2_slide = st.slider("Berapa Index polutan Nitrogendioksida Di Sekitar-mu", 1, 500, 25)
    st.write("Nitrogendioksida Di sekitarmu adalah =", no2_slide)
    pm25_slide = st.slider("Berapa Index polutan `Partikuler 2.5mm` Di Sekitar-mu", 1, 500, 25)
    st.write("`Partikuler 2.5mm` Di sekitarmu adalah =", pm25_slide)



    result_aqi = ''

    if st.button('Hasil Kualitas Udara Sekitar-mu'):
        aqi_result = read_1.predict([[co_slide, oz_slide, no2_slide, pm25_slide]])

        if (aqi_result < 50):
            result_aqi = 'Kualitas Udara Di sekitarmu Baik'
        elif (aqi_result < 100):
            result_aqi = 'Kualitas Udara Di sekitarmu Wajar'
        elif (aqi_result < 150):
            result_aqi = 'Kualitas Udara Di sekitarmu Sensitiv Bagi Kelompok Tertentu'
        elif (aqi_result < 200):
            result_aqi = 'Kualitas Udara Di sekitarmu Kurang Baik untuk Dihirup'
        elif (aqi_result < 250):
            result_aqi = 'Kualitas Udara Di sekitarmu Tidak Baik Untuk Kesehatan'
        else:
            result_aqi = 'Kualitas Udara Di sekitarmu Beracun Dan Fatal Untuk Kesehatan'

    st.success(result_aqi)
