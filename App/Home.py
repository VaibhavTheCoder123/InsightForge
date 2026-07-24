from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="InsightChurn",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).parent
ASSET_DIR = BASE_DIR / "assets"
CSS_FILE = BASE_DIR / "style.css"

if CSS_FILE.exists():
    st.markdown(
        f"<style>{CSS_FILE.read_text()}</style>",
        unsafe_allow_html=True
    )

logo = ASSET_DIR / "logo.png"

if logo.exists():
    st.sidebar.image(str(logo), width=90)

st.sidebar.title("InsightChurn")

st.sidebar.markdown(
"""
AI Powered Customer Analytics

---

Navigate using the pages below.
"""
)

st.title("📊 Customer Churn Analytics Platform")

st.caption(
    "AI Powered Predictive Analytics • Machine Learning • Business Intelligence"
)

st.divider()

left, right = st.columns([2, 1], gap="large")

with left:

    st.markdown(
"""
## Welcome

InsightChurn is a customer analytics platform that predicts customer churn using Machine Learning.

The system combines predictive analytics with interactive business dashboards to help organizations reduce customer attrition and improve retention strategies.

### Key Capabilities

- Predict customer churn
- Analyze customer behaviour
- Explore interactive dashboards
- Evaluate ML models
- Generate business insights
"""
    )

with right:

    st.info(
"""
### Project Summary

**Dataset**

IBM Telco Customer Churn

**Customers**

7,043

**Features**

21

**Best Model**

Logistic Regression

**Accuracy**

80.70%
"""
    )

st.divider()

st.header("Key Metrics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", "7,043")
c2.metric("Features", "21")
c3.metric("Accuracy", "80.70%")
c4.metric("Models Compared", "3")

st.divider()

st.header("Project Workflow")

st.code(
"""
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Feature Engineering
      │
      ▼
Machine Learning
      │
      ▼
Model Evaluation
      │
      ▼
Power BI Dashboard
      │
      ▼
Streamlit Deployment
""",
language="text"
)

st.divider()

st.header("Machine Learning Models")

m1, m2, m3 = st.columns(3)

with m1:

    st.success(
"""
### Logistic Regression

Accuracy

**80.70%**

✔ Selected Model
"""
    )

with m2:

    st.info(
"""
### Random Forest

Accuracy

**78.99%**
"""
    )

with m3:

    st.info(
"""
### Decision Tree

Accuracy

**74.17%**
"""
    )

st.divider()

st.header("Technology Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:

    st.markdown(
"""
### Programming

- Python
- Pandas
- NumPy
"""
    )

with t2:

    st.markdown(
"""
### Machine Learning

- Scikit-Learn
- Joblib
"""
    )

with t3:

    st.markdown(
"""
### Visualization

- Power BI
- Streamlit
- Matplotlib
"""
    )

with t4:

    st.markdown(
"""
### Development

- VS Code
- Git
- GitHub
"""
    )

st.divider()

st.header("Business Impact")

b1, b2, b3 = st.columns(3)

with b1:

    st.success(
"""
### Customer Retention

Identify customers at risk before they leave.
"""
    )

with b2:

    st.success(
"""
### Revenue Protection

Reduce customer churn and revenue loss.
"""
    )

with b3:

    st.success(
"""
### Data-Driven Decisions

Support business decisions with predictive analytics.
"""
    )

st.divider()

st.info(
"""
👈 **Use the sidebar to explore:**

- 🔮 Prediction
- 📊 Analytics Dashboard
- 📈 Model Performance
- 📑 Reports
- 👨‍💻 About
"""
)

st.divider()

st.caption(
    "Developed by Vaibhav Jain • ReadyNest Data Analytics Internship • Week 4"
)