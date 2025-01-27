import winreg
from datetime import datetime

def get_registry_data():
    suspicious_keys = {
        "Run": [
            r"Software\Microsoft\Windows\CurrentVersion\Run",
            r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run"
        ],
        "RunOnce": [
            r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
            r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\RunOnce"
        ],
        "Winlogon UserInit": [
            r"Software\Microsoft\Windows NT\CurrentVersion\Winlogon",
            r"Software\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Winlogon"
        ],
        "Image File Execution Options (IFEO)": [
            r"Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options",
            r"Software\WOW6432Node\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
        ],
        "BHOs": [
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects",
            r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Explorer\Browser Helper Objects"
        ],
        "AppCertDlls": [
            r"Software\Microsoft\Windows\CurrentVersion\AppCertDlls",
            r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\AppCertDlls"
        ],
        "AppInit_DLLs": [
            r"Software\Microsoft\Windows NT\CurrentVersion\AppInit_DLLs",
            r"Software\WOW6432Node\Microsoft\Windows NT\CurrentVersion\AppInit_DLLs"
        ],
        "Shell Extensions": [
            r"Software\Microsoft\Windows\CurrentVersion\Shell Extensions",
            r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Shell Extensions"
        ]
    }

    registry_data = {}

    for key_name, paths in suspicious_keys.items():
        registry_data[key_name] = []
        for path in paths:
            try:
                with winreg.OpenKey(winreg.HKEY_CURRENT_USER, path) as reg_key:
                    num_values = winreg.QueryInfoKey(reg_key)[1]
                    for i in range(num_values):
                        value_name = winreg.EnumValue(reg_key, i)[0]
                        if value_name == "UserInit" or value_name == "(Default)":  # Skip default values
                            continue
                        try:
                            value_data = winreg.QueryValueEx(reg_key, value_name)[0]
                            registry_data[key_name].append({
                                "value": value_name,
                                "data": value_data
                            })
                        except OSError:
                            pass  # Ignore if access is denied
            except FileNotFoundError:
                continue  # Skip if the key does not exist

    return registry_data

def save_to_file(data, filename):
    with open(filename, 'w') as f:
        for section, items in data.items():
            f.write(f"=== {section} ===\n")
            if not items:
                f.write("No entries found\n\n")
                continue
            for item in items:
                f.write(f"Value: {item['value']}\n")
                f.write(f"Data: {item['data']}\n\n")

def print_to_console(data):
    for section, items in data.items():
        print(f"=== {section} ===")
        if not items:
            print("No entries found\n")
            continue
        for item in items:
            print(f"Value: {item['value']}")
            print(f"Data: {item['data']}\n")

def main():
    registry_data = get_registry_data()

    # Example output to console
    print_to_console(registry_data)

    # Save to file with timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"registry_analysis_{timestamp}.txt"
    save_to_file(registry_data, filename)
    print(f"\nData saved to {filename}")

if __name__ == "__main__":
    main()
