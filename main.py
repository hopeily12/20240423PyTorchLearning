import torch
print(torch.__version__)


#scalar----------->vector----------->matrix----------->tensor
scalar = torch.tensor([[[[7]]]])
print(scalar)
print(scalar.ndim)
print(scalar.shape)

vector = torch.tensor([7,7])
print(vector)
print(vector.ndim)
print(vector.shape)

matrix = torch.tensor([[1,2],[3,4]])
print(matrix)
print(matrix.ndim)
print(matrix.shape)

tensor = torch.tensor([[[1,2,3],[4,5,6],[7,8,9]]])
print(tensor)
print(tensor.ndim)
print(tensor.shape)

# Create a random tensor of size (3, 4)
random_tensor = torch.rand(size=(3,4))
print(random_tensor)
print(random_tensor.ndim)
print(random_tensor.shape)

# Create a random tensor of size (224, 224, 3)
random_image_size_tensor = torch.rand(size=(224, 224, 3))
print(random_image_size_tensor)
print(random_image_size_tensor.ndim)
print(random_image_size_tensor.dtype)
