import streamlit as st

# Set Page Configuration
st.set_page_config(page_title="Submit Request", page_icon="📝", layout="centered")

st.title("📝 Submit Your Request")

# Allowed File Types (Audio, Video, CSV, PDF, etc.)
allowed_file_types = ["mp3", "wav", "mp4", "mkv", "avi", "csv", "pdf", "docx", "xlsx"]

# Multi-File Upload Section
uploaded_files = st.file_uploader(
    "Upload Files",
    accept_multiple_files=True,
    type=allowed_file_types
)

# Multi-Select Text Input (Allows Users to Enter Custom Options)
st.subheader("📌 Enter Request Types (Multiple Allowed)")
request_types = st.text_area("Enter Professors name with the required no of avatars for each. Please write each request in a different line. Add any other request here", placeholder="Example:\nEX1\nEX2")

# Convert Multiline Input into a List
selected_requests = [req.strip() for req in request_types.split("\n") if req.strip()]

# Display Uploaded Files and Selected Options
st.divider()

if uploaded_files:
    st.subheader("📂 Uploaded Files:")
    for file in uploaded_files:
        st.write(f"✔️ {file.name}")

if selected_requests:
    st.subheader("📌 Selected Request Types:")
    st.write(", ".join(selected_requests))
    
# Submit Button
if st.button("📤 Submit Request"):
    if uploaded_files and selected_requests:
        st.success("✅ Your request has been submitted successfully!")
    else:
        st.error("⚠️ Please upload files and enter at least one request type.")