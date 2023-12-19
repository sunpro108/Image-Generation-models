import pytest

from hydra import compose, initialize
from omegaconf import DictConfig

@pytest.fixture(scope='package')
def cfg_global() -> DictConfig:
    with initialize(config_path="../configs", version_base='1.3'):
        cfg = compose(config_name='config.yaml', return_hydra_config=False)
    return cfg

def test_config_global(cfg_global):
    """
    Test that the config is loaded correctly
    """
    assert cfg_global
    assert cfg_global.callbacks
    assert cfg_global.trainer
    assert cfg_global.logger
    assert cfg_global.model
    assert cfg_global.datamodule
    assert cfg_global.networks