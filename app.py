# import os
# import sys
# import pickle
# import streamlit as st
# import numpy as np
# from books_recommender.logger.log import logging
# from books_recommender.config.configuration import AppConfiguration
# from books_recommender.pipeline.training_pipeline import TrainingPipeline
# from books_recommender.exception.exception_handler import AppException


# class Recommendation:
#     def __init__(self,app_config = AppConfiguration()):
#         try:
#             self.recommendation_config= app_config.get_recommendation_config()
#         except Exception as e:
#             raise AppException(e, sys) from e


#     def fetch_poster(self,suggestion):
#         try:
#             book_name = []
#             ids_index = []
#             poster_url = []
#             book_pivot =  pickle.load(open(self.recommendation_config.book_pivot_serialized_objects,'rb'))
#             final_rating =  pickle.load(open(self.recommendation_config.final_rating_serialized_objects,'rb'))

#             for book_id in suggestion:
#                 book_name.append(book_pivot.index[book_id])

#             for name in book_name[0]: 
#                 ids = np.where(final_rating['title'] == name)[0][0]
#                 ids_index.append(ids)

#             for idx in ids_index:
#                 url = final_rating.iloc[idx]['image_url']
#                 poster_url.append(url)

#             return poster_url
        
#         except Exception as e:
#             raise AppException(e, sys) from e
        


#     def recommend_book(self,book_name):
#         try:
#             books_list = []
#             model = pickle.load(open(self.recommendation_config.trained_model_path,'rb'))
#             book_pivot =  pickle.load(open(self.recommendation_config.book_pivot_serialized_objects,'rb'))
#             book_id = np.where(book_pivot.index == book_name)[0][0]
#             distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

#             poster_url = self.fetch_poster(suggestion)
            
#             for i in range(len(suggestion)):
#                     books = book_pivot.index[suggestion[i]]
#                     for j in books:
#                         books_list.append(j)
#             return books_list , poster_url   
        
#         except Exception as e:
#             raise AppException(e, sys) from e


#     def train_engine(self):
#         try:
#             obj = TrainingPipeline()
#             obj.start_training_pipeline()
#             st.text("Training Completed!")
#             logging.info(f"Recommended successfully!")
#         except Exception as e:
#             raise AppException(e, sys) from e

    
#     def recommendations_engine(self,selected_books):
#         try:
#             recommended_books,poster_url = self.recommend_book(selected_books)
#             col1, col2, col3, col4, col5 = st.columns(5)
#             with col1:
#                 st.text(recommended_books[1])
#                 st.image(poster_url[1])
#             with col2:
#                 st.text(recommended_books[2])
#                 st.image(poster_url[2])

#             with col3:
#                 st.text(recommended_books[3])
#                 st.image(poster_url[3])
#             with col4:
#                 st.text(recommended_books[4])
#                 st.image(poster_url[4])
#             with col5:
#                 st.text(recommended_books[5])
#                 st.image(poster_url[5])
#         except Exception as e:
#             raise AppException(e, sys) from e



# if __name__ == "__main__":
#     st.header('End to End Books Recommender System')
#     st.text("This is a collaborative filtering based recommendation system!")

#     obj = Recommendation()

#     #Training
#     if st.button('Train Recommender System'):
#         obj.train_engine()

#     book_names = pickle.load(open(os.path.join('templates','book_names.pkl') ,'rb'))
#     selected_books = st.selectbox(
#         "Type or select a book from the dropdown",
#         book_names)
    
#     #recommendation
#     if st.button('Show Recommendation'):
#         obj.recommendations_engine(selected_books)


import os
import sys
import pickle
import streamlit as st
import numpy as np

from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Book Recommender",
    page_icon="📚",
    layout="wide"
)


# -------------------------------------------------
# Custom CSS (Clean, Product-Style)
# -------------------------------------------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-bottom: 0px;
}
.sub-title {
    text-align: center;
    color: #b3b3b3;
    margin-top: 5px;
    margin-bottom: 30px;
}
.book-card {
    text-align: center;
    padding: 8px;
}
.book-title {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 10px;
}
.sidebar-title {
    font-size: 22px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# Recommendation Class (LOGIC UNCHANGED)
# -------------------------------------------------
class Recommendation:
    def __init__(self, app_config=AppConfiguration()):
        try:
            self.recommendation_config = app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def fetch_poster(self, suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []

            book_pivot = pickle.load(
                open(self.recommendation_config.book_pivot_serialized_objects, 'rb')
            )
            final_rating = pickle.load(
                open(self.recommendation_config.final_rating_serialized_objects, 'rb')
            )

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])

            for name in book_name[0]:
                ids = np.where(final_rating['title'] == name)[0][0]
                ids_index.append(ids)

            for idx in ids_index:
                poster_url.append(final_rating.iloc[idx]['image_url'])

            return poster_url

        except Exception as e:
            raise AppException(e, sys) from e

    def recommend_book(self, book_name):
        try:
            books_list = []

            model = pickle.load(
                open(self.recommendation_config.trained_model_path, 'rb')
            )
            book_pivot = pickle.load(
                open(self.recommendation_config.book_pivot_serialized_objects, 'rb')
            )

            book_id = np.where(book_pivot.index == book_name)[0][0]
            _, suggestion = model.kneighbors(
                book_pivot.iloc[book_id, :].values.reshape(1, -1),
                n_neighbors=6
            )

            poster_url = self.fetch_poster(suggestion)

            for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    books_list.append(j)

            return books_list, poster_url

        except Exception as e:
            raise AppException(e, sys) from e

    def train_engine(self):
        try:
            TrainingPipeline().start_training_pipeline()
            logging.info("Training completed successfully")
        except Exception as e:
            raise AppException(e, sys) from e

    def show_recommendations(self, selected_book):
        books, posters = self.recommend_book(selected_book)

        st.markdown("## ✨ Recommended for You")

        cols = st.columns(5)

        for i, col in enumerate(cols):
            with col:
                st.markdown(
                    f"<div class='book-card'>"
                    f"<div class='book-title'>{books[i+1]}</div>"
                    f"</div>",
                    unsafe_allow_html=True
                )
                st.image(posters[i+1], use_container_width=True)


# -------------------------------------------------
# Header Section
# -------------------------------------------------
st.markdown("<div class='main-title'>📚 Book Recommendation System</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub-title'>Find books similar to the ones you love</div>",
    unsafe_allow_html=True
)

st.divider()


# -------------------------------------------------
# Sidebar (REAL APP STYLE)
# -------------------------------------------------
st.sidebar.markdown("<div class='sidebar-title'>📖 Book Recommender</div>", unsafe_allow_html=True)
st.sidebar.markdown("Personalized recommendations using collaborative filtering")

obj = Recommendation()

st.sidebar.divider()

if st.sidebar.button("🚀 Train Model", use_container_width=True):
    with st.sidebar:
        with st.spinner("Training in progress..."):
            obj.train_engine()
        st.success("Model trained successfully!")

st.sidebar.divider()

st.sidebar.markdown(
    """
    **How it works**
    - Uses collaborative filtering  
    - Based on user–book ratings  
    - KNN similarity search  
    """
)


# -------------------------------------------------
# Main Input Section
# -------------------------------------------------
st.markdown("### 🔍 Choose a Book")

book_names = pickle.load(
    open(os.path.join("templates", "book_names.pkl"), 'rb')
)

selected_book = st.selectbox(
    "Search or select a book",
    book_names
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🎯 Get Recommendations", use_container_width=True):
    with st.spinner("Finding books you’ll love..."):
        obj.show_recommendations(selected_book)
