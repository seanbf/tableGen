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
            "time_s": np.linspace(0, 1, len(current_d)),
            "torque_e_nm": np.random.rand(len(current_d)),
            "torque_measured_nm": np.random.rand(len(current_d)),
            "id_apk": current_d + noise,
            "iq_apk": current_q + noise,
            "psi_d_wb": flux_d,
            "psi_q_wb": flux_q,
            "ld_h": flux_d / (current_d + noise + 1e-9),  # Dummy Ld
            "lq_h": flux_q / (current_q + noise + 1e-9),  # Dummy Lq
            "ud_v": np.zeros(len(current_d)),
            "uq_v": np.zeros(len(current_d)),
        }
    )

    config = {
        "motor": {
            "defaults": {
                "ke_v_krpm": 40.0
            }
        },
        "data": {
            "standard_names": {
                "input": {
                    "time": "time_s",
                    "id_apk": "id_apk",
                    "iq_apk": "iq_apk",
                    "torque_measured": "torque_measured_nm",
                },
                "computed": {
                    "torque_e_nm": "torque_e_nm",
                    "psi_d_wb": "psi_d_wb",
                    "psi_q_wb": "psi_q_wb",
                    "ld_h": "ld_h",
                    "lq_h": "lq_h",
                },
            }
        }
    }

    print("Testing plot_results...")
    try:
        plot_results(data, config)
        print("plot_results executed successfully.")
    except Exception as e:
        print(f"Error in plot_results: {e}")


if __name__ == "__main__":
    main()
