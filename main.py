import streamlit as st
from new import *
from scrap_link import *

st.header("PEACE 🎶🎷🎺🎸")
st.caption("Enter your any keyword of song and search it ")

if "video" not in st.session_state:
    st.session_state["video"] = []

if "title" not in st.session_state:
    st.session_state["title"] = "None"

if "audio" not in st.session_state:
    st.session_state["audio"] = None

if 'Video_scrap' not in st.session_state:
    st.session_state.Video_scrap = Scrapper()

# if 'Audio_scrap' not in st.session_state:
#     st.session_state.Audio_scrap = AudioScrap()

# scrapper = Scrapper()

search_query = st.text_input("Enter the song keyword ")

if st.button("Search",type="primary"):
    with st.status("Searching for the song..."):
        st.session_state["video"] = st.session_state.Video_scrap.FetchLinks(search_query)
        st.write("Song Found")
        # for i in range(len(st.session_state["video"])):
        #     st.session_state["video"][i][0] = st.session_state.Audio_scrap.stream_audio(st.session_state["video"][i][0])

        # print(st.session_state["video"])


if st.session_state["video"] !=[]:
    links = st.session_state["video"]
    st.text("Song Found ")
    tab = st.columns((1,9))
    if tab[0].button("▶"):
        st.session_state["audio"] = links[0][0]
        st.session_state["title"] = links[0][1]
    tab[1].write(links[0][1])

st.write("---")
st.write(f"Currently Playing : {st.session_state['title']}")
if st.session_state["audio"] != None:
    st.audio(st.session_state["audio"],autoplay=True,loop=True)
    
