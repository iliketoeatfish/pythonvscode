import streamlit as st #webpage for python app
menu = st.sidebar.selectbox('Menu',['Upload Image','Upload Audio','Upload Video','Upload CSV'])

if menu == 'Upload Image':
    st.header("Upload images to view")

    uploadimage = st.file_uploader('Choose image to upload',type=['jpg','png','jpeg'])

    if uploadimage: #if uploadimage has data
     st.image(uploadimage)




if menu == 'Upload Audio':
   st.header("Upload audio to play")

   uploadaudio = st.file_uploader('Choose audio to upload',type=['mp3'])

   if uploadaudio:
      st.audio(uploadaudio)


if menu == 'Upload Video':
   st.header("Upload video to play")

   youtubelink = st.text_input('Paste your youtube link here')
   if st.button("Play youtube video"):
        if youtubelink:
         st.video(youtubelink)
    
        else:
            st.error("No video link in the box")
         



