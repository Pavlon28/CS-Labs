from collections import Counter

# Initial message
message = """Unsfaxdp tgo nwqvip gvkvi ptxo rqvwqvi tgf nc wqv pdapwxwdwxnghxuqvip wqvf ovphixavo rviv
thwdtssf dpvo, tgo pn wqv cxipw twwvpwvo dpv ncwqtw jvgiv xg unsxwxhts tcctxip hnzv cinz wqv
Inztgp — tgo cinz wqv jivtwvpw Inztg nc wqvz tss. EdsxdpHtvpti wqdp xzuivppvo qxp gtzv
uviztgvgwsf xgwn hifuwnsnjf.Xw zdpw av wqtw tp pnng tp t hdswdiv qtp ivthqvo t hviwtxg
svkvs,uinatasf zvtpdivo stijvsf af xwp sxwvithf, hifuwnjituqf tuuvtippungwtgvndpsf — tp xwp
utivgwp, stgjdtjv tgo rixwxgj, uinatasf tspn oxo.Wqv zdswxusv qdztg gvvop tgo ovpxivp wqtw ovztgo
uixkthf tzngj wrnni zniv uvnusv xg wqv zxopw nc pnhxts sxcv zdpw xgvkxwtasf svto wnhifuwnsnjf
rqvivkvi zvg wqixkv tgo rqvivkvi wqvf rixwv. Hdswditsoxccdpxng pvvzp t svpp sxlvsf vyustgtwxng
cni xwp nhhdiivghv xg. pn ztgftivtp, ztgf nc wqvz oxpwtgw tgo xpnstwvo.Wqv Fvmxoxp, tg naphdiv
pvhw nc tandw 25,000 uvnusv xg, gniwqvig Xitb,dpv t hifuwxh phixuw xg wqvxi qnsf annlp avhtdpv
wqvf cvti uvipvhdwxng afwqvxi Znpsvz gvxjqanip. Wxavwtgp dpv t lxgo nc hxuqvi htssvo "ixg-
pudgp"cni nccxhxts hniivpungovghv; xw xp gtzvo cni xwp xgkvgwni Ixg-h'(qqvg-)pudgp(-ut), rqn
sxkvo xg wqv 1300p. Wqv Gpxaxox pvhivw pnhxvwf nc Gxjvixtlvvup xwp uxhwnjituqxh phixuw
cinz Vdinuvtgp tp zdhq tp unppxasvavhtdpv xw xp dpvo hqxvcsf wn vyuivpp snkv xg itwqvi oxivhw
xztjvif, tgoptzusvp tuuvti wn av tw svtpw tp unignjituqxh tp wqvf tiv hifuwnjituqxh.Wqv hifuwnjituqf
nc Wqtxstgo ovkvsnuvo dgovi Xgoxtg xgcsdvghv. Tgvzaifngxh pwdof nc wqv pdaevhw vkvg tuuvtip
xg t jitzztwxhts rnilvgwxwsvo Unitgtktlft af Qsdtgj Uitpnw Tlptitgxwx (Uqv). Ngv pfpwvz,htssvo
"wqv viixgj Pxtzvpv," pdapwxwdwvp ngv ovsxhtwv Pxtzvpv svwwvi cnitgnwqvi. Xg tgnwqvi
pfpwvz, hngpngtgwp tiv oxkxovo xgwn pvkvg jindup nc cxkv svwwvip;t svwwvi xp xgoxhtwvo af
rixwxgj wqv Pxtzvpv gdzavi nc xwp jindu tgousthxgj kviwxhts onwp dgovi xw vbdts xg gdzavi wn
wqv svwwvi'p usthv xg xwpjindu. T pfpwvz htssvo "wqv qvizxw zvwtzniuqnpxgj svwwvip" rixwvp
wqvwvyw athlrtiop.Xg wqv Vdinuv nc wqv Stwxg tsuqtavw—cinz rqxhq znovig hifuwnsnjfrndso
puixgj—hifuwnjituqf csxhlvivo rvtlsf. Rxwq wqv hnsstupv nc wqvInztg vzuxiv, Vdinuv qto usdgjvo
xgwn wqv naphdixwf nc wqv Otil Tjvp.Sxwvithf qto tss adw oxptuuvtivo. Tiwp tgo phxvghvp rviv
cnijnwwvg, tgohifuwnjituqf rtp gnw vyhvuwvo. Ngsf odixgj wqv Zxoosv Tjvp
nhhtpxngtsztgdphixuwp, rxwq tg xgcivbdvgw pxjgtwdiv ni jsnpp ni "ovn jitwxtp" wqtw tanivo zngl
udw xgwn hxuqvi wn tzdpv qxzpvsc, cxwcdssf xssdzxgtwv wqvhifuwnsnjxh otilgvpp, tgo, sxlv t
pxgjsv htgosv jdwwvixgj xg t jivtwzvoxvkts qtss, wqvxi cvvasv cstixgjp ngsf vzuqtpxmv wqv
jsnnz.Wqv pfpwvzp dpvo rviv pxzusv xg wqv vywivzv. Uqitpvp rviv rixwwvgkviwxhtssf ni athlrtiop;
onwp rviv pdapwxwdwvo cni knrvsp;cnivxjg tsuqtavwp, tp Jivvl, Qvaivr, tgo Tizvgxtg, rviv dpvo;
vthqsvwwvi nc wqv ustxgwvyw rtp ivusthvo af wqv ngv wqtw cnssnrp xw; xg wqv znpwtoktghvo
pfpwvz, puvhxts pxjgp pdapwxwdwvo cni svwwvip. Cni tsznpw twqndptgo fvtip, cinz avcniv 500
wn 1400, wqv hifuwnsnjf nc Rvpwvighxkxsxmtwxng pwtjgtwvo.
"""

message = message.upper()  # Make all letters uppercase
history = []  # To keep track of changes for reversal
transformations = {}  # To track transformations

# English letter frequencies (approximate)
english_frequency = {
    'A': 8.17, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.70, 'F': 2.23, 'G': 2.02, 'H': 6.09,
    'I': 7.00, 'J': 0.15, 'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51, 'P': 1.93,
    'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06, 'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15,
    'Y': 1.97, 'Z': 0.07
}

def print_message():
    print("Current message:\n", message)

def make_transformation():
    global message
    original_letter = input("Enter the original letter to replace (uppercase): ")
    new_letter = input("Enter the new letter (lowercase): ")

    if original_letter in message and original_letter.isupper():
        history.append(message)  # Save current state before changing
        transformations[original_letter] = new_letter  # Track the transformation
        message = message.replace(original_letter, new_letter)  # Perform transformation
        print(f"Replaced '{original_letter}' with '{new_letter}'")
    else:
        print(f"Letter '{original_letter}' not found or it's already transformed.")

def reverse_transformation():
    global message
    original_letter = input("Enter the lowercase letter to reverse: ")

    # Find the corresponding uppercase letter based on transformations
    for uppercase_letter, lowercase_letter in transformations.items():
        if lowercase_letter == original_letter:
            message = message.replace(original_letter, uppercase_letter)
            print(f"Reversed '{original_letter}' back to '{uppercase_letter}'.")
            return

    print("No corresponding uppercase letter found for the provided lowercase letter.")

def show_frequency():
    print("\nFrequency Analysis:")

    # Display original and transformed letters
    print("Original vs Transformed:")
    print(f"{'Original':<10}{'Transformed':<10}")
    print("-" * 25)
    for original, transformed in transformations.items():
        print(f"{original:<10}{transformed:<10}")

    # Count letter frequencies in the message
    letter_count = Counter(filter(str.isalpha, message))
    total_letters = sum(letter_count.values())

    # Prepare headers for message frequencies
    print("\nLetter Frequencies in the message:")
    print(f"{'Letter':<10}{'Count':<10}{'Frequency (%)':<15}")
    print("-" * 35)

    # Sort and display letter frequency in the message
    for letter, count in sorted(letter_count.items(), key=lambda item: item[1], reverse=True):
        frequency = (count / total_letters) * 100 if total_letters > 0 else 0
        print(f"{letter:<10}{count:<10}{frequency:<15.2f}")

    # Prepare headers for English letter frequencies
    print("\nEnglish Letter Frequencies:")
    print(f"{'Letter':<10}{'Frequency (%)':<15}")
    print("-" * 25)

    # Sort and display letter frequency in the English language
    for letter, frequency in sorted(english_frequency.items(), key=lambda item: item[1], reverse=True):
        print(f"{letter:<10}{frequency:<15.2f}")


def main():
    while True:
        print("\nMenu:")
        print("1. Show current message")
        print("2. Transform a letter")
        print("3. Reverse the last transformation")
        print("4. Show frequency analysis")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        if choice == '1':
            print_message()
        elif choice == '2':
            make_transformation()
        elif choice == '3':
            reverse_transformation()
        elif choice == '4':
            show_frequency()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("INVALID CHOICE! Please try again.")

if __name__ == "__main__":
    main()