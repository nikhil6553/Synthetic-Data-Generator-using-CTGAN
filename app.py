import streamlit as st
import pandas as pd
import pickle
from io import BytesIO

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Synthetic Data Generator",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------
# Title
# -----------------------------
st.title("🧬 Synthetic Data Generator using CTGAN")

st.markdown("""
This application generates synthetic data using a trained CTGAN model.
Upload your trained model and generate artificial datasets instantly.
""")

# -----------------------------
# Load Model Function
# -----------------------------
@st.cache_resource
def load_model(model_file):
    model = pickle.load(model_file)
    return model

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("⚙️ Settings")

uploaded_model = st.sidebar.file_uploader(
    "Upload Trained CTGAN Model (.pkl)",
    type=["pkl"]
)

num_samples = st.sidebar.number_input(
    "Number of Synthetic Samples",
    min_value=1,
    max_value=100000,
    value=1000,
    step=100
)

# -----------------------------
# Main Logic
# -----------------------------
if uploaded_model is not None:

    try:
        # Load Model
        model = load_model(uploaded_model)

        st.success("✅ Model loaded successfully!")

        # -----------------------------
        # Generate Synthetic Data
        # -----------------------------
        if st.button("🚀 Generate Synthetic Data"):

            with st.spinner("Generating synthetic data..."):

                st.session_state.synthetic_data = model.sample(num_samples)

            st.success(
                f"✅ Successfully generated {num_samples} synthetic samples!"
            )

        # -----------------------------
        # Display Data If Available
        # -----------------------------
        if "synthetic_data" in st.session_state:

            synthetic_data = st.session_state.synthetic_data

            # -----------------------------
            # Dataset Preview
            # -----------------------------
            st.subheader("📊 Synthetic Dataset Preview")

            st.dataframe(
                synthetic_data,
                use_container_width=True
            )

            # -----------------------------
            # Dataset Information
            # -----------------------------
            st.subheader("📌 Dataset Information")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Rows", synthetic_data.shape[0])

            with col2:
                st.metric("Columns", synthetic_data.shape[1])

            with col3:
                st.metric(
                    "Missing Values",
                    synthetic_data.isnull().sum().sum()
                )

            # -----------------------------
            # Statistical Summary
            # -----------------------------
            st.subheader("📈 Statistical Summary")

            st.dataframe(
                synthetic_data.describe(include="all"),
                use_container_width=True
            )

            # -----------------------------
            # Visualizations
            # -----------------------------
            st.subheader("📉 Visualizations")

            numeric_columns = synthetic_data.select_dtypes(
                include=["int64", "float64"]
            ).columns.tolist()

            if len(numeric_columns) > 0:

                selected_column = st.selectbox(
                    "Select Numeric Column",
                    numeric_columns
                )

                st.bar_chart(
                    synthetic_data[selected_column]
                )

            else:
                st.info(
                    "No numeric columns available for visualization."
                )

            # -----------------------------
            # Download Section
            # -----------------------------
            st.subheader("⬇️ Download Synthetic Data")

            # CSV Download
            csv = synthetic_data.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(
                label="📥 Download CSV File",
                data=csv,
                file_name="synthetic_data.csv",
                mime="text/csv"
            )

            # Excel Download
            excel_buffer = BytesIO()

            with pd.ExcelWriter(
                excel_buffer,
                engine="openpyxl"
            ) as writer:

                synthetic_data.to_excel(
                    writer,
                    index=False,
                    sheet_name="SyntheticData"
                )

            st.download_button(
                label="📥 Download Excel File",
                data=excel_buffer.getvalue(),
                file_name="synthetic_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:

        st.error(
            f"❌ Error loading model or generating data:\n\n{e}"
        )

else:
    st.info(
        "👈 Upload your trained CTGAN model (.pkl) from the sidebar to begin."
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.markdown(
    "Developed using Streamlit + CTGAN for Synthetic Data Generation"
)