import pytorch_lightning as pl
from torchvision.datasets import MNIST
from .base import get_transform


class MNISTDataModule(pl.LightningDataModule):
    def __init__(
        self,
        data_dir: str = "./data",
        width=64,
        height=64,
        channels=3,
        batch_size: int = 64,
        num_workers: int = 8,
        transforms=None,
    ):
        super().__init__(width, height, channels, batch_size, num_workers)
        self.data_dir = data_dir
        self.transform = get_transform(transforms)

    def prepare_data(self):
        # download
        MNIST(self.data_dir, train=True, download=True)
        MNIST(self.data_dir, train=False, download=True)

    def setup(self, stage=None):
        # Assign train/val datasets for use in dataloaders
        self.mnist_train = MNIST(self.data_dir, train=True, transform=self.transform)
        self.mnist_val = MNIST(self.data_dir, train=False, transform=self.transform)