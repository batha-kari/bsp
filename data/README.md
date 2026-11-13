# Input data

The chat export contained code but no datasets. Place comma-separated numeric CSV files in this directory using the filenames expected by each script:

- `ecg_normal.csv` — ECG samples for `ecg/heart_rate_threshold.py`, `ecg/ecg_morphology.py`, and `ecg/ecg_artifact_filtering.py`.
- `hr.csv` — ECG/heart-rate samples for `ecg/hrv_metrics.py`.
- `ppg.csv` — PPG samples for the scripts in `ppg/`.
- `respiratory.csv` — respiratory samples for `respiratory/respiratory_rate.py`.

The ECG, PPG, and HRV scripts use comma delimiters. The respiratory example uses NumPy's default whitespace delimiter. Keep local datasets out of version control; `.gitignore` excludes CSV files in this directory.
