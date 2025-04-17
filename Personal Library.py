import streamlit as st

st.set_page_config(page_title="My Library", page_icon="📚", layout="wide")
st.title("📚 My Personal Library")

if "library" not in st.session_state:
    st.session_state.library = []

with st.sidebar:
    st.header("Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    if st.button("➕ Add"):
        if title and author:
            st.session_state.library.append({"title": title, "author": author})
            st.success(f"Added '{title}'")
        else:
            st.error("Both fields required")

st.subheader("Books Collection")
if not st.session_state.library:
    st.info("No books yet. Add some from the sidebar!")
else:
    for idx, book in enumerate(st.session_state.library):
        cols = st.columns([4, 3, 1])
        cols[0].write(f"**{book['title']}**")
        cols[1].write(f"*by {book['author']}*")
        if cols[2].button("❌", key=idx):
            st.session_state.library.pop(idx)
            st.experimental_rerun()
