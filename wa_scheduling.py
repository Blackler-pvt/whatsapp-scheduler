import pyautogui
import time
from datetime import datetime
import os
import subprocess

class WhatsAppScheduler:
    def __init__(self):
        self.messages = []
    
    def open_whatsapp(self):
        """Open WhatsApp"""
        try:
            os.system('start whatsapp:')
            print("✓ Opening WhatsApp...")
            time.sleep(5)
            return True
        except:
            pyautogui.press('win')
            time.sleep(1)
            pyautogui.write('whatsapp', interval=0.1)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(5)
            return True
    
    def copy_file_to_clipboard(self, file_path):
        """Copy file to clipboard - FIXED for paths with spaces"""
        try:
            # Normalize the path
            file_path = os.path.abspath(file_path)
            
            # Method 1: Using PowerShell with proper escaping
            # Escape double quotes inside the path and wrap entire path in quotes
            escaped_path = file_path.replace('"', '`"')
            command = f'powershell -Command "Set-Clipboard -LiteralPath \'{escaped_path}\'"'
            
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"⚠ PowerShell error: {result.stderr}")
                # Try alternative method
                return self.copy_file_alternative(file_path)
            
            print(f"✓ File copied to clipboard: {os.path.basename(file_path)}")
            return True
            
        except Exception as e:
            print(f"✗ Error copying file: {e}")
            return self.copy_file_alternative(file_path)
    
    def copy_file_alternative(self, file_path):
        """Alternative method using Python win32clipboard"""
        try:
            import win32clipboard
            import win32con
            
            # Open clipboard
            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            
            # Set file list to clipboard
            file_list = [file_path]
            
            # Convert to proper format
            data = '\x00'.join(file_list) + '\x00\x00'
            data = data.encode('utf-16le')
            
            win32clipboard.SetClipboardData(win32con.CF_HDROP, data)
            win32clipboard.CloseClipboard()
            
            print(f"✓ File copied to clipboard (alternative method)")
            return True
            
        except ImportError:
            print("⚠ Installing pywin32 for better file copy support...")
            print("Run: pip install pywin32")
            return False
        except Exception as e:
            print(f"✗ Alternative method failed: {e}")
            return False
    
    def send_message(self, phone, message, file_path=None):
        """Send message with optional media file using copy-paste"""
        try:
            print(f"\n📤 Preparing to send to {phone}...")
            
            # Open WhatsApp
            self.open_whatsapp()
            
            # Search for contact
            print("Searching contact...")
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            
            # Clear and type phone number
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(0.5)
            pyautogui.press('delete')
            time.sleep(0.5)
            
            print(f"Typing: {phone}")
            pyautogui.write(phone, interval=0.15)
            time.sleep(3)
            
            # Select contact
            print("Opening chat...")
            pyautogui.press('down')
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(2)
            
            # If file is provided, send file first
            if file_path and os.path.exists(file_path):
                print(f"📎 Sending file: {os.path.basename(file_path)}")
                
                # Copy file to clipboard
                if self.copy_file_to_clipboard(file_path):
                    time.sleep(1)
                    
                    # Click on message box
                    pyautogui.click(700, 748)
                    time.sleep(1)
                    
                    # Paste file (Ctrl+V)
                    print("Pasting file...")
                    pyautogui.hotkey('ctrl', 'v')
                    time.sleep(4)  # Wait for file preview to load
                    
                    # Add caption if message is provided
                    if message:
                        print("Adding caption...")
                        time.sleep(1)
                        for char in message:
                            pyautogui.write(char, interval=0.05)
                        time.sleep(1)
                    
                    # Send
                    print("Sending...")
                    pyautogui.press('enter')
                    time.sleep(2)
                else:
                    print("⚠ Failed to copy file, skipping...")
                    return False
                
            # If no file, just send text message
            elif message:
                print("Typing message...")
                pyautogui.click(700, 748)
                time.sleep(1)
                
                for char in message:
                    pyautogui.write(char, interval=0.05)
                
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(2)
            
            print(f"✓ Sent at {datetime.now().strftime('%H:%M:%S')}")
            return True
            
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def add_message(self, phone, message, date_time, file_path=None):
        """Add message/media to schedule"""
        try:
            target_dt = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
            
            # Validate file path if provided
            if file_path:
                if not os.path.exists(file_path):
                    print(f"⚠ Warning: File not found: {file_path}")
                    return
                else:
                    print(f"✓ File validated: {os.path.basename(file_path)}")
            
            self.messages.append({
                'phone': phone,
                'message': message,
                'file_path': file_path,
                'datetime': target_dt,
                'sent': False
            })
            
            if file_path:
                print(f"✓ Scheduled media for {date_time}")
            else:
                print(f"✓ Scheduled message for {date_time}")
                
        except ValueError:
            print("✗ Invalid format. Use 'YYYY-MM-DD HH:MM'")
    
    def send_pending(self):
        """Send pending messages"""
        current = datetime.now()
        
        for msg in self.messages:
            if not msg['sent']:
                diff = (current - msg['datetime']).total_seconds()
                
                if 0 <= diff <= 60:
                    self.send_message(
                        msg['phone'], 
                        msg['message'], 
                        msg.get('file_path')
                    )
                    msg['sent'] = True
                    time.sleep(3)
    
    def show_status(self):
        """Show status"""
        print("\n" + "="*70)
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70)
        
        pending = [m for m in self.messages if not m['sent']]
        sent = [m for m in self.messages if m['sent']]
        
        print(f"Pending: {len(pending)} | Sent: {len(sent)}")
        
        if pending:
            print("\nNext messages:")
            for msg in pending[:5]:
                media_type = "📎" if msg.get('file_path') else "💬"
                file_name = os.path.basename(msg['file_path']) if msg.get('file_path') else ""
                time_str = msg['datetime'].strftime('%H:%M')
                print(f"  {media_type} {msg['phone']} at {time_str} {file_name}")
        print("="*70 + "\n")
    
    def run(self):
        """Start scheduler"""
        print("\n" + "="*70)
        print("WhatsApp Scheduler - Media Support (Fixed for Spaces in Path)")
        print("Press Ctrl+C to stop")
        print("="*70)
        
        self.show_status()
        
        try:
            while True:
                self.send_pending()
                time.sleep(30)
        except KeyboardInterrupt:
            print("\n\n" + "="*70)
            print("Scheduler Stopped")
            print("="*70)
            self.show_status()


# ========== USAGE EXAMPLES ==========

if __name__ == "__main__":
    scheduler = WhatsAppScheduler()
    
    # Example with path containing spaces - NOW WORKS!
    scheduler.add_message(
        phone="9xxxxxxxxxx",
        message="Video file with spaces in path",
        date_time="2025-11-16 17:12",
        file_path=r"C:\Users\aswin\Pictures\Screenshots\Screenshot (10).png"
    )
    
    # # More examples
    scheduler.add_message(
        phone="8xxxxxxxxxx",
        message="Another file",
        date_time="2025-11-16 17:13",
        file_path=r"C:\Users\aswin\Pictures\Screenshots\Screenshot 2025-11-15 192024.png"
    )
    
    scheduler.add_message(
        phone="9xxxxxxxxx",
        message="T kudicha",
        date_time="2025-11-16 17:14"
        # file_path=r"C:\Users\aswin\Pictures\photo.jpg"
    )
    
    # # Start the scheduler
    scheduler.run()
    
    # instant message
    # scheduler.send_message(
    #     phone="9487656235",
    #     message="Sample",
    #     file_path=r"C:\SD card\videos\VID20210102135923.mp4"
    # )
