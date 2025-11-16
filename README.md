# WhatsApp Scheduler 📱⏰

A Python automation tool to schedule and send WhatsApp messages and media files on Windows using WhatsApp Desktop app.

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)](https://www.microsoft.com/windows)

## ✨ Features

- 📅 **Schedule Messages** - Send messages at specific date and time
- 📎 **Media Support** - Send images, videos, documents, audio, zip files
- 💬 **Captions** - Add captions to media files
- 🔄 **Batch Scheduling** - Schedule multiple messages at once
- ⚡ **Simple API** - Easy-to-use Python interface
- 🖥️ **Windows Native** - Works with WhatsApp Desktop app

## 📋 Requirements

- Windows 10/11
- Python 3.7 or higher
- WhatsApp Desktop app installed
- WhatsApp account logged in

## 🚀 Installation

1. **Clone the repository**

git clone https://github.com/Blackler-pvt/whatsapp-scheduler.git
cd whatsapp-scheduler


2. **Install dependencies**

pip install -r requirements.txt


3. **Install WhatsApp Desktop**
- Download from [Microsoft Store](https://www.microsoft.com/store/productId/9NKSQGP7F2NH)
- Or download from [WhatsApp website](https://www.whatsapp.com/download)
- Login to your WhatsApp account

## 📖 Usage

### Basic Text Message

from whatsapp_scheduler import WhatsAppScheduler

scheduler = WhatsAppScheduler()

scheduler.add_message(
phone="919876543210", # Country code without +
message="Hello! This is a scheduled message.",
date_time="2025-11-17 09:00" # Format: YYYY-MM-DD HH:MM
)

scheduler.run()


### Send Image with Caption

scheduler.add_message(
phone="919876543210",
message="Check out this photo!",
date_time="2025-11-17 10:30",
file_path=r"C:\Users\YourName\Pictures\photo.jpg"
)


### Send Document

scheduler.add_message(
phone="918765432109",
message="Here's the report",
date_time="2025-11-17 14:00",
file_path=r"C:\Users\YourName\Documents\report.pdf"
)


### Multiple Scheduled Messages

scheduler = WhatsAppScheduler()

Morning message
scheduler.add_message("919876543210", "Good morning!", "2025-11-17 09:00")

Lunch reminder
scheduler.add_message("919876543210", "Lunch time!", "2025-11-17 13:00")

Evening message
scheduler.add_message("919876543210", "Good evening!", "2025-11-17 18:00")

scheduler.run()


## 📁 Supported File Types

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
- **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`
- **Audio**: `.mp3`, `.wav`, `.ogg`, `.m4a`
- **Documents**: `.pdf`, `.docx`, `.xlsx`, `.txt`, `.pptx`
- **Archives**: `.zip`, `.rar`, `.7z`

## ⚙️ Configuration

### Phone Number Format

Use country code without the `+` sign:
- ✅ Correct: `919876543210` (India)
- ✅ Correct: `14155552671` (USA)
- ❌ Wrong: `+919876543210`

### Date-Time Format

Use `YYYY-MM-DD HH:MM` format (24-hour):
- ✅ Correct: `2025-11-17 14:30`
- ✅ Correct: `2025-12-25 09:00`
- ❌ Wrong: `17-11-2025 2:30 PM`

### File Paths

Use raw strings (prefix with `r`) for Windows paths:

Correct
file_path=r"C:\Users\Name\Documents\file.pdf"

Also correct
file_path="C:\Users\Name\Documents\file.pdf"


## 🛠️ Troubleshooting

### WhatsApp not opening
- Ensure WhatsApp Desktop is installed
- Check if you're logged in to WhatsApp
- Try manually opening WhatsApp once before running

### File not sending
- Verify file path is correct
- Check file exists at the specified location
- Ensure file size is under 100MB (WhatsApp limit)

### Messages not sending at scheduled time
- Keep the script running (don't close)
- Computer must be unlocked and active
- Check date-time format is correct

### Paths with spaces not working
- Install `pywin32`: `pip install pywin32`
- Use raw strings: `r"C:\My Documents\file.pdf"`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is for educational and personal use only. Please respect WhatsApp's Terms of Service and use responsibly. Automated messaging may violate WhatsApp's policies if used for spam or commercial purposes.

## 🙏 Acknowledgments

- Built with [PyAutoGUI](https://pyautogui.readthedocs.io/)
- Inspired by the need for simple WhatsApp automation

## 📧 Support

If you have any questions or issues:
- Open an [Issue](https://github.com/yourusername/whatsapp-scheduler/issues)
- Star ⭐ this repository if you find it helpful!

---

