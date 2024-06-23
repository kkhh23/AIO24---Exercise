import torch
import torch.nn as nn

# Sigmoid


class MySigmoid(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return 1 / (1 + torch.exp(-x))

# Relu


class MyReluActivation(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        zeros = torch.zeros_like(x)
        return torch.maximum(x, zeros)
