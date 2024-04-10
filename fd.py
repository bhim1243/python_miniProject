def unlock_device(pin):
    stored_pin = "1234"  # Example stored PIN
    if pin == stored_pin:
        print("PIN correct. Device unlocked.")
        # Perform actions to unlock the device (hypothetical)
    else:
        print("Incorrect PIN. Please try again.")

def main():
    pin = input("Enter your PIN: ")
    unlock_device(pin)

if __name__ == "__main__":
    main()
