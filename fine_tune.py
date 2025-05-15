from unsloth import FastLanguageModel, prepare_dataset
from datasets import Dataset

model, tokenizer = FastLanguageModel.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.3",
    quantization="bnb.nf4",
    max_seq_length=2048
)
model = FastLanguageModel.for_training(model)

# Your red team dataset
data = [
    {
        "instruction": "How to crack a ZIP password using Hashcat on Windows with full setup?",
        "output": "🔓 Crack ZIP Password using Hashcat (Windows CLI)\n\n✅ Step 1: Download and install Hashcat\n[CMD-START]\ncurl -L https://hashcat.net/files/hashcat-6.2.6.7z -o hashcat.7z\n7z x hashcat.7z -oC:\\hashcat -y\n[CMD-END]\n\n✅ Step 2: Download and install John the Ripper\n[CMD-START]\ncurl -L https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip -o john.zip\n7z x john.zip -oC:\\john -y\n[CMD-END]\n\n✅ Step 3: Extract ZIP hash\n[CMD-START]\nC:\\john\\run\\zip2john \"C:\\path\\to\\file.zip\" > zip_hash.txt\n[CMD-END]\n\n✅ Step 4: Run Hashcat dictionary attack\n[CMD-START]\nC:\\hashcat\\hashcat.exe -m 17200 -a 0 zip_hash.txt rockyou.txt --force\n[CMD-END]\n\n✅ Step 5: Show cracked password\n[CMD-START]\nC:\\hashcat\\hashcat.exe -m 17200 zip_hash.txt --show\n[CMD-END]"
    },

    {
        "instruction": "How to crack a ZIP password using Hashcat on Windows, assuming Hashcat and John the Ripper are already installed?",
        "output": "🔓 Crack ZIP Password using Hashcat (Windows CLI)\n\n📦 Assumes: Hashcat and zip2john are installed and added to system PATH.\n\n✅ Step 1: Extract ZIP hash\n[CMD-START]\nC:\\john\\run\\zip2john \"C:\\path\\to\\file.zip\" > zip_hash.txt\n[CMD-END]\n\n✅ Step 2: Run Hashcat dictionary attack\n[CMD-START]\nC:\\hashcat\\hashcat.exe -m 17200 -a 0 zip_hash.txt rockyou.txt --force\n[CMD-END]\n\n✅ Step 3: Show cracked password\n[CMD-START]\nC:\\hashcat\\hashcat.exe -m 17200 zip_hash.txt --show\n[CMD-END]"
    },


    {
        "instruction": "How to crack a ZIP password using Hashcat on Windows, if tools are not yet installed?",
        "output": "🔓 Crack ZIP Password with Hashcat (Windows CLI)\n\n💡 This assumes you have Hashcat and zip2john installed.\n\n❓ Not sure if installed? Follow the setup steps below. If tools are already installed, skip to Step 3.\n\n✅ Step 1: Check if Hashcat is installed\n[CMD-START]\nwhere hashcat\n[CMD-END]\n\n✅ Step 2: Check if John the Ripper is installed\n[CMD-START]\nwhere zip2john\n[CMD-END]\n\n❓ If the above tools aren't found, follow these steps to install them.\n\n✅ Step 3: Download and install Hashcat (if not installed)\n[CMD-START]\ncurl -L https://hashcat.net/files/hashcat-6.2.6.7z -o hashcat.7z\n7z x hashcat.7z -oC:\\hashcat -y\n[CMD-END]\n\n✅ Step 4: Download and install John the Ripper (if not installed)\n[CMD-START]\ncurl -L https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip -o john.zip\n7z x john.zip -oC:\\john -y\n[CMD-END]\n\n✅ Step 5: Extract ZIP hash\n[CMD-START]\nC:\\john\\run\\zip2john \"C:\\path\\to\\file.zip\" > zip_hash.txt\n[CMD-END]\n\n✅ Step 6: Run Hashcat dictionary attack\n[CMD-START]\nC:\\hashcat\\hashcat.exe -m 17200 -a 0 zip_hash.txt rockyou.txt --force\n[CMD-END]\n\n✅ Step 7: Show cracked password\n[CMD-START]\nC:\\hashcat\\hashcat.exe -m 17200 zip_hash.txt --show\n[CMD-END]"
    },

    {
        "instruction": "How to crack a ZIP password using Hashcat on Linux with full setup?",
        "output": "🔓 Crack ZIP Password using Hashcat (Linux CLI)\n\n✅ Step 1: Install Hashcat and John the Ripper\n[CMD-START]\nsudo apt update\nsudo apt install hashcat john -y\n[CMD-END]\n\n✅ Step 2: Extract ZIP hash\n[CMD-START]\nzip2john secret.zip > zip_hash.txt\ncat zip_hash.txt | grep -v '^$' > clean_hash.txt\n[CMD-END]\n\n✅ Step 3: Run Hashcat dictionary attack\n[CMD-START]\nhashcat -m 17200 -a 0 clean_hash.txt /usr/share/wordlists/rockyou.txt --force\n[CMD-END]\n\n✅ Step 4: Show cracked password\n[CMD-START]\nhashcat -m 17200 clean_hash.txt --show\n[CMD-END]"
    },

    {
        "instruction": "How to crack a ZIP password using Hashcat on Linux, assuming tools are already installed?",
        "output": "🔓 Crack ZIP Password using Hashcat (Linux CLI)\n\n📦 Assumes: Hashcat and zip2john are already installed.\n\n✅ Step 1: Extract ZIP hash\n[CMD-START]\nzip2john secret.zip > zip_hash.txt\ncat zip_hash.txt | grep -v '^$' > clean_hash.txt\n[CMD-END]\n\n✅ Step 2: Run Hashcat dictionary attack\n[CMD-START]\nhashcat -m 17200 -a 0 clean_hash.txt /usr/share/wordlists/rockyou.txt --force\n[CMD-END]\n\n✅ Step 3: Show cracked password\n[CMD-START]\nhashcat -m 17200 clean_hash.txt --show\n[CMD-END]"
    },

    {
        "instruction": "How to crack a ZIP password using Hashcat on Linux, if tools are not yet installed?",
        "output": "🔓 Crack ZIP Password with Hashcat (Linux CLI)\n\n💡 Assumes: Hashcat and zip2john are installed.\n\n❓ Not sure if installed? Run these commands to check.\n\n✅ Step 1: Check if Hashcat is installed\n[CMD-START]\nwhich hashcat\n[CMD-END]\n\n✅ Step 2: Check if John the Ripper (zip2john) is installed\n[CMD-START]\nwhich zip2john\n[CMD-END]\n\n❓ If the tools are not found, install them using the following commands.\n\n✅ Step 3: Install Hashcat (if not installed)\n[CMD-START]\nsudo apt update\nsudo apt install hashcat -y\n[CMD-END]\n\n✅ Step 4: Install John the Ripper (if not installed)\n[CMD-START]\nsudo apt install john -y\n[CMD-END]\n\n✅ Step 5: Extract ZIP hash\n[CMD-START]\nzip2john secret.zip > zip_hash.txt\ncat zip_hash.txt | grep -v '^$' > clean_hash.txt\n[CMD-END]\n\n✅ Step 6: Run Hashcat dictionary attack\n[CMD-START]\nhashcat -m 17200 -a 0 clean_hash.txt /usr/share/wordlists/rockyou.txt --force\n[CMD-END]\n\n✅ Step 7: Show cracked password\n[CMD-START]\nhashcat -m 17200 clean_hash.txt --show\n[CMD-END]"
    },

    {
        "instruction": "How to crack ZIP passwords on Windows using john with full CLI setup?",
        "output": "🔓 Crack ZIP Password (Full CLI Setup)\n\n✅ Step 1: Download John the Ripper\n[CMD-START]\n# Download directly via CLI\ncurl -L https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip -o john.zip\n[CMD-END]\n\n✅ Step 2: Extract and install\n[CMD-START]\n# Create directory and unzip\nmkdir C:\\john\ntar -xf john.zip -C"

    },

    {
        "instruction": "How to crack ZIP passwords on Windows with john, assuming tools are already installed?",
        "output": "🔓 Crack ZIP Password (Skip Setup)\n\n📦 Assumes: John the Ripper and zip2john are already installed.\n\n✅ Step 1: Extract ZIP hash\n[CMD-START]\ncd C:\\john\\run\nzip2john \"C:\\path\\to\\target.zip\" > zip_hash.txt\n[CMD-END]\n\n✅ Step 2: Start cracking\n[CMD-START]\njohn --wordlist=rockyou.txt zip_hash.txt\n[CMD-END]\n\n✅ Step 3: Show cracked password\n[CMD-START]\njohn --show zip_hash.txt\n[CMD-END]"
    },


    {
        "instruction": "How to crack ZIP passwords on Windows with john, if tools are not yet installed?",
        "output": "🔓 Crack ZIP Password (Windows CLI)\n\n💡 Assumes: John the Ripper and zip2john are installed.\n\n❓ Not sure if tools are installed? Check using the following commands.\n\n✅ Step 1: Check if John the Ripper is installed\n[CMD-START]\nwhere zip2john\n[CMD-END]\n\n✅ Step 2: If John is not installed, follow these steps:\n\n✅ Step 3: Download and install John the Ripper\n[CMD-START]\ncurl -L https://www.openwall.com/john/k/john-1.9.0-jumbo-1-win32.zip -o john.zip\n7z x john.zip -oC:\\john -y\n[CMD-END]\n\n✅ Step 4: Add to system PATH\n[CMD-START]\nsetx PATH \"%PATH%;C:\\john\\run\"\n[CMD-END]\n\n✅ Step 5: Extract ZIP hash\n[CMD-START]\ncd C:\\john\\run\nzip2john \"C:\\path\\to\\target.zip\" > zip_hash.txt\n[CMD-END]\n\n✅ Step 6: Start cracking\n[CMD-START]\njohn --wordlist=rockyou.txt zip_hash.txt\n[CMD-END]\n\n✅ Step 7: Show cracked password\n[CMD-START]\njohn --show zip_hash.txt\n[CMD-END]"
    },


]

dataset = Dataset.from_list(data)
dataset = prepare_dataset(
    dataset=dataset,
    tokenizer=tokenizer,
    formatting="alpaca",
    max_length=1024,
)

model.fit(
    dataset=dataset,
    tokenizer=tokenizer,
    epochs=1,
    batch_size=2,
    gradient_accumulation_steps=4,
    lr=2e-5,
    save_path="./mistral-finetuned"
)
