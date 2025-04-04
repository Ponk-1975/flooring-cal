import streamlit as st
from PIL import Image  # For adding images if needed

# Set page config for better appearance
st.set_page_config(
    page_title="Vinyl Tile Calculator",
    page_icon="🧮",
    layout="centered"
)

# Add some styling
st.markdown("""
<style>
    .header {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #2E86AB !important;
    }
    .result-box {
        background-color: #F8F9FA;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    .highlight {
        color: #E83F6F;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Main app
def main():
    # Header section
    st.markdown('<p class="header">🧮 Vinyl Tile Material Calculator</p>', unsafe_allow_html=True)
    st.write("Calculate the materials needed for vinyl tile installation")
    
    # Add a separator
    st.markdown("---")
    
    # Tile type selection with visual help
    st.subheader("1. Tile Specifications")
    tile_type = st.radio(
        "Select tile size:",
        ["600x600 mm", "610x610 mm", "900x900 mm"],
        help="Choose the size of tiles you'll be using"
    )
    
    # Tile data
    TILE_DATA = {
        "600x600 mm": {"size": 0.6*0.6, "pieces_per_sqm": 2.78},
        "610x610 mm": {"size": 0.61*0.61, "pieces_per_sqm": 2.69},
        "900x900 mm": {"size": 0.9*0.9, "pieces_per_sqm": 1.23}
    }
    
    # Area input with multiple unit options
    st.subheader("2. Area to Cover")
    unit = st.radio(
        "Input unit:",
        ["Square meters", "Square feet"],
        horizontal=True
    )
    
    if unit == "Square meters":
        area = st.number_input(
            "Enter area in square meters:",
            min_value=0.1,
            value=10.0,
            step=0.1,
            help="Enter the total area you need to cover"
        )
    else:
        sqft = st.number_input(
            "Enter area in square feet:",
            min_value=1.0,
            value=100.0,
            step=1.0
        )
        area = sqft * 0.092903  # Convert to square meters
    
    # Material rates
    st.subheader("3. Material Specifications (Optional)")
    with st.expander("Adjust material rates if needed"):
        copper_wire_rate = st.number_input(
            "Copper wire (meters per sqm):",
            min_value=0.1,
            value=0.63,
            step=0.01
        )
        adhesive_coverage = st.number_input(
            "Adhesive coverage (sqm per 15kg bucket):",
            min_value=1,
            value=70,
            step=1
        )
    
    # Calculate button
    if st.button("Calculate Materials", type="primary"):
        # Perform calculations
        tile_data = TILE_DATA[tile_type]
        tiles_needed = round(area * tile_data["pieces_per_sqm"], 2)
        copper_wire_needed = round(area * copper_wire_rate, 2)
        adhesive_needed = round(area / adhesive_coverage, 2)
        
        # Display results in a nice box
        with st.container():
            st.markdown('<div class="result-box">', unsafe_allow_html=True)
            st.subheader("📊 Calculation Results")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(
                    label=f"{tile_type} Tiles Needed",
                    value=f"{tiles_needed} pieces"
                )
                st.metric(
                    label="Copper Wire Needed",
                    value=f"{copper_wire_needed} meters"
                )
            
            with col2:
                st.metric(
                    label="Adhesive Needed",
                    value=f"{adhesive_needed} buckets"
                )
                st.metric(
                    label="Total Area",
                    value=f"{area:.2f} sqm"
                )
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Add some tips
            st.info("💡 Remember to add 10% extra for cutting waste and errors")

if __name__ == "__main__":
    main()