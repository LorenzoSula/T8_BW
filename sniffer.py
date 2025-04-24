from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS
from datetime import datetime
import csv

# Generate the CSV file name with date and time
start_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
FILE_CSV = f"sniffer_log_{start_time}.csv"

# Write the header to the CSV
with open(FILE_CSV, mode='w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Source", "Source Port", "Destination", "Destination Port", "Protocol"])

# Function that displays the packets in tabular format and saves them to CSV
def display_packet(p):
    if IP in p:
        src = p[IP].src
        dst = p[IP].dst
    if TCP in p:
        sport = p[TCP].sport
        dport = p[TCP].dport
        proto = "TCP"
    elif UDP in p:
        sport = p[UDP].sport
        dport = p[UDP].dport
        proto = "UDP"
    else:
        sport = dport = "-"
        proto = "OTHER"
    
    # Print the packet in tabular format
    print(f"{src:<18} {str(sport):<5} → {dst:<18} {str(dport):<5} | {proto}")

    # Save the packet to the CSV
    with open(FILE_CSV, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([src, sport, dst, dport, proto])

# Menu to choose the packet filter
def choose_filter():
    print("\nSelect the type of packets to sniff")
    print("1. Only TCP")
    print("2. Only UDP")
    print("3. Only ICMP")
    print("4. Only DNS")
    print("5. All IP packets")
    choice = input("Choice (1-5): ")
    if choice == "1":
        return "tcp"
    elif choice == "2":
        return "udp"
    elif choice == "3":
        return "icmp"
    elif choice == "4":
        return "port 53"
    elif choice == "5":
        return "ip"
    else:
        print("Invalid choice. Using default filter: ip")
        return "ip"

# Menu for sniffing mode
def choose_mode():
    print("\nSelect sniffing mode")
    print("1. Continuous sniffing (CTRL+C to stop)")
    print("2. Sniff a specific number of packets")
    choice = input("Choice (1-2): ")
    if choice == "1":
        return 0  # infinite
    elif choice == "2":
        try:
            number = int(input("How many packets do you want to sniff? "))
            return number if number > 0 else 1
        except ValueError:
            print("Invalid input. Sniffing 1 packet.")
            return 1
    else:
        print("Invalid choice. Starting in continuous mode.")
        return 0

# Ask the user if they want to save the data to CSV
def ask_to_save_csv():
    save_choice = input("\nDo you want to save the sniffed packets to a CSV file? (yes/no): ").lower()
    if save_choice == 'yes':
        print(f"Saving the packets to {FILE_CSV}")
    else:
        print("The packets were not saved.")

# Main
if __name__ == "__main__":
    filter_choice = choose_filter()
    count = choose_mode()
    print(f"\nStarting sniffing with filter: '{filter_choice}' | Packets: {'infinite' if count == 0 else count}\n")
    print(f"{'Source':<18} {'Port':<5} → {'Destination':<18} {'Port':<5} | Protocol")
    print("-" * 65)
    sniff(filter=filter_choice, prn=display_packet, store=False, count=count)
    
    # Ask the user if they want to save the results to a CSV file
    ask_to_save_csv()
