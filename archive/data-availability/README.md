Assessment of overall data availability
=======================================

With the archive built, we first want to make a quick assessment and visualisation of the data availability for the deployment. This is done using the ``miniseed-availability`` utility (https://github.com/hemmelig/miniseed-availability):

```bash
mseed-availability compute --config askja-mag.toml
mseed-availability visualise --config askja-mag.toml
ln -s ../../data/processed/availability/plots/magnetic/availability/askja-mag-availability-plot.png askja-mag-availability-plot.png
```

This will produce a summary plot and make a local symlink.
