## Using Models :
# Whisper
# ada embeddings
# gemini pro 
# + LangChain
############################# FIRST SCENARIO 
# 
#  
import streamlit as st
import videohelper
import raghelper

if "current_video_url" not in st.session_state:
    st.session_state.current_video_url = None
    st.session_state.current_transcript_docs = []
    st.session_state.videos = []


st.set_page_config(page_title="ASKTube: Conversation with Youtube!", layout="centered")
st.image(image="./img/app_banner.png")
st.title("ASKTube: Conversation with Youtube!")
st.divider()

tab_url, tab_search = st.tabs(["URL", "Search"])

with tab_url:
    video_url = st.text_input(label="Given a YouTube Video Address:", key="url_video_url")
    prompt = st.text_input(label="Ask Your Question:", key="url_prompt")
    submit_btn = st.button("Sor", key="url_submit")


    if submit_btn:
        st.video(data=video_url)
        st.divider()

        #FIRST STEP : video > audio > text
        if st.session_state.current_video_url != video_url:

            with st.spinner("STEP-1: Preparing the text..."):
                video_transcript_docs = videohelper.get_video_transcript(url=video_url)
                st.session_state.current_transcript_docs = video_transcript_docs
        st.succes("Video transcript is saved!")
        st.divider()

        st.session_state.current_video_url = video_url

        #SECOND STEP : text > RAG
        with st.spinner("STEP-2: Answering your question..."):
            AI_Response, relevant_documents = raghelper.rag_with_video_transcript(transcript_docs=st.session_state.current_transcript_docs, prompt=prompt)
        st.info("ANSWER:")
        st.markdown(AI_Response)
        st.divider()

        for doc in relevant_documents:
            st.warning("REFERENCES:")
            st.caption(doc.page_content)
            st.markdown(f"Source: {doc.metadata}")
            st.divider()

############################# SECOND SCENARIO 
# 
#  

with tab_search:
    col_left, col_center, col_right = st.columns([20,1,10])

    with col_left:

        st.subheader("Video Searching Functionalities")
        st.divider()

        search_term = st.text_input(label="Please given keywords:", key="search_term")
        video_count = st.slider(label="Result Count", min_values=1, max_value=5, key="search_video_count")
        sorting_options = ["En İlgili", "Tarihe Göre", "İzlenmes Sayisi", "Beğeni Sayisi"]
        sorting_criteria = st.selectbox(label="Sıralama Ölçütü", options=sorting_options)
        search_btn = st.button(label="Search Video", key="search_button")
        st.divider()

        if search_btn:
            st.session_state.videos = []
            videolist = videohelper.get_videos_for_search_term(search_term=search_term, video_count=video_count, sorting_criteria=sorting_criteria)
            for video in videolist:
                st.seesion_state.videos.append(video)


        video_urls  = []
        video_titles = {}

        for video in st.session_state.videos:
            video_urls.append(video.video_url)
            video_titles.update({video.video_url:video.video_title})

        selected_video = st.selectbox(
            label="Select the Video for Chatting: ",
            options=video_urls,
            format_func=lambda url: video_titles[url],
            key="search_selectbox"

        )

        if selected_video:
            search_prompt = st.text_input(label="Ask a Guestion:", key="search_prompt")
            search_ask_btn = st.button(label="Ask", key="search_ask_button")

            if search_ask_btn:
                st.caption("Selected Video")
                st.video(data=selected_video)
                st.divider()

                if st.session_state.current_video_url != video_url:
                    with st.spinner("STEP-1: Preparing the text..."):
                        video_transcript_docs = videohelper.get_video_transcript(url=video_url)
                        st.session_state.current_transcript_docs = video_transcript_docs
                    st.succes("Video transcript is saved!")
                    st.divider()
                    st.session_state.current_video_url = video_url

                with st.spinner("STEP-2: Answering your question..."):
                    AI_Response, relevant_documents = raghelper.rag_with_video_transcript(transcript_docs=st.session_state.current_transcript_docs, prompt=prompt)
                st.info("ANSWER:")
                st.markdown(AI_Response)
                st.divider()

                for doc in relevant_documents:
                    st.warning("REFERENCES:")
                    st.caption(doc.page_content)
                    st.markdown(f"Source: {doc.metadata}")
                    st.divider()

    with col_center:
        st.empty()

    with col_right:

        st.subheader("Releated Videos")
        st.divider()

        for i, video in enumerate(st.session_state.videos):
            st.info(f"video No: {i+1}")
            st.video(data=video.video_url)
            st.caption(f"Video Title: {video.video_title}")
            st.caption(f"Channel Name: {video.channel_name}")
            st.caption(f"Duration: {video.duration}")
            st.divider()