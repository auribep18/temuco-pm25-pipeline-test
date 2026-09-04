import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Temuco PM2.5 Explorer",
    page_icon="🏠",
    layout="centered",
)

# ------------------------------------------------------------
# Data: estimates from the simplified Jupyter notebook
# ------------------------------------------------------------
results = pd.DataFrame(
    {
        "Scenario": [
            "Pellet only",
            "Insulation only",
            "Pellet + Insulation",
        ],
        "Percent change": [
            -2.3295,
            -2.7199,
            -11.8922,
        ],
        "CI low": [
            -7.9776,
            -9.1957,
            -17.3489,
        ],
        "CI high": [
            3.6652,
            4.2177,
            -6.0753,
        ],
    }
)

# ------------------------------------------------------------
# Header
# ------------------------------------------------------------
st.title("Temuco PM₂.₅ Explorer")

st.markdown(
    """
This small interactive prototype presents the estimated change in indoor PM₂.₅
for residential heating and insulation interventions in Temuco, Chile.

**Reference scenario:** Firewood – No Insulation
"""
)

# ------------------------------------------------------------
# User interaction
# ------------------------------------------------------------
scenario = st.selectbox(
    "Select a scenario",
    results["Scenario"].tolist(),
)

selected = results.loc[results["Scenario"] == scenario].iloc[0]

# ------------------------------------------------------------
# Main result
# ------------------------------------------------------------
st.subheader("Estimated effect")

st.metric(
    label="Change in indoor PM₂.₅",
    value=f"{selected['Percent change']:.1f}%",
)

st.write(
    f"95% confidence interval: "
    f"{selected['CI low']:.1f}% to {selected['CI high']:.1f}%"
)

# ------------------------------------------------------------
# Plot
# ------------------------------------------------------------
st.subheader("Comparison across scenarios")

plot_data = results.copy()

x = plot_data["Percent change"].to_numpy()
xerr = [
    x - plot_data["CI low"].to_numpy(),
    plot_data["CI high"].to_numpy() - x,
]

fig, ax = plt.subplots(figsize=(7, 4.2))

y = range(len(plot_data))

ax.errorbar(
    x,
    y,
    xerr=xerr,
    fmt="o",
    capsize=4,
    linewidth=1.5,
)

ax.axvline(0, linewidth=1)
ax.set_yticks(list(y))
ax.set_yticklabels(plot_data["Scenario"])
ax.invert_yaxis()

ax.set_xlabel("Estimated change in indoor PM₂.₅ (%)")
ax.set_title("Treatment-group effects relative to Firewood – No Insulation")
ax.grid(axis="x", alpha=0.25)

plt.tight_layout()
st.pyplot(fig)

# ------------------------------------------------------------
# Short interpretation
# ------------------------------------------------------------
st.subheader("Interpretation")

if scenario == "Pellet + Insulation":
    st.write(
        "This scenario shows the largest estimated reduction in indoor PM₂.₅ "
        "among the three interventions in this prototype."
    )
else:
    st.write(
        "The estimated effect is relatively small and its 95% confidence interval "
        "crosses zero in this prototype."
    )

# ------------------------------------------------------------
# About
# ------------------------------------------------------------
with st.expander("About this prototype"):
    st.markdown(
        """
This app is a pipeline test built from a simplified Jupyter notebook.

The workflow is:

**Jupyter → GitHub → Streamlit → Zenodo**

For this prototype, the app uses the treatment-effect estimates already
calculated in the notebook rather than re-estimating the statistical model online.
"""
    )
