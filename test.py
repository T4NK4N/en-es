import torch
import numpy as np
import torch.nn.functional as F
if __name__ == '__main__':
    input = torch.tensor(range(10), dtype=torch.float)
    input_ = F.softmax(input, dim=0)
    print(input_)