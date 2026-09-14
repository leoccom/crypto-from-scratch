import random
import matplotlib.pyplot as plt

ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext: str, key_map: dict[str, str]) -> str:   # returns ciphertext
    ciphertext = ""
    for char in plaintext:
        try:
            index = list(key_map.keys())[0].upper().index(char.upper())
            new_char = list(key_map.values())[0][index]
        except:
            new_char = char
        if char.isupper():
            new_char = new_char.upper()
        else:
            new_char = new_char.lower()
        ciphertext += new_char
    return ciphertext


def decrypt(ciphertext: str, key_map: dict[str, str]) -> str:  # returns plaintext
    plaintext = ""
    for char in ciphertext:
        try:
            index = list(key_map.values())[0].upper().index(char.upper())
            new_char = list(key_map.keys())[0][index]
        except:
            new_char = char
        if char.isupper():
            new_char = new_char.upper()
        else:
            new_char = new_char.lower()
        plaintext += new_char
    return plaintext


def frequency_analysis(ciphertext: str) -> dict[str, float]:   # returns letter -> frequency %
    total_chars = len([char for char in ciphertext if char.isalpha()])
    output = {}
    for alphabet in ALPHABETS:
        output[alphabet] = 0
    for char in ciphertext:
        try:
            output[char.upper()] += 1
        except:
            continue
    output = {alpha: (count_alpha / total_chars) for (alpha, count_alpha) in output.items()}
    return output

def draw_graph(frequency_dict: dict, N: int = 10):
    top_N = sorted(frequency_dict.items(), key= lambda item: item[1], reverse=True)[:N]
    x = [alpha for (alpha, _) in top_N] # Top N Alphabets
    y = [freq for (_, freq) in top_N] # Top N Frequencies

    ranks = list(range(N))

    plt.bar(ranks, y)

    # ALPHABETS
    alphabets = list(ALPHABETS)
    std_freq = [0.082  , 0.015  , 0.028  , 0.043  , 0.127  , 0.022  , 0.02   ,0.061  , 0.07   , 0.0016 , 0.0077 , 0.04   , 0.024  , 0.067  ,0.075  , 0.019  , 0.0012 , 0.06   , 0.063  , 0.091  , 0.028  ,0.0098 , 0.024  , 0.0015 , 0.02   , 0.00074]
    std_freq_top_N = sorted(dict(zip(alphabets, std_freq)).items(), key=lambda item: item[1], reverse=True)[:N]
    x_std = [alpha for (alpha, _) in std_freq_top_N] # Top N Alphabets Standard
    y_std = [freq for (_, freq) in std_freq_top_N] # Top N Frequencies Standard

    plt.plot(ranks, y_std, "ro")

    for idx, (char, val) in enumerate(zip(x_std, y_std)):
        plt.annotate(
            text=char,                     # Standard letter (e.g., 'E', 'T', 'A')
            xy=(idx, val),                 # Marker coordinate
            xytext=(0, 6),                 # 6 points above marker
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontweight="bold",
            color="darkred"
        )

    plt.xticks(ranks, x)
    plt.xlabel("Ciphertext Characters (ranked)")
    plt.ylabel("Frequencies")
    plt.title(f"Frequency Analysis: Top {N} Sample vs. Standard English")
    plt.legend()
    plt.margins(y=0.15)
    plt.tight_layout()

    plt.show()


def generate_random_key() -> dict[str, str]:                    # returns a-z shuffled substitution map
    key = ALPHABETS
    substitution = ''.join(random.sample(key, len(key)))
    return {key: substitution}

random_key = generate_random_key()
ciphertext = encrypt("""To be, or not to be: that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them? To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd. To die, to sleep;
To sleep: perchance to dream: ay, there's the rub;
For in that sleep of death what dreams may come
When we have shuffled off this mortal coil,
Must give us pause: there's the respect
That makes calamity of so long life;
For who would bear the whips and scorns of time,
The oppressor's wrong, the proud man's contumely,
The pangs of despised love, the law's delay,
The insolence of office and the spurns
That patient merit of the unworthy takes,
When he himself might his quietus make
With a bare bodkin? who would fardels bear,
To grunt and sweat under a weary life,
But that the dread of something after death,
The undiscover'd country from whose bourn
No traveller returns, puzzles the will
And makes us rather bear those ills we have
Than fly to others that we know not of?
Thus conscience does make cowards of us all;
And thus the native hue of resolution
Is sicklied o'er with the pale cast of thought,
And enterprises of great pith and moment
With this regard their currents turn awry,
And lose the name of action.--Soft you now!
The fair Ophelia! Nymph, in thy orisons
Be all my sins remember'd!""", random_key)
print(f"Encrypted Text: {ciphertext}")
frequency_dict = frequency_analysis(ciphertext)
print(f"Frequency Analysis: {frequency_dict}")
plaintext = decrypt(ciphertext, random_key)
print(f"Original Text: {plaintext}")
print(f"Random Key: {random_key}")
draw_graph(frequency_dict)