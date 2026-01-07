# STS Carbon Benefits Calculator: Forest Carbon Benefits of Spongy Moth Management (STS)

**Author:** Ksenia Onufrieva (2025)

Interactive web-based research tool for exploring carbon sequestration, avoided emissions, and social cost of carbon benefits associated with spongy moth management under the Slow the Spread (STS) program.

The calculator supports evaluation of climate benefits resulting from prevention of spongy moth (*Lymantria dispar*)–induced tree mortality.

👉 **Live app:** https://sts-carbon-benefits.streamlit.app/

## Overview
This Streamlit app estimates the carbon and economic benefits of preventing spongy moth–induced forest mortality through the Slow the Spread (STS) Program.

It calculates:
- One-time avoided CO₂ emissions from prevented tree mortality
- Preserved annual carbon sequestration from living forest
- Social Cost of Carbon (SCC) benefits
- Equivalent number of passenger vehicles removed from the road

## How to Use
1. Enter the area protected (acres)
2. Set percent mortality prevented by STS
3. Adjust carbon stock and sequestration rate
4. Choose SCC values and vehicle CO₂ rates

View outputs for:
- avoided emissions
- annual sequestration
- SCC value
- vehicle equivalents

## Methods
- Area conversion: 1 acre = 0.40468564224 ha  
- CO₂ conversion: t C × 3.667 = t CO₂  

**Avoided mortality pulse:**  
CO₂ = area_ha × mortality × carbon_stock × 3.667  

**Preserved annual sink:**  
Annual_CO₂ = area_ha × mortality × sequestration_CO₂  

**Social Cost of Carbon:**  
SCC_value = CO₂ × SCC  

**Vehicle equivalent:**  
Cars = CO₂ / emissions_per_car  

## License
MIT License

