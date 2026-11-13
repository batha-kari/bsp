# Biomedical Signal Processing Exercises

A collection of Python signal-processing examples transcribed from a WhatsApp chat and organized by topic. The scripts retain the shared algorithms; machine-specific Windows file paths were replaced with repository-relative paths under `data/`.

## Requirements

- Python 3.10+
- NumPy
- Matplotlib
- SciPy (used by ECG, PPG, and respiratory examples)

Install dependencies from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

Run a script from the repository root, for example:

```bash
python fundamentals/discrete_convolution.py
python ecg/heart_rate_threshold.py
```

The biomedical scripts load CSV files from `data/`. See [data/README.md](data/README.md) for expected filenames. The chat export did not include the CSV datasets, so add your own files before running those examples.

## Scripts

### ECG

- `ecg/heart_rate_threshold.py` — threshold-based R-peak detection and heart-rate estimate.
- `ecg/ecg_morphology.py` — R, Q, S, P, and T peak and interval calculations.
- `ecg/hrv_metrics.py` — RR intervals and basic HRV metrics.
- `ecg/ecg_artifact_filtering.py` — synthetic artifact addition and filtering demonstrations.

### PPG

- `ppg/pulse_metrics.py` — pulse peak, interval, rate, and area calculations.
- `ppg/dicrotic_notch.py` — derivative-based dicrotic-notch detection.

### Respiratory

- `respiratory/respiratory_rate.py` — time-domain and FFT respiratory-rate estimates.

### Fundamentals

- `fundamentals/elementary_signals.py` — unit step, impulse, and ramp sequences.
- `fundamentals/exponential_sequences.py` — exponential sequences for four bases.
- `fundamentals/sinusoidal_signals.py` — sine waves and their sum.
- `fundamentals/discrete_convolution.py` — discrete convolution by NumPy and a direct sum.

These are educational examples transcribed from chat. Their signal-processing assumptions and numerical results have not been independently validated.
