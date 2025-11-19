import streamlit as st

st.title("Forest Carbon Benefits of Spongy Moth Management (STS)")

st.markdown(
    """
This simple calculator estimates the **carbon and economic benefits** of preventing
spongy moth–induced tree mortality on forested land.
"""
)

st.header("Inputs")

col1, col2 = st.columns(2)

with col1:
    area_acres = st.number_input(
        "Area protected (acres)",
        min_value=1.0,
        value=100000.0,
        step=1000.0,
        format="%.0f"
    )
    mortality_percent = st.slider(
        "Defoliation-induced mortality avoided (%)",
        min_value=1,
        max_value=90,
        value=10,
        step=1
    )
    carbon_stock = st.number_input(
        "Aboveground carbon stock (t C / ha)",
        min_value=10.0,
        max_value=300.0,
        value=50.0,
        step=5.0
    )

with col2:
    sequestration_rate = st.number_input(
        "Annual net sequestration (t C / ha / yr)",
        min_value=0.1,
        max_value=3.0,
        value=0.5,
        step=0.1
    )
    scc_low = st.number_input(
        "Social Cost of Carbon – low ($ / t CO₂)",
        min_value=0.0,
        max_value=500.0,
        value=51.0,
        step=1.0
    )
    scc_high = st.number_input(
        "Social Cost of Carbon – high ($ / t CO₂)",
        min_value=0.0,
        max_value=500.0,
        value=190.0,
        step=1.0
    )
    car_emissions = st.number_input(
        "Average car emissions (t CO₂ / car / yr)",
        min_value=1.0,
        max_value=10.0,
        value=4.6,
        step=0.1
    )

st.divider()

# --- Core calculations ---

# Conversions
ACRE_TO_HA = 0.40468564224
C_TO_CO2 = 3.667

area_ha = area_acres * ACRE_TO_HA
mortality_frac = mortality_percent / 100.0

# One-time carbon pulse avoided (from mortality)
# C lost = area_ha * mortality_frac * carbon_stock (t C)
carbon_lost_tC = area_ha * mortality_frac * carbon_stock
co2_avoided_t = carbon_lost_tC * C_TO_CO2

# Annual sequestration preserved (because those trees stay alive)
# Annual C uptake = area_ha * mortality_frac * sequestration_rate
annual_c_uptake_tC = area_ha * mortality_frac * sequestration_rate
annual_co2_preserved_t = annual_c_uptake_tC * C_TO_CO2

# Cars equivalent
cars_one_time = co2_avoided_t / car_emissions if car_emissions > 0 else 0.0
cars_annual = annual_co2_preserved_t / car_emissions if car_emissions > 0 else 0.0

# Dollar values
one_time_value_low = co2_avoided_t * scc_low
one_time_value_high = co2_avoided_t * scc_high

annual_value_low = annual_co2_preserved_t * scc_low
annual_value_high = annual_co2_preserved_t * scc_high

st.header("Results")

colA, colB = st.columns(2)

with colA:
    st.subheader("One-time avoided carbon pulse (mortality)")

    st.metric(
        "CO₂ avoided (one-time)",
        f"{co2_avoided_t/1e6:.3f} Mt CO₂",
        help=f"{co2_avoided_t:,.0f} t CO₂"
    )

    st.metric(
        "Cars equivalent (one-time)",
        f"{cars_one_time:,.0f} cars · year⁻¹"
    )

    
low_val = f"{annual_value_low:,.0f}"
high_val = f"{annual_value_high:,.0f}"

st.markdown(
    f"""
    <p style='font-size:16px;'>
        <strong>Annual SCC value:</strong>
        <span style='white-space: nowrap;'>${low_val}</span>
        –
        <span style='white-space: nowrap;'>${high_val}</span>
        per year
    </p>
    """,
    unsafe_allow_html=True

    )


with colB:
    st.subheader("Preserved annual sink (ongoing)")

    st.metric(
        "Annual CO₂ preserved",
        f"{annual_co2_preserved_t/1e3:.1f} kt CO₂ / yr",
        help=f"{annual_co2_preserved_t:,.0f} t CO₂ / yr"
    )

    st.metric(
        "Cars equivalent (annual)",
        f"{cars_annual:,.0f} cars · year⁻¹"
    )

    low_val = f"{annual_value_low:,.0f}"
high_val = f"{annual_value_high:,.0f}"

st.markdown(
    f"""
    <p style='font-size:16px;'>
        <strong>Annual SCC value:</strong>
        <span style='white-space: nowrap;'>${low_val}</span>
        –
        <span style='white-space: nowrap;'>${high_val}</span>
        per year
    </p>
    """,
    unsafe_allow_html=True

    )

st.divider()

st.caption(
    "Note: This is a simple illustrative tool. Users should adjust carbon stock, "
    "sequestration rates, and mortality percentages based on local forest data "
    "and published literature."
)
