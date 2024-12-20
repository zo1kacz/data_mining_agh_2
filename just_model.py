
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

#tworzymy sieć
class FullyConnectedMNIST(nn.Module):
    def __init__(self, input_size=784, num_classes=10):
        super(FullyConnectedMNIST, self).__init__()

        # warstwy
        self.network = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        # spłaszczenie obrazu
        x = x.view(x.size(0), -1)
        return self.network(x)

# przygotowanie danych
def prepare_data():
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)) #wartości dla zbioru MNIST
    ])

    #pobieranie MNIST
    train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

    return train_loader, test_loader

# trening
def train(model, train_loader, criterion, optimizer, device):
    model.train()
    total_loss = 0

    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)

        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(train_loader)

# test
def test(model, test_loader, device):
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad(): #wyłączamy obliczanie gradientów by zszybsze obliczenie
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            predicted = torch.max(output.data, 1)[1]

            total += target.size(0)
            comparison = (predicted == target)
            correct += comparison.sum().item()

    accuracy = 100 * correct / total
    return accuracy

#main
def main():
    #dostępność GPU z CUDA
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Używane urządzenie: {device}")


    train_loader, test_loader = prepare_data()
    model = FullyConnectedMNIST().to(device)

    #wybory paramentrów i funkcji
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    epochs = 3


    for epoch in range(1, epochs + 1):
        train_loss = train(model, train_loader, criterion, optimizer, device)
        test_accuracy = test(model, test_loader, device)

        print(f"Epoka {epoch}: Strata treningowa = {train_loss:.4f}, Dokładność testowa = {test_accuracy:.2f}%")

if __name__ == "__main__":
    main()
