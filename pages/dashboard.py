import streamlit as st

# Logout Function
def logout():
    st.session_state.authenticated = False
    st.session_state.username = None
    st.switch_page("login.py")  # Redirect to login

# Ensure User is Logged In
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.switch_page("login.py")  # Redirect to login page if not authenticated

# Set Streamlit Page Config
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="centered")

# Display Welcome Message
st.title(f"👋 Welcome, {st.session_state.username}")

# Create Two Large Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("📝 Submit Your Request", use_container_width=True):
        st.switch_page("pages/submit_request.py")  # Redirect to request submission page

with col2:
    if st.button("📊 Analytics", use_container_width=True):
        st.switch_page("pages/analytics.py")  # Redirect to analytics page

# Logout Button (Centered)
st.divider()
st.button("🚪 Logout", on_click=logout, use_container_width=True)
