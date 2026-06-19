# HydroSense-Kenya: Scientific Computing System

**Project Title:** HydroSense-Kenya: A Scientific Computing System for Smart Irrigation, Water Balance Simulation, and Climate-Aware Decision Support  
**Course Code:** ICS 2207: Scientific Computing  
**Academic Period:** February - May 2026 Semester  
**Core Domain:** Smart Agriculture, Hydrological Modeling, Numerical Optimization  

---

## 1. Project Overview
HydroSense-Kenya is a comprehensive scientific computing suite designed to address water-use efficiency for smallholder farms in Kenya. This project follows the intellectual arc of scientific computing: problem framing, data acquisition, mathematical modeling, numerical computation, simulation, optimization, validation, and scientific communication. 

The system transitions through an incremental six-level design, moving beyond basic programming by implementing manual numerical engines (Root Finding, ODE Solvers, Linear Algebra) to provide a robust decision-support platform for modern agriculture.

## 2. Core Scientific Logic
The system is built upon the following mathematical foundations:
- **Water Balance Equation:** $S_{t+1} = S_t + R_t + I_t - ET_t - D_t$
- **Evapotranspiration (ET) Model:** An empirical non-linear relationship between temperature, wind speed, solar index, and humidity.
- **Predictive Modeling:** 4th-order Runge-Kutta (RK4) integration for stable soil-moisture evolution.
- **Decision Intelligence:** Gradient Descent optimization to minimize water usage costs while respecting moisture constraints.

## 3. Project Structure
In accordance with Section 6 of the Project Brief, the repository is organized as follows:

```text
HydroSense-Kenya/
├── data/
│   ├── raw/                           # Original datasets (Realistic/Messy)
│   │   ├── weather_daily.csv          # Rain, temp, solar, wind data
│   │   ├── soil_sensor_data.csv       # Moisture and tank levels for Zones A, B, C
│   │   └── crop_zone_parameters.csv   # Thresholds, area, and drainage coeffs
│   └── processed/                     # Cleaned, aggregated daily datasets
│       └── cleaned_irrigation_dataset.csv
├── notebooks/                         # Six-level incremental project structure
│   ├── Level_1_Problem_Framing.ipynb  # Context and Python foundation
│   ├── Level_2_Vectorization_and_Error.ipynb # Performance and FP reliability
│   ├── Level_3_Numerical_Methods.ipynb      # Manual implementation of core engines
│   ├── Level_4_Data_Analysis_and_Visualization.ipynb # Cleaning and interpretation
│   ├── Level_5_Simulation_and_Optimization.ipynb    # RK4, Monte Carlo, and GD
│   └── Level_6_Final_Integration.ipynb      # Audit defense and validation
├── src/                               # Reusable Python source modules
│   ├── data_cleaning.py               # Aggregation and anomaly handling
│   ├── numerical_methods.py           # Manual root-finding, integration, Ax=b
│   ├── simulation.py                  # Physics logic and ODE solvers
│   ├── optimization.py                # Gradient Descent and cost functions
│   └── visualization.py               # Scientific and 3D plotting
├── tests/                             # Automated validation suite (pytest)
│   ├── test_root_finding.py           # Testing Bisection, Newton, Differentiation
│   ├── test_integration.py            # Testing Trapezoidal and Simpson rules
│   ├── test_linear_systems.py         # Testing Gaussian Elimination
│   └── test_simulation.py             # Testing RK4 and Water Balance physics
├── reports/                           # Final deliverables
│   ├── final_scientific_report.pdf    # Detailed technical documentation
│   └── presentation_slides.pdf        # Live audit defense materials
├── AI_USE_LOG.md                      # Transparent record of AI assistance
├── requirements.txt                   # Dependency list for reproducibility
└── README.md                          # Project documentation (this file)
```

## 4. Prerequisites
The project is built using the Python scientific stack. Ensure the following are installed on your system:
- **Python 3.8+**
- **NumPy:** For vectorized array operations and linear algebra.
- **Pandas:** For data wrangling and time-series aggregation.
- **Matplotlib:** For scientific visualizations and 3D plotting.
- **pytest:** For executing the automated validation suite.
- **python-pptx:** Required if generating the automated slide deck.
- **SciPy:** (Optional) Used in Level 6 for verification of manual results only.

## 5. Installation & Setup
Follow these steps to set up the reproducible environment:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/[your-username]/HydroSense-Kenya.git
   cd HydroSense-Kenya
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .\.venv\Scripts\activate
   ```
3. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## 6. Usage
### Executing the Workflow
The project is designed to be followed incrementally. Open the Jupyter notebooks in the `notebooks/` directory sequentially to observe the scientific progression.
```bash
jupyter notebook
```

### Running the Validation Suite (Code Audit Defense)
To verify the numerical correctness of the manual algorithms (a critical requirement for the Level 6 code audit):
```bash
pytest tests/
```

## 7. Contributing
This system is an open-source capstone project. Contributions that enhance the accuracy of the moisture-decay ODEs or introduce more complex optimization constraints (e.g., energy tariffs) are welcome.
1. Fork the project.
2. Create your feature branch (`git checkout -b feature/NewOptimization`).
3. Ensure all tests pass (`pytest tests/`).
4. Submit a Pull Request with a clear description of the mathematical changes.

## 8. Contact & Acknowledgments
- **Author:** CALEB MUTAI
- **Email:** caleb.mutai@students.jkuat.ac.ke
- **Institutional Alignment:** Developed for ICS 2207 - Scientific Computing.
- **Data Source:** Synthetic datasets provided by the ICS 2207 Project Pack.

---
**Disclaimer:** This project incorporates AI-assisted coding tools for testing and visualization. Full documentation of prompts and verification methods is available in the `AI_USE_LOG.md` file.
