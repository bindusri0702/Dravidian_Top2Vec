# Dravidian_Top2Vec
Top2Vec language modelling on Tamil and Telugu news data

[![](https://img.shields.io/pypi/v/top2vec.svg)](https://pypi.org/project/top2vec/)
[![](https://img.shields.io/github/license/bindusri0702/Dravidian_Top2Vec)](https://github.com/bindusri0702/Dravidian_Top2Vec/blob/main/LICENSE)


<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#top2vec">Top2Vec</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#UMAP">UMAP</a></li>
        <li><a href="#HDBSCAN">HDBSCAN</a></li>
      </ul>
    </li>
    <li><a href="#embedding">Embedding Models</a></li>
    <li><a href="#tokenizers">Tokenizers</a></li>
    <li><a href="#tamil">Top2Vec on Tamil news articles</a></li>
    <li><a href="#telugu">Top2Vec on Telugu news articles</a></li>
    <li><a href="#kannada">Top2Vec on Kannada news articles</a></li>
    <li><a href="#streamlit">Streamlit GUI</a></li>
    <li><a href="#acknowledgment">Acknowledgment</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
Top2Vec is an algorithm for **topic modeling** and **semantic search**. It automatically detects topics present in text
and generates jointly embedded topic, document and word vectors. Once you train the Top2Vec model 
you can:
* Get number of detected topics.
* Get topics.
* Get topic sizes. 
* Get hierarchichal topics. 
* Search topics by keywords.
* Search documents by topic.
* Search documents by keywords.
* Find similar words.
* Find similar documents.
* Expose model with [RESTful-Top2Vec](https://github.com/ddangelov/RESTful-Top2Vec)

See the [paper](http://arxiv.org/abs/2008.09470) for more details on how it works.

Benefits
--------
1. Automatically finds number of topics.
2. No stop word lists required.
3. No need for stemming/lemmatization.
4. Works on short text.
5. Creates jointly embedded topic, document, and word vectors. 
6. Has search functions built in.

This project uses the basic functions of Top2Vec like number of detected topics and name of topics detected for dravidian languages.

<p align="center">
  <img src="images/dravidian_top2vec.jpg" alt="DravidianTop2Vec" width="50%">
</p>
<h3 align="center">Dravidian - Top2Vec</h3>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

In this growing digital era, with the rapid increase in technology, data has also been growing. Organizing, searching and summarising large collections of text is a ubiquitous problem. To make this strenuous task possible, Topic modelling is used. Topic modelling is usually used on a large collection of data where organization and summarization of data cannot be done manually.This project is about identifying topic vectors by using joint document and word semantic embedding in Dravidian languages.With this paradigm, the number of topics is automatically determined without the need for stop-word lists, stemming, or lemmatization. The topic vectors that come from this are jointly embedded with the
word and document vectors, with the distance between them signifying semantic similarity.

### Prerequisites







<p align="right">(<a href="#readme-top">back to top</a>)</p>


