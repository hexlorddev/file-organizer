#!/usr/bin/env jython

"""
Jython File Organizer - A GUI application that demonstrates Jython's ability
to combine Python logic with Java Swing components.

This application organizes files in a directory by their extensions,
moving them into organized subdirectories.
"""

from javax.swing import (JFrame, JPanel, JButton, JLabel, JTextField, 
                        JTextArea, JScrollPane, JFileChooser, JOptionPane,
                        BoxLayout, BorderFactory)
from java.awt import BorderLayout, FlowLayout, Dimension
from java.awt.event import ActionListener
from java.io import File
import os
import shutil
from collections import defaultdict

class FileOrganizerGUI(ActionListener):
    def __init__(self):
        self.frame = JFrame("Jython File Organizer")
        self.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.frame.setSize(600, 500)
        
        # Directory selection panel
        self.dir_panel = JPanel(FlowLayout())
        self.dir_label = JLabel("Directory:")
        self.dir_field = JTextField(30)
        self.browse_btn = JButton("Browse")
        self.browse_btn.addActionListener(self)
        
        self.dir_panel.add(self.dir_label)
        self.dir_panel.add(self.dir_field)
        self.dir_panel.add(self.browse_btn)
        
        # Control buttons panel
        self.control_panel = JPanel(FlowLayout())
        self.analyze_btn = JButton("Analyze Directory")
        self.organize_btn = JButton("Organize Files")
        self.analyze_btn.addActionListener(self)
        self.organize_btn.addActionListener(self)
        self.organize_btn.setEnabled(False)
        
        self.control_panel.add(self.analyze_btn)
        self.control_panel.add(self.organize_btn)
        
        # Results text area
        self.results_area = JTextArea(20, 50)
        self.results_area.setEditable(False)
        self.scroll_pane = JScrollPane(self.results_area)
        
        # Main panel assembly
        self.main_panel = JPanel(BorderLayout())
        
        # Top panel for directory selection and controls
        self.top_panel = JPanel()
        self.top_panel.setLayout(BoxLayout(self.top_panel, BoxLayout.Y_AXIS))
        self.top_panel.add(self.dir_panel)
        self.top_panel.add(self.control_panel)
        
        self.main_panel.add(self.top_panel, BorderLayout.NORTH)
        self.main_panel.add(self.scroll_pane, BorderLayout.CENTER)
        
        self.frame.add(self.main_panel)
        self.frame.setLocationRelativeTo(None)  # Center on screen
        
        # Data storage
        self.current_directory = None
        self.file_analysis = None
        
    def actionPerformed(self, event):
        """Handle button clicks - Java ActionListener interface implementation"""
        command = event.getActionCommand()
        
        if command == "Browse":
            self.browse_directory()
        elif command == "Analyze Directory":
            self.analyze_directory()
        elif command == "Organize Files":
            self.organize_files()
    
    def browse_directory(self):
        """Open file chooser to select directory"""
        chooser = JFileChooser()
        chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
        
        if chooser.showOpenDialog(self.frame) == JFileChooser.APPROVE_OPTION:
            selected_dir = chooser.getSelectedFile().getAbsolutePath()
            self.dir_field.setText(selected_dir)
            self.current_directory = selected_dir
            self.organize_btn.setEnabled(False)
            self.results_area.setText("")
    
    def analyze_directory(self):
        """Analyze the selected directory and show file type distribution"""
        directory = self.dir_field.getText().strip()
        
        if not directory:
            JOptionPane.showMessageDialog(self.frame, "Please select a directory first!")
            return
        
        if not os.path.exists(directory):
            JOptionPane.showMessageDialog(self.frame, "Directory does not exist!")
            return
        
        try:
            # Use Python's powerful file handling
            file_types = defaultdict(list)
            total_files = 0
            
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    total_files += 1
                    ext = os.path.splitext(filename)[1].lower()
                    if not ext:
                        ext = "no_extension"
                    file_types[ext].append(filename)
            
            # Store analysis results
            self.file_analysis = file_types
            self.current_directory = directory
            
            # Display results
            result_text = f"Analysis Results for: {directory}\n"
            result_text += "=" * 50 + "\n\n"
            result_text += f"Total files found: {total_files}\n\n"
            
            if file_types:
                result_text += "File types and counts:\n"
                for ext, files in sorted(file_types.items()):
                    ext_display = ext if ext != "no_extension" else "(no extension)"
                    result_text += f"  {ext_display}: {len(files)} files\n"
                
                result_text += "\nFiles by type:\n"
                for ext, files in sorted(file_types.items()):
                    ext_display = ext if ext != "no_extension" else "(no extension)"
                    result_text += f"\n{ext_display}:\n"
                    for filename in sorted(files)[:10]:  # Show first 10 files
                        result_text += f"  - {filename}\n"
                    if len(files) > 10:
                        result_text += f"  ... and {len(files) - 10} more files\n"
                
                self.organize_btn.setEnabled(True)
            else:
                result_text += "No files found in the directory.\n"
                self.organize_btn.setEnabled(False)
            
            self.results_area.setText(result_text)
            
        except Exception as e:
            JOptionPane.showMessageDialog(self.frame, f"Error analyzing directory: {str(e)}")
    
    def organize_files(self):
        """Organize files into subdirectories by extension"""
        if not self.file_analysis or not self.current_directory:
            JOptionPane.showMessageDialog(self.frame, "Please analyze directory first!")
            return
        
        # Confirm action
        response = JOptionPane.showConfirmDialog(
            self.frame,
            "This will move files into organized subdirectories. Continue?",
            "Confirm Organization",
            JOptionPane.YES_NO_OPTION
        )
        
        if response != JOptionPane.YES_OPTION:
            return
        
        try:
            organized_count = 0
            result_text = f"Organizing files in: {self.current_directory}\n"
            result_text += "=" * 50 + "\n\n"
            
            for ext, files in self.file_analysis.items():
                # Create subdirectory
                if ext == "no_extension":
                    subdir = os.path.join(self.current_directory, "No_Extension")
                else:
                    # Remove dot from extension for folder name
                    folder_name = ext[1:].upper() + "_Files" if ext.startswith('.') else ext.upper() + "_Files"
                    subdir = os.path.join(self.current_directory, folder_name)
                
                if not os.path.exists(subdir):
                    os.makedirs(subdir)
                    result_text += f"Created directory: {os.path.basename(subdir)}\n"
                
                # Move files
                moved_files = 0
                for filename in files:
                    src = os.path.join(self.current_directory, filename)
                    dst = os.path.join(subdir, filename)
                    
                    if os.path.exists(src) and src != dst:
                        try:
                            shutil.move(src, dst)
                            moved_files += 1
                            organized_count += 1
                        except Exception as e:
                            result_text += f"  Error moving {filename}: {str(e)}\n"
                
                if moved_files > 0:
                    result_text += f"  Moved {moved_files} {ext if ext != 'no_extension' else 'no extension'} files\n"
            
            result_text += f"\nOrganization complete! Moved {organized_count} files total.\n"
            result_text += "\nDirectory structure created:\n"
            
            # Show final directory structure
            for item in sorted(os.listdir(self.current_directory)):
                item_path = os.path.join(self.current_directory, item)
                if os.path.isdir(item_path):
                    file_count = len([f for f in os.listdir(item_path) if os.path.isfile(os.path.join(item_path, f))])
                    result_text += f"  📁 {item}/ ({file_count} files)\n"
            
            self.results_area.setText(result_text)
            self.organize_btn.setEnabled(False)
            
            JOptionPane.showMessageDialog(self.frame, f"Successfully organized {organized_count} files!")
            
        except Exception as e:
            JOptionPane.showMessageDialog(self.frame, f"Error organizing files: {str(e)}")
    
    def show(self):
        """Display the GUI"""
        self.frame.setVisible(True)

def main():
    """Main function to run the application"""
    print("Starting Jython File Organizer...")
    print("This application demonstrates Jython's ability to:")
    print("- Use Java Swing for GUI components")
    print("- Implement Java interfaces (ActionListener)")
    print("- Leverage Python's file handling capabilities")
    print("- Combine the best of both languages!")
    print()
    
    # Create and show the GUI
    app = FileOrganizerGUI()
    app.show()

if __name__ == "__main__":
    main()
