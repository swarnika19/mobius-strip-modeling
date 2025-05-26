# Möbius Strip 3D Modeling and Geometry Analysis

This project models a Möbius Strip using parametric equations in 3D and numerically estimates key geometric properties including surface area and boundary length.

## 🔧 Technologies Used

- **Python 3**
- **NumPy** for numerical computation
- **Matplotlib** for 3D surface visualization

## 📐 Parametric Equation Used

The Möbius strip is modeled using the following equations:

x(u,v) = (R + v * cos(u/2)) * cos(u)
y(u,v) = (R + v * cos(u/2)) * sin(u)
z(u,v) = v * sin(u/2)


- `u ∈ [0, 2π]` (angle around the center)
- `v ∈ [-w/2, w/2]` (offset from the strip center)
- `R`: Radius of the loop  
- `w`: Width of the strip

## 📊 Features

- Generates a 3D mesh of the Möbius surface
- Numerically estimates surface area using cross product of partial derivatives
- Computes total boundary length
- Visualizes the Möbius strip in 3D with aesthetic styling

## 📁 File Details

- `mobius_strip.py` – Main script for computing and visualizing the Möbius strip

## 📸 Sample Output

- Prints the estimated surface area and edge length
- Displays a colored 3D plot of the Möbius strip

## 🧠 Learning Outcome

This internship task demonstrates:
- 3D parametric modeling using Python
- Surface analysis using vector calculus
- Mesh-based numerical integration
- Clear coding practices and mathematical implementation

## 🔗 Author

**Swarnika**  
Third-year B.Tech Student  
Data Science Internship Project  
