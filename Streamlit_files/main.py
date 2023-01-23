# Imports

import pandas as pd
import streamlit as st
import methods.functions as functions
st.title('Dravidian Top2Vec')
# creating a side bar 
st.sidebar.info("Team 5 - Mini Project")
st.sidebar.info("Mentor : Dr. Premjith B")
# Adding an image to the side bar
st.sidebar.header("Topic Modelling for Dravidian Languages using Dravidian Top2Vec") 
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFdnvMK8fWksE-qhdPatK1Z-iqzaTKJfEekmOGbOfubH-kTLcBrWPRH2gOo7uD_rQdUIY&usqp=CAU", width=None)
col3, mid, col4 = st.sidebar.columns([1,1,20])
with col3:
	st.sidebar.subheader("Top2Vec Github : ")
with col4:
	st.sidebar.markdown("[![Github](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJGtP-Pq0P67Ptyv3tB7Zn2ZYPIT-lPGI7AA&usqp=CAU)](https://github.com/ddangelov/Top2Vec)")

data = st.file_uploader('Upload Dataset Here', accept_multiple_files=False, type={"csv"})

if data is not None:
    tamil_data = pd.read_csv(data)
    st.write(tamil_data.head())
    st.write('Reading the Documents...')
    documents = list(tamil_data.news_article)
    documents = documents[0:5000]
    option = st.selectbox('Select an Embedding Model of your choice', ('Select a valid model','IndicBert', 'Muril-base', 'Muril-large','Opus-mt-en-dra'))
    embdng_path = ''
    umap_args = {}
    hdbscan_args = {}
    if option == "IndicBert":
        embdng_path = 'https://huggingface.co/ai4bharat/indic-bert'
    elif option == "Muril-base":
        embdng_path = 'https://huggingface.co/google/muril-base-cased'
    elif option == "Muril-large":
        embdng_path = 'https://huggingface.co/google/muril-large-cased'
    elif option == "Opus-mt-en-dra":
        embdng_path = 'https://huggingface.co/Helsinki-NLP/opus-mt-en-dra'
    if option != 'Select a valid model':
        opt = st.selectbox('Selecting UMAP and HDBSCAN hyperparameters',('Select an option','Use Default','Play around and experiment'))
        if opt == 'Use Default':
            umap_args = dict({'n_neighbors':20, 'min_dist':0.2, 'n_components':20, 'metric':'cosine'})
            hdbscan_args = dict({'min_cluster_size':50, 'min_samples':5, 'metric':'euclidean', 'cluster_selection_method': 'eom'})
        elif opt == 'Play around and experiment':
            st.write("Provide UMAP parameters")
            u1 = st.number_input('n_neighbors : ')
            u2 = st.number_input('min_dist : ')
            u3 = st.number_input('n_components : ')
            u4 = st.text_input('UMAP metric : euclidian/cosine')
            st.write("Provide HDBSCAN parameters")
            h1 = st.number_input('min_cluster_size : ')
            h2 = st.number_input('min_samples : ')
            h3 = st.text_input('HDBSCAN metric : euclidian/cosine')
            umap_args = dict({'n_neighbors':u1, 'min_dist':u2, 'n_components':u3, 'metric':u4})
            hdbscan_args = dict({'min_cluster_size':h1, 'min_samples':h2, 'metric':h3, 'cluster_selection_method': 'eom'})
        elif opt == "Select an option":
            st.warning("Please select the mode of setting the hyperparameters")
        if(opt != "Select an option"):
            st.info("Please note that the tokenizer has been experimentally set to Muril-large cased")
            st.write('Applying Top2Vec....')
            with st.spinner("Applying Top2Vec"):
                dstl = functions.Top2Vec(documents,embedding_model_path = embdng_path,umap_args = umap_args, hdbscan_args = hdbscan_args,tokenizer = functions.custom_tokenizer) #, use_embedding_model_tokenizer=True, tokenizer = tokenizer )
            topic_words, word_scores, topic_nums = dstl.get_topics()
            st.info("Topic Vectors generated succcessfully by Dravidian Top2Vec are : ")
            st.success(topic_words)
    else:
        st.warning("You haven't selected an embedding model")

