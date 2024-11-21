from __future__ import annotations

from coverage import CoveragePlugin
from coverage.plugin_support import Plugins
from coverage.types import TConfigurable


class DisableBranchCoverage(CoveragePlugin):
    def configure(self, config: TConfigurable) -> None:
        config.set_option('run:branch', False)


def coverage_init(reg: Plugins, options: dict[str, str]) -> None:
    reg.add_configurer(DisableBranchCoverage())
