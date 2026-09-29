import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Binary Number System Converter",
    page_icon="🔢",
    layout="centered"
)

# -----------------------------
# Application Title
# -----------------------------
st.title("🔢 Binary Number System Converter")
st.write("Convert numbers between Binary, Octal, Decimal, and Hexadecimal.")

st.divider()

# -----------------------------
# Number System Selection
# -----------------------------
number_systems = {
    "Binary (Base 2)": 2,
    "Octal (Base 8)": 8,
    "Decimal (Base 10)": 10,
    "Hexadecimal (Base 16)": 16
}

col1, col2 = st.columns(2)

with col1:
    from_system = st.selectbox(
        "From Number System",
        list(number_systems.keys())
    )

with col2:
    to_system = st.selectbox(
        "To Number System",
        list(number_systems.keys()),
        index=1
    )

# -----------------------------
# User Input
# -----------------------------
number = st.text_input(
    "Enter the number",
    placeholder="Example: 1010"
)

# -----------------------------
# Conversion Function
# -----------------------------
def convert_number(number, from_base, to_base):
    decimal_number = int(number, from_base)

    if to_base == 2:
        return bin(decimal_number)[2:]

    elif to_base == 8:
        return oct(decimal_number)[2:]

    elif to_base == 10:
        return str(decimal_number)

    elif to_base == 16:
        return hex(decimal_number)[2:].upper()


# -----------------------------
# Convert Button
# -----------------------------
if st.button("Convert", type="primary", use_container_width=True):

    if number.strip() == "":
        st.warning("Please enter a number.")

    else:
        try:
            from_base = number_systems[from_system]
            to_base = number_systems[to_system]

            # Validate and convert
            decimal_number = int(number.strip(), from_base)
            result = convert_number(
                number.strip(),
                from_base,
                to_base
            )

            st.success("Conversion Successful!")

            st.subheader("Conversion Result")
            st.code(result, language="text")

            st.write(f"**Input:** {number} ({from_system})")
            st.write(f"**Output:** {result} ({to_system})")

        except ValueError:
            st.error(
                f"Invalid input! Please enter a valid "
                f"{from_system} number."
            )

# -----------------------------
# Information Section
# -----------------------------
st.divider()

st.subheader("About Number Systems")

st.markdown("""
- **Binary (Base 2):** Uses digits 0 and 1.
- **Octal (Base 8):** Uses digits 0 to 7.
- **Decimal (Base 10):** Uses digits 0 to 9.
- **Hexadecimal (Base 16):** Uses digits 0 to 9 and letters A to F.
""")

st.caption("Developed as an Experiential Learning Project.")