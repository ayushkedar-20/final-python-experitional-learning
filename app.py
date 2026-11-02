
         import streamlit as st
import math
import statistics

st.set_page_config(page_title="Multi-Format Scientific Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Multi-Format Scientific & Engineering Calculator")
st.markdown("**Project Assessment:** Advanced Python Calculator supporting Arithmetic, Scientific, Engineering, Statistics, and Unit Conversions.")

# Sidebar navigation for features
section = st.sidebar.selectbox(
    "Select Calculator Module", 
    ["Arithmetic & Scientific", "Engineering Calculations", "Statistical Analysis", "Unit Conversions"]
)

# 1. Arithmetic & Scientific
if section == "Arithmetic & Scientific":
    st.header("➕ Basic Arithmetic & 🔬 Scientific Functions")
    
    calc_mode = st.radio("Choose Input Mode", ["Expression Evaluator", "Direct Scientific Functions"])
    
    if calc_mode == "Expression Evaluator":
        st.info("Example expressions: `15 * (3 + 5)`, `math.sin(math.radians(90))`, `math.sqrt(144)`")
        expr = st.text_input("Enter mathematical expression:", "25 * 4 + 10")
        if st.button("Calculate"):
            try:
                # Safe evaluation with math module enabled
                result = eval(expr, {"__builtins__": None}, {"math": math})
                st.success(f"**Result:** {result}")
            except Exception as e:
                st.error(f"Calculation Error: {e}")
                
    else:
        func = st.selectbox("Select Function", ["Square Root", "Power (x^y)", "Factorial", "Logarithm (ln / log10)", "Trigonometry"])
        
        if func == "Square Root":
            val = st.number_input("Enter value:", value=9.0)
            if st.button("Compute"):
                st.success(f"Result: {math.sqrt(val)}")
                
        elif func == "Power (x^y)":
            base = st.number_input("Base (x):", value=2.0)
            exp = st.number_input("Exponent (y):", value=3.0)
            if st.button("Compute"):
                st.success(f"Result: {math.pow(base, exp)}")
                
        elif func == "Factorial":
            val = st.number_input("Enter integer:", min_value=0, step=1, value=5)
            if st.button("Compute"):
                st.success(f"Result: {math.factorial(int(val))}")
                
        elif func == "Logarithm (ln / log10)":
            val = st.number_input("Enter value (>0):", value=10.0)
            log_type = st.radio("Type", ["Natural Log (ln)", "Log Base 10"])
            if st.button("Compute"):
                if val <= 0:
                    st.error("Value must be greater than zero.")
                else:
                    res = math.log(val) if "Natural" in log_type else math.log10(val)
                    st.success(f"Result: {res}")
                    
        elif func == "Trigonometry":
            trig_op = st.selectbox("Operation", ["sin", "cos", "tan"])
            angle = st.number_input("Enter angle value:", value=30.0)
            unit = st.radio("Angle Unit", ["Degrees", "Radians"])
            if st.button("Compute"):
                rad = math.radians(angle) if unit == "Degrees" else angle
                res = math.sin(rad) if trig_op == "sin" else (math.cos(rad) if trig_op == "cos" else math.tan(rad))
                st.success(f"{trig_op}({angle} {unit}) = {res}")

# 2. Engineering Calculations
elif section == "Engineering Calculations":
    st.header("⚙️ Engineering Calculations")
    eng_tool = st.selectbox("Select Tool", ["Ohm's Law Calculator (V = I * R)", "Quadratic Equation Solver (ax² + bx + c = 0)"])
    
    if eng_tool == "Ohm's Law Calculator (V = I * R)":
        sub_calc = st.selectbox("Find:", ["Voltage (V)", "Current (I)", "Resistance (R)"])
        if sub_calc == "Voltage (V)":
            i = st.number_input("Current (I in Amps):", value=2.0)
            r = st.number_input("Resistance (R in Ohms):", value=5.0)
            if st.button("Calculate Voltage"):
                st.success(f"Voltage = {i * R if 'R' in locals() else i * r} Volts")
        elif sub_calc == "Current (I)":
            v = st.number_input("Voltage (V in Volts):", value=10.0)
            r = st.number_input("Resistance (R in Ohms):", value=5.0)
            if st.button("Calculate Current"):
                st.success(f"Current = {v / r if r != 0 else 'Division by zero'} Amps")
        else:
            v = st.number_input("Voltage (V in Volts):", value=10.0)
            i = st.number_input("Current (I in Amps):", value=2.0)
            if st.button("Calculate Resistance"):
                st.success(f"Resistance = {v / i if i != 0 else 'Division by zero'} Ohms")
                
    else:
        st.markdown("Solve equations of form: $ax^2 + bx + c = 0$")
        a = st.number_input("Coefficient a:", value=1.0)
        b = st.number_input("Coefficient b:", value=-3.0)
        c = st.number_input("Coefficient c:", value=2.0)
        if st.button("Solve Roots"):
            disc = (b**2) - (4*a*c)
            if disc > 0:
                root1 = (-b + math.sqrt(disc)) / (2*a)
                root2 = (-b - math.sqrt(disc)) / (2*a)
                st.success(f"Two distinct real roots: **{root1}** and **{root2}**")
            elif disc == 0:
                root = -b / (2*a)
                st.success(f"One repeated real root: **{root}**")
            else:
                real_part = -b / (2*a)
                imag_part = math.sqrt(abs(disc)) / (2*a)
                st.success(f"Complex roots: **{real_part} ± {imag_part}i**")

# 3. Statistical Analysis
elif section == "Statistical Analysis":
    st.header("📊 Statistical Calculations")
    data_str = st.text_input("Enter comma-separated numbers:", "12, 15, 22, 28, 35, 42")
    
    if st.button("Analyze Data"):
        try:
            data = [float(x.strip()) for x in data_str.split(",")]
            if len(data) == 0:
                st.warning("Please enter valid numbers.")
            else:
                st.write(f"**Count (N):** {len(data)}")
                st.write(f"**Mean:** {statistics.mean(data):.4f}")
                st.write(f"**Median:** {statistics.median(data):.4f}")
                st.write(f"**Mode:** {statistics.mode(data) if len(set(data)) < len(data) else 'No unique mode'}")
                st.write(f"**Standard Deviation:** {statistics.stdev(data):.4f}" if len(data) > 1 else "**Standard Deviation:** Requires ≥ 2 items")
                st.write(f"**Variance:** {statistics.variance(data):.4f}" if len(data) > 1 else "**Variance:** Requires ≥ 2 items")
        except Exception as e:
            st.error(f"Error parsing data: {e}")

# 4. Unit Conversions
elif section == "Unit Conversions":
    st.header("🔄 Unit Conversions")
    cat = st.selectbox("Category", ["Length", "Temperature", "Weight"])
    
    val = st.number_input("Value to convert:", value=100.0)
    
    if cat == "Length":
        direction = st.selectbox("Conversion", ["Meters to Kilometers", "Kilometers to Meters", "Centimeters to Meters"])
        if st.button("Convert"):
            if "Meters to Kilo" in direction: st.success(f"{val} m = {val / 1000} km")
            elif "Kilometers to Meter" in direction: st.success(f"{val} km = {val * 1000} m")
            else: st.success(f"{val} cm = {val / 100} m")
            
    elif cat == "Temperature":
        direction = st.selectbox("Conversion", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
        if st.button("Convert"):
            if "Celsius to F" in direction: st.success(f"{val}°C = {(val * 9/5) + 32}°F")
            else: st.success(f"{val}°F = {(val - 32) * 5/9}°C")
            
    else:
        direction = st.selectbox("Conversion", ["Grams to Kilograms", "Kilograms to Grams"])
        if st.button("Convert"):
            if "Grams to Kilo" in direction: st.success(f"{val} g = {val / 1000} kg")
            else: st.success(f"{val} kg = {val * 1000} g")
