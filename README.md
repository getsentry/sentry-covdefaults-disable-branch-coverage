sentry-covdefaults-disable-branch-coverage
==========================================

disables `run:branch` for coverage (enabled by default with covdefaults)

## installation

```bash
pip install sentry-covdefaults-disable-branch-coverage
```

## why?

branch coverage is extremely slow until [this issue] is solved

[covdefaults] always sets `run:branch = true`

this is a hack to disable `run:branch` (by ordering this plugin after `covdefaults`)

[covdefaults]: https://github.com/asottile/covdefaults
[this issue]: https://github.com/nedbat/coveragepy/issues/1746

## usage

to enable the plugin, add it after `covdefaults` in your coverage plugins

in `.coveragerc`:

```ini
[run]
plugins =
    covdefaults
    sentry_covdefaults_disable_branch_coverage
```

in `setup.cfg` / `tox.ini`:

```ini
[coverage:run]
plugins =
    covdefaults
    sentry_covdefaults_disable_branch_coverage
```
