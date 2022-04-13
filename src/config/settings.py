from dynaconf import Dynaconf

settings_with_prefix = Dynaconf(
    settings_files=["settings.toml"],
    environments=True,
)
# with settings_with_prefix.using_env("default"):
#     assert settings_with_prefix.CUSTOM == "this is custom when we set a prefix"
# assert (
#     settings_with_prefix.from_env("production").CUSTOM
#     == "this is custom when we set a prefix"
# )
