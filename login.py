import streamlit as st
import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize Session State for Authentication
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None
# Streamlit UI
st.set_page_config(page_title="Login", page_icon="🔐", layout="centered")

# HideSidebar 
if not st.session_state.authenticated:
    hide_sidebar = """
        <style>
            [data-testid="stSidebar"] {display: none;}
        </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)

# Logout Mechanism
def logout():
    st.session_state.authenticated = False
    st.session_state.username = None
    st.rerun()  # Refresh the page to show login form again

# If User is Logged In → Show Dashboard
if st.session_state.authenticated:
    st.title(f"Welcome, {st.session_state.username} 👋")
    st.switch_page('pages/dashboard.py'); 
    # Logout Button
    if st.button("Logout"):
        logout()

# If User is Not Logged In → Show Login Form
else:
    st.title("🔐 Secure Login")

    with st.container():
        st.subheader("Enter Your Credentials")

        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", placeholder="Enter your password", type="password")

        login_button = st.button("Login")

    # Authentication Logic
    if login_button:
        # conn = get_connection()  # Get connection from pool
        # cursor = conn.cursor()

        # cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        # result = cursor.fetchone()

        if username == "admin" and password == "admin":
            st.session_state.authenticated = True  # Mark user as authenticated
            st.session_state.username = username
            st.success("✅ Login Successful!")
            st.switch_page("pages/dashboard.py")
            #st.rerun()  
        else:
            st.error("❌ Invalid Username or Password")
        # cursor.close()
        # close_connection(conn)  # Return connection to pool
