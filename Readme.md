# STS Carbon Benefits Calculator

This Streamlit app estimates the **carbon and economic benefits** of preventing
spongy moth (*Lymantria dispar*)–induced tree mortality through the Slow the Spread (STS) Program.

It calculates:
- One-time avoided CO₂ emissions (from prevented tree mortality)
- Preserved annual carbon sequestration (from living forest)
- Social Cost of Carbon (SCC) benefits
- Equivalent number of passenger vehicles removed from the road

---

## How to Use

1. Enter the area protected (acres).
2. Set % mortality prevented by STS.
3. Adjust carbon stock and sequestration rate.
4. Choose SCC values and vehicle CO₂ rates.
5. View:
   - avoided emissions  
   - annual sequestration  
   - SCC value  
   - car-equivalents  

---

## Methods

- **Area conversion:** 1 acre = 0.40468564224 ha  
- **CO₂ conversion:** t C × 3.667 = t CO₂  
- **Avoided mortality pulse:**  
  `CO₂ = area_ha × mortality × carbon_stock × 3.667`  
- **Preserved annual sink:**  
  `Annual_CO₂ = area_ha × mortality × sequestration_CO₂`  
- **SCC:**  
  `SCC_value = CO₂ × SCC`  
- **Cars equivalent:**  
  `Cars = CO₂ / emissions_per_car`

---

## Author
Developed by K. Onufrieva (2025).

---

## License
MIT License.
