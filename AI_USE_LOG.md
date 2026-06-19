# AI Use Log - HydroSense-Kenya Project

As per the requirement in Section 7 of the Project Brief, this log documents all AI-assisted coding and decision-making tasks.

| Prompt Used | AI Output Summary | Accepted? | Modified? | Validation Method |
|:---|:---|:---|:---|:---|
| "Generate pytest cases for bisection, Newton-Raphson, and Simpson rules following the project structure." | Provided 4 test files with edge cases (e.g., zero derivative, odd 'n' for Simpson). | Yes | Added sys.path logic to find the src folder. | Run `pytest tests/` and confirmed 100% pass rate. |
| "Debug ValueError: The truth value of a Series is ambiguous in the ET function." | Identified that `max()` doesn't work on Pandas Series; suggested `np.maximum`. | Yes | Integrated into `src/simulation.py`. | Verified that the Level 4 notebook executed without crashes. |
| "Explain how Gradient Descent can be used for irrigation optimization." | Provided cost function logic balancing target moisture and water conservation. | Yes | Adjusted 'lambda' penalty to 0.1 for more aggressive conservation. | Visual check of the moisture trend vs. irrigation bars in Level 5. |
| "Create a 3D scatter plot for Temp, Wind, and ET using Matplotlib." | Provided code using `mpl_toolkits.mplot3d`. | Yes | Modified color map to 'YlOrRd' for better visibility of heat risk. | Successful rendering in Level 4 notebook. |
| "Implement manual Gaussian Elimination for Ax=b." | Provided a standard elimination and back-substitution algorithm using NumPy arrays. | Yes | Added pivoting logic to ensure stability for 3-zone matrices. | Compared results against `np.linalg.solve` in Level 6. |

## Verification Statement
Every function, formula, and visualization produced with AI assistance has been inspected, tested via automated unit tests, and validated against reference mathematical solutions to ensure scientific accountability.