import altair as alt
import streamlit as st


# remote geojson data object
url_geojson = 'https://raw.githubusercontent.com/denniskhoo/resources/main/Subzone_Census2010.geojson'
data_geojson_remote = alt.Data(url=url_geojson, format=alt.DataFormat(property='features',type='json'))

# chart object
chart = (
    alt.Chart(data_geojson_remote).mark_geoshape(
    )
#    .mark_geoshape(stroke="white", strokeWidth=2)
    .encode(
        color="properties.name:N"
    )
    .properties(
        projection={'type': 'identity', 'reflectY': True}
    )
)


st.altair_chart(chart)