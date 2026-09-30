# Target configuration

Copy `target.example.json` to a local target file and edit the external read-only paths. `target.json` is a machine-local example for the current host.

The setup project owns all plans, run directories, screenshots, reports, findings, and skills. The configured `project`, `source_config`, and `runtime_config` paths are read-only inputs and are not copied into this repository.

Use `python3 scripts/preflight.py --config config/target.json --level-id <level-id>` before creating a run.
