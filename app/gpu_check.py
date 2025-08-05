import torch

def check_gpu():
    if torch.cuda.is_available():
        print("✅ CUDA-enabled GPU detected.")
        print("Device:", torch.cuda.get_device_name(0))
    else:
        print("⚠️ No GPU detected. Using CPU.")
