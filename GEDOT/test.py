import torch
a = torch.randn(4, 2)
d=a
b = torch.randn(4,3)
d = torch.cat([d,b],dim=1)
print(d.shape)
c = torch.randn(4,4)
d = torch.cat([d,c], dim=1)
print(d.shape)