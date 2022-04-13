from pathlib import Path

from dynaconf import Dynaconf

config_root = Path(__file__).parent.resolve()
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[config_root / "settings.toml", config_root / ".secrets.toml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
