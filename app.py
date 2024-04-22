import streamlit as st
import pickle
import pandas as pd
import pydeck as pdk

# Recommendation function
def recommend(museum):
    museum_index = museums[museums['Museum_Name'] == museum].index[0]
    distances = similarity[museum_index]
    museums_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_museums = []
    for i in museums_list:
        recommended_museums.append(museums.iloc[i[0]].Museum_Name)
    return recommended_museums

# Load data
museums_dict = pickle.load(open('museums_dict.pkl', 'rb'))
museums = pd.DataFrame(museums_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit page setup, create logo and title
col1, col2 = st.columns([1, 7])
with col1:
    st.image("Fordham-University-Logo-1907.png", width=100)
with col2:
    st.title('Museum Recommender System')
    st.markdown("<br>", unsafe_allow_html=True)

selected_museum_name = st.selectbox(
     'Select a museum from these options:',
     museums['Museum_Name'].values)

if st.button('Recommend'):
    names = recommend(selected_museum_name)
    # Filter and sort the museums results by rank
    recommended_museums = museums[museums['Museum_Name'].isin(names)].sort_values('Rank')
    recommended_museums = recommended_museums.head(5)

    # Prepare data for the map
    map_data_with_labels = pd.DataFrame({
        'lat': recommended_museums['Latitude'],
        'lon': recommended_museums['Longitude'],
        'name': recommended_museums['Museum_Name']
    })
    # centeral the map
    view_state = pdk.ViewState(
        latitude=39.50, 
        longitude=-98.35, 
        zoom=3
    )
    # Display Names on map
    text_layer = pdk.Layer(
        "TextLayer",
        data=map_data_with_labels,
        get_position='[lon, lat]',
        get_text='name',
        get_size=12,
        get_color=[165, 42, 42, 255],
        get_text_anchor='"middle"',
        get_alignment_baseline='"center"',
        size_scale=1,
        billboard=False,
        background_color=[255, 255, 255, 255]
    )
    # Build the overall map
    r = pdk.Deck(
        layers=[text_layer],
        initial_view_state=view_state,
        map_style='mapbox://styles/mapbox/light-v9'
    )
    st.markdown("---")
    st.markdown("<h2 style='text-align: center; color: black;'>Museum Explorer Map</h1>", unsafe_allow_html=True)
    st.pydeck_chart(r)
    st.markdown("---")

    # Display recommendations
    for _, museum_info in recommended_museums.iterrows():

        # Use HTML to center the image
        st.markdown(
            f"<div style='text-align: center;'>"
            f"<img src='{museum_info['Photo_URL']}' style='max-width: 100%; height: auto;'>"
            f"</div>", 
            unsafe_allow_html=True
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center'>{museum_info['Museum_Name']}</h3>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(f"**Rank:** {museum_info['Rank']}")
        st.markdown(f"**Rating:** {museum_info['Rating']:.2f}")
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown(f"**Best for:** {museum_info['Tourist_Type']}", unsafe_allow_html=True)
        st.markdown(f"**Address:** {museum_info['Address']}")
        st.markdown(f"**Description:** {museum_info['Description']}")

        st.markdown("---")

        #st.markdown("<br>", unsafe_allow_html=True)  # UI design bottom space