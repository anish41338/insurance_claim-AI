import streamlit as st
import requests

# Streamlit Page Config
st.set_page_config(
    page_title="Claims Automation UI",
    layout="centered",
    page_icon="🛰️"
)

# CSS for enhanced glassmorphism + visual polish + animations
st.markdown("""
    <style>
    @import url('https://fonts.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    :root {
        --primary-color: #0097A7;
        --secondary-color: #00796B;
        --text-color: #2c3e50;
        --background-gradient-start: #e0f7fa;
        --background-gradient-end: #ffffff;
        --card-background: rgba(255, 255, 255, 0.85); /* More transparent for glass effect */
        --card-border: 1px solid rgba(255, 255, 255, 0.3);
        --card-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.1); /* Stronger shadow */
        --border-radius: 16px;
    }

    html, body, [class^="st"] {
        font-family: 'Inter', sans-serif !important;
        background: linear-gradient(to bottom right, var(--background-gradient-start), var(--background-gradient-end));
        color: var(--text-color);
        background-attachment: fixed; /* Ensures gradient fills whole background */
    }

    h1, h2, h3, h4 {
        font-weight: 700;
        color: var(--text-color);
        margin-bottom: 10px;
    }

    /* Main Title Styling */
    .app-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1c1c1c; /* A bit darker for contrast */
        text-align: center;
        margin-bottom: 30px;
        background: linear-gradient(45deg, #00BCD4, #00796B); /* Gradient for title */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.2rem;
        color: var(--secondary-color);
        border-bottom: 2px solid rgba(0, 121, 107, 0.2);
        padding-bottom: 5px;
    }

    .card {
        background-color: var(--card-background);
        border-radius: var(--border-radius);
        padding: 28px; /* Slightly more padding */
        margin: 25px 0; /* More margin for separation */
        box-shadow: var(--card-shadow);
        border: var(--card-border);
        backdrop-filter: blur(10px); /* Glassmorphism blur */
        -webkit-backdrop-filter: blur(10px); /* Safari support */
        transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }

    .card:hover {
        transform: translateY(-5px); /* Lift effect on hover */
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.15);
    }

    .stButton button {
        background-color: var(--primary-color);
        color: white;
        border: none;
        padding: 12px 28px; /* Larger buttons */
        border-radius: 10px; /* More rounded */
        font-weight: 600;
        font-size: 1.1rem;
        transition: 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 151, 167, 0.3);
    }

    .stButton button:hover {
        background-color: var(--secondary-color);
        box-shadow: 0 6px 15px rgba(0, 121, 107, 0.4);
        transform: translateY(-2px);
    }

    .stTextInput>div>div>input, .stFileUploader>div>div {
        background-color: rgba(255, 255, 255, 0.7) !important; /* Semi-transparent input */
        border: 1.5px solid rgba(176, 190, 197, 0.5) !important;
        border-radius: 10px;
        padding: 12px;
        color: var(--text-color);
    }

    .stAlert {
        border-radius: 12px;
        background-color: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(5px);
        -webkit-backdrop-filter: blur(5px);
    }

    ::selection {
        background-color: #b2dfdb;
        color: var(--text-color);
    }

    /* Pulsating animation for processing status */
    @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.03); opacity: 0.8; }
        100% { transform: scale(1); opacity: 1; }
    }

    .pulsating {
        animation: pulse 1.5s infinite ease-in-out;
    }

    /* Neon effect (optional, if you want to keep a touch of it) */
    .neon {
        text-shadow:
            0 0 7px #00BCD4,
            0 0 10px #00BCD4,
            0 0 21px #00BCD4,
            0 0 42px #00BCD4,
            0 0 82px #00BCD4,
            0 0 92px #00BCD4,
            0 0 102px #00BCD4,
            0 0 151px #00BCD4;
    }

    /* Placeholder/Welcome Content */
    .welcome-card {
        background-color: var(--card-background);
        border-radius: var(--border-radius);
        padding: 30px;
        margin: 40px 0;
        box-shadow: var(--card-shadow);
        border: var(--card-border);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        text-align: center;
    }

    .welcome-card h2 {
        color: var(--primary-color);
        font-size: 2rem;
        margin-bottom: 15px;
    }

    .welcome-card p {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)


# App Title
st.markdown('<h1 class="app-title">🚀 Insurance Claims Automation System</h1>', unsafe_allow_html=True)

# File Uploader Card
st.markdown('<div class="card">', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "📤 Upload Claim Document",
    type=["png", "jpg", "jpeg", "txt", "pdf"], # Added PDF as a common document type
    help="Select an image, text, or PDF file for claim processing."
)
st.markdown('</div>', unsafe_allow_html=True) # Close file uploader card


# Conditional Welcome Content - THIS IS THE CRITICAL CHANGE
if uploaded_file is None:
    st.markdown("""
        <div class="welcome-card">
            <h2>Welcome to the Future of Claims Processing!</h2>
            <p>Our intelligent system automates the processing of insurance claims, making it faster and more efficient.</p>
            <p>Simply upload a claim document (image, text, or PDF) below, and watch as our AI instantly extracts key data, classifies the claim, determines compliance, and suggests the optimal routing.</p>
            <p><b>Get started by uploading your first document!</b></p>
        </div>
    """, unsafe_allow_html=True)


if uploaded_file is not None:
    st.markdown('<div class="card pulsating">', unsafe_allow_html=True) # Apply pulsating to processing card
    st.info("Processing claim...", icon="🔎")
    st.markdown('</div>', unsafe_allow_html=True)


    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    try:
        response = requests.post("http://localhost:8000/process-claim/", files=files)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        result = response.json()
    except requests.exceptions.ConnectionError:
        st.error("❌ Connection Error: Could not connect to the backend server. Please ensure the server is running.")
        result = None
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error during request to backend: {e}")
        result = None
    except ValueError: # Catches JSON decoding errors
        st.error("❌ Error: Received malformed response from the backend server. Please check the server logs.")
        result = None

    if result:
        st.success("Claim processed successfully!", icon="✅")

        # Extracted Data Section
        st.markdown('---') # Separator
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📄 Extracted Data</div>', unsafe_allow_html=True)
        if result["extracted_data"].get("raw_text"):
            st.code(result["extracted_data"].get("raw_text"), language="text")
        else:
            st.warning("No raw text extracted. This might be normal for image-only documents, or an issue with OCR.")
        st.markdown('</div>', unsafe_allow_html=True)

        # Classification & Routing Section
        st.markdown('---') # Separator
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📦 Classification & Routing</div>', unsafe_allow_html=True)
        st.json({ # Using st.json for better display of dictionary
            "Category": result["classification"].get("category", "N/A"),
            "Priority": result["classification"].get("priority", "N/A"),
            "Route": result["route"]
        })
        st.markdown('</div>', unsafe_allow_html=True)

        # Policy Compliance Section
        st.markdown('---') # Separator
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">🛡️ Policy Compliance</div>', unsafe_allow_html=True)
        compliance = result.get("compliance_check", {})
        if compliance.get('compliant'):
            st.success(f"✅ Compliant: {compliance.get('compliant', False)}. Notes: {compliance.get('notes', 'N/A')}", icon="✅")
        else:
            st.error(f"❌ Compliant: {compliance.get('compliant', False)}. Notes: {compliance.get('notes', 'N/A')}", icon="⚠️")
        st.markdown('</div>', unsafe_allow_html=True)