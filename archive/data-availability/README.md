Assessment of overall data availability
=======================================

With the archive built, we first want to make a quick assessment and visualisation of the data availability for the deployment. This is done using the ``miniseed-availability`` utility (https://github.com/hemmelig/miniseed-availability). 

```bash
# Setup virtual environment
uv sync

# Run the computation and visualisation
uv run mseed-availability compute --config askja-mag.toml
uv run mseed-availability visualise --config askja-mag.toml

# Create a local symlink of the availability plot
ln -s ../../data/processed/availability/plots/magnetic/availability/askja-mag-availability-plot.png askja-mag-availability-plot.png
```
