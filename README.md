# Jython File Organizer

A powerful GUI file organization tool built with Jython, combining the elegance of Python with the robustness of Java Swing.

## 📁 About

This application demonstrates the unique capabilities of Jython by creating a file organizer that automatically sorts files into directories based on their extensions. It showcases how Jython seamlessly bridges Python's intuitive syntax with Java's mature GUI framework.

**Developer:** [hexlorddev](https://github.com/hexlorddev)

## ✨ Features

- **Smart File Analysis** - Scans directories and categorizes files by extension
- **Automatic Organization** - Creates organized subdirectories and moves files accordingly
- **Intuitive GUI** - Clean, user-friendly interface built with Java Swing
- **Real-time Feedback** - Shows file counts, organization progress, and results
- **Safe Operations** - Confirmation dialogs prevent accidental file moves
- **Cross-platform** - Runs on any system with Jython installed

## 🔧 Requirements

- **Jython 2.7+** or **Jython 3.x**
- Java Runtime Environment (JRE) 8 or higher
- Operating System: Windows, macOS, or Linux

## 🚀 Installation & Usage

### Install Jython
```bash
# Download from https://www.jython.org/download
# Or via package manager:
pip install jython-installer
```

### Run the Application
```bash
jython index.py
```

### Using the Application
1. **Browse** - Click "Browse" to select a directory to organize
2. **Analyze** - Click "Analyze Directory" to see file type distribution
3. **Organize** - Click "Organize Files" to automatically sort files into folders

## 📂 How It Works

The application creates organized subdirectories based on file extensions:

```
📁 Your Directory/
├── 📁 JPG_Files/
│   ├── photo1.jpg
│   └── photo2.jpg
├── 📁 PDF_Files/
│   ├── document1.pdf
│   └── report.pdf
├── 📁 TXT_Files/
│   └── notes.txt
└── 📁 No_Extension/
    └── README
```

## 🎨 Jython Features Demonstrated

This project showcases several key Jython capabilities:

- **Java Integration** - Direct use of Java Swing components
- **Interface Implementation** - Implements Java's `ActionListener` interface
- **Python Logic** - Leverages Python's file handling and collections
- **Seamless Interop** - No complex bindings or wrappers needed
- **Best of Both Worlds** - Java's mature ecosystem with Python's readability

## 💻 Code Structure

```python
# Core Components
FileOrganizerGUI(ActionListener)  # Main application class
├── browse_directory()            # File chooser integration
├── analyze_directory()          # Python-powered file analysis
├── organize_files()             # Smart file organization
└── actionPerformed()            # Java event handling
```

## 🛠️ Technical Details

- **GUI Framework**: Java Swing
- **File Operations**: Python `os`, `shutil`, `collections`
- **Event Handling**: Java ActionListener pattern
- **Error Handling**: Comprehensive exception management
- **Memory Efficient**: Processes files without loading into memory

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### Development Setup
```bash
git clone <repository-url>
cd jython-file-organizer
jython index.py
```

## 📄 License

This project is open source. Please check the license file for details.

## 🐛 Known Issues

- Large directories (>10,000 files) may take longer to process
- Network drives may have slower performance
- Some special characters in filenames might need handling

## 🔮 Future Enhancements

- [ ] Drag & drop functionality
- [ ] Custom organization rules
- [ ] Undo functionality
- [ ] Progress bars for large operations
- [ ] File preview capabilities
- [ ] Batch processing multiple directories

## 📞 Support

For questions, issues, or suggestions:
- Create an issue in the repository
- Contact: hexlorddev

## 🏆 Acknowledgments

- Jython development team for the amazing Python-Java bridge
- Java Swing documentation and community
- Python file handling libraries

---

**Built with ❤️ using Jython by hexlorddev**
