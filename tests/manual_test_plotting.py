import os
import sys

import numpy as np
import pandas as pd

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ui import plot_results


def main():
    """Run reproduction script."""
    print("Generating synthetic data for Surface Plot...")
    # Create valid grid-like data for interpolation
    # Generate a grid of Id, Iq values
    id_range = np.linspace(-100, 100, 20)
    iq_range = np.linspace(-100, 100, 20)
    xx, yy = np.meshgrid(id_range, iq_range)

    # Flatten to simulate scattered input data (as the real data would be)
    current_d = xx.flatten()
    current_q = yy.flatten()

    # Calculate dummy Flux values based on some function (e.g. linear + saturation)
    # FluxD = Ld * Id + PM (simplified)
    # FluxQ = Lq * Iq
    flux_d = 0.001 * current_d + 0.1
    flux_q = 0.002 * current_q

    # Add some noise to simulate measurement noise
    noise = np.random.normal(0, 0.005, len(current_d))

    data = pd.DataFrame(
        {
            "timeS": np.linspace(0, 1, len(current_d)),
            "torqueElectromagneticNm": np.random.rand(len(current_d)),  # Dummy
            "torqueMeasuredNm": np.random.rand(len(current_d)),  # Dummy
            "currentDAxisApeak": current_d + noise,
            "currentQAxisApeak": current_q + noise,
            "fluxLinkageDAxisWb": flux_d,
            "fluxLinkageQAxisWb": flux_q,
        }
    )

    print("Testing plot_results (2D)...")
    try:
        plot_results(data)
        print("plot_results executed successfully (check browser/output).")
    except Exception as e:
        print(f"Error in plot_results: {e}")




if __name__ == "__main__":
    main()
